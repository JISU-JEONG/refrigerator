<template>
  <div class="container">
    <!-- <div class="picture-container"> ?? ??????.
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
        <div class="option right" @click="onSubmitImage">
          <v-icon>mdi-arrow-right</v-icon>
          <p>SEND</p>
        </div>
        <img :src="image">
      </div>
    </div> -->
    <div class="material-container">
      <div class="material-card">
        <p>Select materials</p>
        <ul @click="onClcikMaterial">
          <div class="hello-container"></div>
          <li v-for="material in materials" :key="material">
            {{ material }}
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "RecipeRecommendation",
  components: {},
  data: () => ({
    image: "",
    uploadedImage: new FormData(),
    picked: [],
    show: true,
    materials: [
      "salt",
      "sugar",
      "pepper",
      "sauce1",
      "sauce1",
      "sauce1",
      "sauce1",
      "sauce1",
      "sauce1",
      "sauce1",
      "sauce1",
      "sauce1",
      "sauce1",
      "sauce1",
      "sauce1",
      "sauce1",
      "sauce1",
      "sauce1",
      "sauce1",
      "sauce1",
      "sauce1",
      "sauce1",
      "sauce1",
      "sauce1",
      "sauce1",
      "sauce1"
    ],
    main: [],
    sub: []
  }),
  methods: {
    onFileChange(e) {
      var files = e.target.files || e.dataTransfer.files;
      if (!files.length) return;
      this.uploadedImage.append("image", files[0]);
      console.log(this.uploadedImage.get("image"));
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
    onSubmitImage() {
      const imageFormData = new FormData();
    },
    onClcikMaterial() {
      const target = event.target;
      if (target.nodeName === "LI") {
        const material = target.innerText;
        if (target.classList.contains("on")) {
          this.sub.splice(
            this.sub.findIndex(elm => elm === material),
            1
          );
        } else {
          this.sub.push(material);
        }
        console.log(this.sub);
        target.classList.toggle("on");
      }
    }
  }
};
</script>

<style scoped lang="scss">
div {
  box-sizing: border-box;
}
.container {
  width: 100%;
  height: 100vh;
  margin: 0;
  padding: 70px 0 0 0;
  background: #f1f1f1;
}
/* .picture-container { width:100%; height: 40%; position:relative; box-sizing: border-box; border: 1px green solid;}
  .before-take { width:100%; height: 100%; position: relative; text-align: center; }
  .before-take>div { margin: 0; position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); }
  .before-take>div input { position: absolute; width: 1px; height: 1px; padding: 0; margin: -1px; overflow: hidden; clip:rect(0,0,0,0); border: 0; }
  .before-take>div label {display: inline-block; padding: .5em .75em; color: #fff; font-size: inherit; line-height: normal; vertical-align: middle; background-color: #337ab7; cursor: pointer; border: 1px solid #2e6da4; border-bottom-color: #e2e2e2; border-radius: .25em; }
  .picture-container img { width: 40%; height: auto; position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); }
  .picture { width: 100%; height: 80%; border: 1px black solid; }
  .option { position: absolute; width: 10%; top: 50%; transform: translateY(-50%); text-align: center; cursor: pointer;}
  .option p { margin: 0;}
  .left { left: 5%; }
  .right { right:5%;  } */
.material-card {
  height: 100%;
  text-align: center;
}
.material-card > p {
  margin: 0;
  font-size: 24px;
  font-weight: 700;
  color: rgb(65, 65, 65);
}
.material-card ul {
  width: 100%;
  max-height: 85%;
  margin: 8px 0 0 0;
  padding: 0;
  margin-top: 8px;
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  overflow: scroll; /*border: solid 1px red;*/
}
.material-card li {
  width: 90px;
  height: 55px;
  margin: 8px;
  box-sizing: border-box;
  list-style: none;
  line-height: 51px;
  box-shadow: 4px 4px 8px #cbced1, -4px -4px 8px #ffffff;
  border-radius: 10px;
  color: rgb(124, 124, 124);
  font-weight: 600;
}
.material-card li.on {
  box-shadow: inset 6px 6px 6px #cbced1, inset -6px -6px 6px #ffffff;
  color: black;
}

.hello-container {
  width: 100px;
  height: 100px;
  mask-image: url("../assets/ingredients/salt.svg");
  background-color: gray;
  position: relative;
}
.hello-container:hover {
  background-color: red;
}
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
