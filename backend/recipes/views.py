from django.shortcuts import render, get_object_or_404, redirect
from IPython import embed
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
# Create your views here.

@api_view(['GET'])
def basicinfo(request):
  recipebasic = RecipeBasicInfo.objects.all()
  serializer = RecipeBasicInfoSerializer(recipebasic, many=True)
  # embed()
  return Response(serializer.data)
  
@api_view(['GET'])
def materialinfo(request, basic_pk):
  materials = RecipeMaterialInfo.objects.filter(material_code=basic_pk)
  # for i in materials:
  #   print(i.material_name)

  serializer = RecipeMaterialInfoSerializer(materials, many=True)
  # embed()
  return Response(serializer.data)

@api_view(['GET'])
def processinfo(request, basic_pk):
  process = RecipeProcessInfo.objects.filter(process_code=basic_pk)
  process = process.order_by('process_order')
  serializer = RecipeProcessInfoSerializer(process, many=True)
  # embed()
  return Response(serializer.data)

@api_view(['GET'])
def materialcheck(request):
  # 사진에서 인식한 재료
  get_materials = ['베이컨', '양배추', '소고기', '대파', '쌀', '고구마 큰거', '올리브유', '소면', '물', '포도']
  # 사용자가 선택할 조미료
  get_cond = ['설탕', '소금']
  all_materials = set(get_materials + get_cond)

  all_dishes = RecipeBasicInfo.objects.all()
  dish_list = []
  for dish in all_dishes:
    recipe_materials = RecipeMaterialInfo.objects.filter(material_code=dish.basic_code)
    cnt = 0
    for r_m in recipe_materials:
      for a_m in all_materials:
        if r_m.material_name == a_m:
          cnt += 1

    if len(recipe_materials) == cnt:
      dish_list.append(dish.basic_code)
  # embed()
  dish_list = RecipeBasicInfo.objects.filter(basic_code__in=dish_list)
  serializer = RecipeBasicInfoSerializer(dish_list, many=True)
  return Response(serializer.data)

from .forms import *
import matplotlib.pyplot as plt
from PIL import Image
import tensorflow as tf
@api_view(['POST'])
def image_upload(request):
  img = request.FILES.get('file').read()
  # 배열 변환
  img = tf.image.decode_jpeg(img)
  plt.imshow(img)
  plt.show()
  # embed()
  pass

  