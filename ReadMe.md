# Sub02 - AI



## req 1 이미지 데이터 전처리

### req 1-1, 1-2 이미지 데이터 전처리 및 이미지 정규화

```python
def Standardization(encode_train, standard):

	def image_load(image_path):
		img = tf.io.read_file(image_path)
		img = tf.image.decode_jpeg(img, channels=3)
		img = tf.image.resize(img, (299, 299))
		if standard:
			img = tf.keras.applications.inception_v3.preprocess_input(img)
		return img, image_path

	image_dataset = tf.data.Dataset.from_tensor_slices(encode_train)
	image_dataset = image_dataset.map(image_load, num_parallel_calls=tf.data.experimental.AUTOTUNE).batch(16)

	return image_dataset
```

standard 값에 따라서 이미지의 정규화의 유무를 결정한다. 정규화된 이미지 데이터 들을 Dataset으로 저장을 하고 속도 향상을 위해서 batch를 16 크기로 반환을 해주었다.



## req 2 텍스트 데이터 전처리

### req 2-1, 2-2 텍스트 데이터 토큰화 및 Tokenizer 저장 및 불러오기

```python
def save_tokenizer(captions,top_k):
	tokenizer = tf.keras.preprocessing.text.Tokenizer(num_words=top_k,
	                                                  oov_token="<unk>",
	                                                  filters='!"#$%&()*+.,-/:;=?@[\]^_`{|}~ ')
	tokenizer.fit_on_texts((map(lambda x: '<start> '+x+' <end>', captions)))
	
	# tokenizer.word_index['<start>'] = 0
	# tokenizer.index_word[0] = '<start>'
	# tokenizer.word_index['<end>'] = 1
	# tokenizer.index_word[1] = '<end>'
	tokenizer.word_index['<pad>'] = 0
	tokenizer.index_word[0] = '<pad>'
	train_seqs = tokenizer.texts_to_sequences(captions)
	with open("tokenizer.pickle","wb") as fw:
		pickle.dump(tokenizer, fw)
	return
```

 캡션과 top_k를 받아 top_k의 갯수만큼 단어를 토큰화 한다. 이때 포함되지 않은 단어들은 <unk>로 처리를 해주면서 캡션을 토큰화 하기 전에 문장들에 <start> '+x+' <end>' 처리를 해주어서 붙여준다.

 tokenizer.index_word[0]는 예약어로 유저가 설정할수 있으며 <pad>를 예약어 설정을 해주었다.  토큰화가 다 되었으면 pickle 파일로 저장해 주었다.



```python
with open('tokenizer.pickle', 'rb') as f:
		tokenizer = pickle.load(f)

train_seqs = tokenizer.texts_to_sequences(train_captions)
cap_vector = tf.keras.preprocessing.sequence.pad_sequences(train_seqs, padding='post',value=0)
```

토큰화된 데이터를 불러와서 길이를 가장 긴 문장의 길이로 통일을 해준다. 이때 짧은 문장들의 부족한 부분의 위에서 설정된 예약어 <pad>로 채워준다.



## req 3 Dataset 생성 함수 구현

### req 3-1 tf.data.Dataset 생성

위에 Standardization 함수에서 처리함

### req 3-2 Image Data Augmentation

```python
def Augmentation(img):
	image = img.numpy()
	x = image.reshape((1,) + image.shape)
	datagen = ImageDataGenerator(
        rotation_range=40,
        width_shift_range=0.2,
        height_shift_range=0.2,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        fill_mode='nearest')
	i = 0
	lst = []
	for batch in datagen.flow(x):
		i += 1
		if i > 3: break  # 이미지 20장을 생성하고 마칩니다
		batch = batch.reshape(299,299,3)
		lst.append(batch)
	return lst
```

이미지를 받아서 매번 랜덤하고 다양하게 Augmentation 적용한 이미지 리스트를 반환해 준다. 학습시간 관계상 여기서는 3개의 변환된 이미지 리스트를 반환하게 했다.



## req 4 이미지 모델(Encoder) 구현

### req 4-1 Pre-trained 모델로 특성 추출

```python
image_model = tf.keras.applications.InceptionV3(include_top=False, weights='imagenet')

new_input = image_model.input
hidden_layer = image_model.layers[-1].output

image_features_extract_model = tf.keras.Model(new_input, hidden_layer)

# Get unique images
encode_train = sorted(set(img_name_vector))

image_dataset = utils.Standardization(encode_train,1)

for imgs, paths in tqdm(image_dataset):
	for img,path in zip(imgs,paths):
		cnt = 0
		for image in utils.Augmentation(img):
			image = tf.reshape(image,(1,299,299,3))
			batch_features = image_features_extract_model(image)
			batch_features = tf.reshape(batch_features,(-1, batch_features.shape[3]))
			path_of_feature = path.numpy().decode("utf-8")
			np.save(path_of_feature+'_'+str(cnt), batch_fatures)
			cnt += 1

            
image_features_extract_model.save('image_features_extract_model.h5')
```

Augmentation이 적용도니 이미지 (299,299,3)의 형태를 전처리 학습을 위해서 (1,299,299,3) 형태로 변환해 준다. 전처리 학습에 사용되어 리턴된 이미지는 (8,8,2048)의 모양을 가지며 이것을 (64,2048)의 형태로 변환하여 npy파일에 저장하여 준다. 이때 저장된 npy파일들의 이름은 이미지이름+_0,1,2 등의 파일이름으로 저장하여 준다.

마지막으로 image_features_extract_model.h5 파일로 Pre-trained  모델을 저장 차 후 predict.py에서 사용을 한다.



### req 4-2 Feature Encoder 구현

```python
class CNN_Encoder(tf.keras.Model):

    # Since you have already extracted the features and dumped it using pickle
    # This encoder passes those features through a Fully connected layer
	def __init__(self, embedding_dim):

		super(CNN_Encoder, self).__init__()
        # shape after fc == (batch_size, 64, embedding_dim)
		self.fc = tf.keras.layers.Dense(embedding_dim)
	
	def call(self, x):
		x = self.fc(x)
		x = tf.nn.relu(x)
		return x
    
encoder = CNN_Encoder(embedding_dim)
```

RNN Decoder의 입력 형식에 맞추기 위해서 CNN_Enconder 구현



## req 5 텍스트 모델(Decoder) 구현

### req 5-1 임베딩 레이어 구현

```python
class BahdanauAttention(tf.keras.Model):
	def __init__(self, units):
		super(BahdanauAttention, self).__init__()
		self.W1 = tf.keras.layers.Dense(units)
		self.W2 = tf.keras.layers.Dense(units)
		self.V = tf.keras.layers.Dense(1)
	
	def call(self, features, hidden):
		# features(CNN_encoder output) shape == (batch_size, 64, embedding_dim)

		# hidden shape == (batch_size, hidden_size)
		# hidden_with_time_axis shape == (batch_size, 1, hidden_size)
		hidden_with_time_axis = tf.expand_dims(hidden, 1)

		# score shape == (batch_size, 64, hidden_size)
		score = tf.nn.tanh(self.W1(features) + self.W2(hidden_with_time_axis))

		# attention_weights shape == (batch_size, 64, 1)
		# you get 1 at the last axis because you are applying score to self.V
		attention_weights = tf.nn.softmax(self.V(score), axis=1)

		# context_vector shape after sum == (batch_size, hidden_size)
		context_vector = attention_weights * features
		context_vector = tf.reduce_sum(context_vector, axis=1)
		return context_vector, attention_weights

class RNN_Decoder(tf.keras.Model):
	def __init__(self, embedding_dim, units, vocab_size):
		super(RNN_Decoder, self).__init__()
		self.units = units

		self.embedding = tf.keras.layers.Embedding(vocab_size, embedding_dim)
		self.gru = tf.keras.layers.GRU(self.units,
									return_sequences=True,
									return_state=True,
									recurrent_initializer='glorot_uniform')
		self.fc1 = tf.keras.layers.Dense(self.units)
		self.fc2 = tf.keras.layers.Dense(vocab_size)

		self.attention = BahdanauAttention(self.units)

	def call(self, x, features, hidden):
		# defining attention as a separate model
		context_vector, attention_weights = self.attention(features, hidden)

		# x shape after passing through embedding == (batch_size, 1, embedding_dim)
		x = self.embedding(x)

		# x shape after concatenation == (batch_size, 1, embedding_dim + hidden_size)
		x = tf.concat([tf.expand_dims(context_vector, 1), x], axis=-1)

		# passing the concatenated vector to the GRU
		output, state = self.gru(x)

		# shape == (batch_size, max_length, hidden_size)
		x = self.fc1(output)

		# x shape == (batch_size * max_length, hidden_size)
		x = tf.reshape(x, (-1, x.shape[2]))

		# output shape == (batch_size * max_length, vocab)
		x = self.fc2(x)
	
		return x, state, attention_weights
	
	def reset_state(self, batch_size):
		return tf.zeros((batch_size, self.units))
    
decoder = RNN_Decoder(embedding_dim, units, vocab_size)
```

- InvolutionV3의 하위 컨벌루션 레이어에서 형상을 추출하여 모양 벡터 (8, 8, 2048)를 제공.
- (64, 2048)의 모양으로 reshape.
- 다음이벡터는 CNN 인코더 (단일 완전 연결된 레이어로 구성)를 통과.
- RNN (여기서는 GRU)이 다음 단어를 예측하기 위해 이미지를 살펴봄.



## req 6 train.py 구현



```python
loss_plot = []

@tf.function
def train_step(img_tensor, target):
	loss = 0

	# initializing the hidden state for each batch
	# # because the captions are not related from image to image
	hidden = decoder.reset_state(batch_size=target.shape[0])

	dec_input = tf.expand_dims([tokenizer.word_index['<start>']] * target.shape[0], 1)
	with tf.GradientTape() as tape:
		features = encoder(img_tensor)
		for i in range(1, target.shape[1]):
			# passing the features through the decoder
			predictions, hidden, _ = decoder(dec_input, features, hidden)
			
			loss += loss_function(target[:, i], predictions)
			# using teacher forcing
			dec_input = tf.expand_dims(target[:, i], 1)

	total_loss = (loss / int(target.shape[1]))
	trainable_variables = encoder.trainable_variables + decoder.trainable_variables
	gradients = tape.gradient(loss, trainable_variables)
	optimizer.apply_gradients(zip(gradients, trainable_variables))
	
	return loss, total_loss


EPOCHS = 20

for epoch in range(start_epoch, EPOCHS):
	start = time.time()
	total_loss = 0

	for (batch, (img_tensor, target)) in enumerate(dataset):
		batch_loss, t_loss = train_step(img_tensor, target)
		total_loss += t_loss
		
		if batch % 100 == 0:
			print ('Epoch {} Batch {} Loss {:.4f}'.format(
				epoch + 1, batch, batch_loss.numpy() / int(target.shape[1])))
    # storing the epoch end loss value to plot later
	loss_plot.append(total_loss / num_steps)
	
	if epoch % 5 == 0:
		ckpt_manager.save()

	print ('Epoch {} Loss {:.6f}'.format(epoch + 1,total_loss/num_steps))
	print ('Time taken for 1 epoch {} sec\n'.format(time.time() - start))

plt.plot(loss_plot)
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.title('Loss Plot')
plt.show()
```

- 각 `.npy`파일에 저장된 기능을 추출한 다음 해당 기능을 인코더를 통해 전달합.
- 엔코더 출력, 숨겨진 상태 (0으로 초기화 됨) 및 디코더 입력 (시작 토큰)은 디코더로 전달.
- 디코더는 예측 및 디코더 숨겨진 상태를 반환.
- 그런 다음 디코더 숨겨진 상태가 모델로 다시 전달되고 예측은 손실을 계산하는 데 사용.
- 티쳐 포싱를 사용하여 디코더에 대한 다음 입력을 결정.
- 티쳐 포싱는 대상 단어가 다음 입력으로 디코더에 전달하는 것.
- 마지막 단계는 그라디언트를 계산하고이를 옵티 마이저 및 역전파에 적용.



## req 7,8 predict.py 구현 및 체크포인터 매니저

```python
import config
from data import preprocess 
from utils import utils
import random
# # config 저장
utils.save_config()

# # 이미지 경로 및 캡션 불러오기
# img_paths, captions = preprocess.get_path_caption()
# utils.save_tokenizer(captions)
# dataset = utils.Dataset_setting(img_paths,captions)
def load_image(image_path):
		img = tf.io.read_file(image_path)
		img = tf.image.decode_jpeg(img, channels=3)
		img = tf.image.resize(img, (299, 299))
		img = tf.keras.applications.inception_v3.preprocess_input(img)
		return img, image_path
# cnt =0
# for x, y in dataset:
#     if cnt==1: break
#     print(x)
#     utils.Augmentation(x)
#     cnt+=1

# 전체 데이터셋을 분리해 저장하기
# train_dataset_path, val_dataset_path = preprocess.dataset_split_save()

# 저장된 데이터셋 불러오기
# img_paths, caption = preprocess.get_data_file(train_dataset_path)

# print(utils.Standardization(img_paths[0],1))

# 데이터 샘플링
# if config.do_sampling:
#     img_paths, caption = preprocess.sampling_data(img_paths, caption, 1000)
# 이미지와 캡션 시각화 하기
# utils.visualize_img_caption(img_paths,caption,1)

# preprocess.token(captions)

import tensorflow as tf
physical_devices = tf.config.experimental.list_physical_devices('GPU')
assert len(physical_devices) > 0, "Not enough GPU hardware devices available"
config = tf.config.experimental.set_memory_growth(physical_devices[0], True)
import os
os.environ["CUDA_VISIBLE_DEVICES"] = '1'
# You'll generate plots of attention in order to see which parts of an image
# our model focuses on during captioning
import matplotlib.pyplot as plt

from tqdm import tqdm
# Scikit-learn includes many helpful utilities
from sklearn.model_selection import train_test_split
from sklearn.utils import shuffle

import re
import numpy as np
import os
import time
import json
from glob import glob
from PIL import Image
import pickle

# Store captions and image names in vectors
img_paths, captions = preprocess.get_path_caption()
captions = list(map(lambda x: '<start> ' + x + ' <end>', captions))
def calc_max_length(tensor):
    return max(len(t) for t in tensor)

# Calculates the max_length, which is used to store the attention weights
max_length = calc_max_length(captions)

class BahdanauAttention(tf.keras.Model):
	def __init__(self, units):
		super(BahdanauAttention, self).__init__()
		self.W1 = tf.keras.layers.Dense(units)
		self.W2 = tf.keras.layers.Dense(units)
		self.V = tf.keras.layers.Dense(1)
	
	def call(self, features, hidden):
		# features(CNN_encoder output) shape == (batch_size, 64, embedding_dim)

		# hidden shape == (batch_size, hidden_size)
		# hidden_with_time_axis shape == (batch_size, 1, hidden_size)
		hidden_with_time_axis = tf.expand_dims(hidden, 1)

		# score shape == (batch_size, 64, hidden_size)
		score = tf.nn.tanh(self.W1(features) + self.W2(hidden_with_time_axis))

		# attention_weights shape == (batch_size, 64, 1)
		# you get 1 at the last axis because you are applying score to self.V
		attention_weights = tf.nn.softmax(self.V(score), axis=1)

		# context_vector shape after sum == (batch_size, hidden_size)
		context_vector = attention_weights * features
		context_vector = tf.reduce_sum(context_vector, axis=1)
		return context_vector, attention_weights

class CNN_Encoder(tf.keras.Model):

    # Since you have already extracted the features and dumped it using pickle
    # This encoder passes those features through a Fully connected layer
	def __init__(self, embedding_dim):

		super(CNN_Encoder, self).__init__()
        # shape after fc == (batch_size, 64, embedding_dim)
		self.fc = tf.keras.layers.Dense(embedding_dim)
	
	def call(self, x):
		x = self.fc(x)
		x = tf.nn.relu(x)
		return x


class RNN_Decoder(tf.keras.Model):
	def __init__(self, embedding_dim, units, vocab_size):
		super(RNN_Decoder, self).__init__()
		self.units = units

		self.embedding = tf.keras.layers.Embedding(vocab_size, embedding_dim)
		self.gru = tf.keras.layers.GRU(self.units,
									return_sequences=True,
									return_state=True,
									recurrent_initializer='glorot_uniform')
		self.fc1 = tf.keras.layers.Dense(self.units)
		self.fc2 = tf.keras.layers.Dense(vocab_size)

		self.attention = BahdanauAttention(self.units)

	def call(self, x, features, hidden):
		# defining attention as a separate model
		context_vector, attention_weights = self.attention(features, hidden)

		# x shape after passing through embedding == (batch_size, 1, embedding_dim)
		x = self.embedding(x)

		# x shape after concatenation == (batch_size, 1, embedding_dim + hidden_size)
		x = tf.concat([tf.expand_dims(context_vector, 1), x], axis=-1)

		# passing the concatenated vector to the GRU
		output, state = self.gru(x)

		# shape == (batch_size, max_length, hidden_size)
		x = self.fc1(output)

		# x shape == (batch_size * max_length, hidden_size)
		x = tf.reshape(x, (-1, x.shape[2]))

		# output shape == (batch_size * max_length, vocab)
		x = self.fc2(x)
	
		return x, state, attention_weights
	
	def reset_state(self, batch_size):
		return tf.zeros((batch_size, self.units))
embedding_dim = 256
units = 512
vocab_size = 5001
with open('tokenizer.pickle', 'rb') as f:
		tokenizer = pickle.load(f)

image_features_extract_model = tf.keras.models.load_model('image_features_extract_model.h5')
encoder = CNN_Encoder(embedding_dim)
decoder = RNN_Decoder(embedding_dim, units, vocab_size)

optimizer = tf.keras.optimizers.Adam()
loss_object = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True, reduction='none')

def loss_function(real, pred):
	mask = tf.math.logical_not(tf.math.equal(real, 0))
	loss_ = loss_object(real, pred)
	mask = tf.cast(mask, dtype=loss_.dtype)
	loss_ *= mask
	
	return tf.reduce_mean(loss_)

checkpoint_path = "./checkpoints/train"
ckpt = tf.train.Checkpoint(encoder=encoder,decoder=decoder, optimizer = optimizer)
ckpt_manager = tf.train.CheckpointManager(ckpt, checkpoint_path, max_to_keep=5)

start_epoch = 0
if ckpt_manager.latest_checkpoint:
	start_epoch = int(ckpt_manager.latest_checkpoint.split('-')[-1])

	# restoring the latest checkpoint in checkpoint_path
	ckpt.restore(ckpt_manager.latest_checkpoint)


def evaluate(image):
    attention_plot = np.zeros((max_length, 64))

    hidden = decoder.reset_state(batch_size=1)

    temp_input = tf.expand_dims(load_image(image)[0], 0)
    img_tensor_val = image_features_extract_model(temp_input)
    img_tensor_val = tf.reshape(img_tensor_val, (img_tensor_val.shape[0], -1, img_tensor_val.shape[3]))

    features = encoder(img_tensor_val)

    dec_input = tf.expand_dims([tokenizer.word_index['<start>']], 0)
    result = []

    for i in range(max_length):
        predictions, hidden, attention_weights = decoder(dec_input, features, hidden)

        attention_plot[i] = tf.reshape(attention_weights, (-1, )).numpy()

        predicted_id = tf.random.categorical(predictions, 1)[0][0].numpy()
        result.append(tokenizer.index_word[predicted_id])

        if tokenizer.index_word[predicted_id] == '<end>':
            return result, attention_plot

        dec_input = tf.expand_dims([predicted_id], 0)

    attention_plot = attention_plot[:len(result), :]
    return result, attention_plot

def plot_attention(image, result,caption):
    temp_image = np.array(Image.open(image))
    plt.title('Prediction Caption: '+' '.join(result)+'\n'+'Real Caption:'+''.join(caption))
    plt.imshow(temp_image)
    plt.show()

idx = random.randrange(0,len(captions))
image_path =img_paths[idx]
# captions
result, attention_plot = evaluate(image_path)
plot_attention(image_path, result, captions[idx])

```

* image_features_extract_model = tf.keras.models.load_model('image_features_extract_model.h5') 를 통해서 전처리 되었던 모델을 불러온다.
* 체크포인트에 저장되었던 encoder 및 decoder를 불러옴
* 이미지를 받아서 예측 및 출력



## Req. 9. 팀별 인공지능 서비스 기획안 작성

### Req. 9-1 데이터셋 검색 및 선정

- [공공데이터포털](https://www.data.go.kr/) - 농수축산물 안심레시피 정보

### Req. 9-2 기존 서비스 검색

- [만개의레시피](https://www.10000recipe.com/) - 원하는 음식의 레시피를 제공하는 사이트

![image](https://user-images.githubusercontent.com/52814897/78846407-a43d4680-7a46-11ea-847a-28ac99cad86c.png)

- [Pic2Recipe](http://pic2recipe.csail.mit.edu/) - 음식 사진을 찍으면 해당 음식의 레시피를 알려주는 서비스

![image](https://user-images.githubusercontent.com/52814897/78952869-e67f8a00-7b11-11ea-833a-83584585ef71.png)

### Req. 9-3 팀만의 서비스 기획

현재의 상황처럼 외출이 자유롭지 않거나 배달 음식을 시킬 여건이 되지 않을 때, 이미지 분석 및 인공지능을 통해 냉장고 안의 활용가능한 재료를 분석하고 그 재료로 만들 수 있는 음식 및 레시피를 제공해주는 서비스

#### 기술스택

- Front-End - Vue.js

- Back-End - Django

- DB - MySQL

- Core - Tensorflow

### Req. 9-4 개발 일정 수립

#### 역할 분담

- Front-End - 김태우, 정영길
- Back-End - 김기은, 정영훈
- Core - 서용재, 정지수(팀장)

#### 개발 일정

1~2주차 : 제공 서비스 구체화, 핵심 기능 구현

3주차 - 부가 기능 구현

