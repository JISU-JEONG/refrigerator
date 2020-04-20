<template>
  <div class="container">
    <div class="picture-container">
      <div class="before-take" v-if="!image">
        <div>
          <p>Plz Take Pic</p>
          <label for="ex_file">Take</label>
          <input type="file" @change="onFileChange" id="ex_file"/>
        </div>
      </div>
      <div class="after-take" v-else>
        <div class="option left">
          <v-icon  @click="removeImage">mdi-rotate-right</v-icon>
          <p>RE</p>
        </div>
        <div class="option right">
          <v-icon>mdi-arrow-right</v-icon>
          <p>SEND</p>
        </div>
        <img :src="image">
      </div>
    </div>
    <div class="material-container">

    </div>
  </div>
  <!-- <div class="img">
    <div v-if="!image">
      <h2>Select an image</h2>
      <input type="file" @change="onFileChange" />
    </div>
    <div v-else>
      <img :src="image" />
      <button @click="removeImage">Remove image</button>
    </div>
    <br />
    <input type="checkbox" id="one" value="One" v-model="picked" />
    <label for="one">One</label>
    <br />
    <input type="checkbox" id="two" value="Two" v-model="picked" />
    <label for="two">Two</label>
    <br />
    <span>선택: {{ picked }}</span>
  </div> -->
</template>

<script>
export default {
  name: "RecipeRecommendation",
  components: {},
  data: () => ({
    image: "",
    picked: [],
    show: true,
    materials : ['??', '??', '??', '???', '??', '??', '??', '??', '???', '??', '??', '??', '??' ]
  }),
  methods: {
    onFileChange(e) {
      var files = e.target.files || e.dataTransfer.files;
      if (!files.length) return;
      this.createImage(files[0]);
    },
    createImage(file) {
      var image = new Image();
      var reader = new FileReader();
      var vm = this;

      reader.onload = e => {
        vm.image = e.target.result;
      };
      reader.readAsDataURL(file);
    },
    removeImage: function(e) {
      this.image = "";
    },
    clickMaterial() { 
      if (event.target.nodeName === 'INPUT') {
        console.log(event.target.parentElement.previousElementSibling)
      }
      
    }
  }
};
</script>

<style scoped lang="scss">
  div { box-sizing: border-box; }
  .container { width: 100vw; height: 100vh; margin:0; padding: 80px 0 0 0; }
  .picture-container { width:100%; height: 40%; position:relative; box-sizing: border-box; border: 1px green solid; }
  .before-take { width:100%; height: 100%; position: relative; text-align: center; }
  .before-take>div { margin: 0; position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); }
  .before-take>div input { position: absolute; width: 1px; height: 1px; padding: 0; margin: -1px; overflow: hidden; clip:rect(0,0,0,0); border: 0; }
  .before-take>div label {display: inline-block; padding: .5em .75em; color: #fff; font-size: inherit; line-height: normal; vertical-align: middle; background-color: #337ab7; cursor: pointer; border: 1px solid #2e6da4; border-bottom-color: #e2e2e2; border-radius: .25em; }
  .picture-container img { width: 40%; height: auto; position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); }
  .picture { width: 100%; height: 80%; border: 1px black solid; }
  .option { position: absolute; width: 10%; top: 50%; transform: translateY(-50%); text-align: center; }
  .option p { margin: 0;}
  .left { left: 5%; }
  .right { right:5%;  }


/* .img {
  width: 100%;
  height: 100vh;
  padding-top: 80px;

  text-align: center;
}
img {
  width: 30%;
  margin: auto;
  display: block;
  margin-bottom: 10px;
} */
</style>
