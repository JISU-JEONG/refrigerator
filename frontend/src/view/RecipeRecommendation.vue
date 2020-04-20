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
      <div class="material">
        <div class="card">
          <h1 class="heading">Select material </h1>
          <ul id="list" @click="clickMaterial">
            <li class="item" v-for="material in materials" :key="material">
              <span class="text">{{material}}</span>
              <div class="custom-checkbox">
                <input type="checkbox">
                <svg viewBox="0 0 35.6 35.6">
                  <circle class="background" cx="17.8" cy="17.8" r="17.8"></circle>
                  <circle class="stroke" cx="17.8" cy="17.8" r="14.37"></circle>
                  <polyline class="check" points="11.78 18.12 15.55 22.23 25.17 12.87"></polyline>
                </svg>
              </div>
            </li>
          </ul>
        </div>
      </div>
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

  .material-container { width: 100%; height: 60%; position: relative; border: 1px blue solid; }
  .material {
    width: 100%;
    height: 100%;
    .card {
      position: absolute;
      left: 50%; top: 50%;
      transform: translate(-50%, -50%);
      width: 100%;
      height: 100%;
      max-width: 400px;
      padding: 5%;
      border-radius: 20px 20px 0 0;
      background-color: #fff;
      box-shadow: 0px 5px 10px rgba(0,0,0,.2);
    }
    .heading {
      opacity: .6;
      margin: 0px auto 20px;
      font-size: 18px;
      text-align: center;
    }
    #list {
      display: flex;
      flex-wrap: wrap;
      justify-content: space-between;
      .item {
        display: flex;
        flex-direction: column-reverse;
        align-items: center;
        .text {
          opacity: 0.4;
          margin-top: 10px;
          font-size: 12px;
          font-weight: bold;
          transition: ease all .2s;
          -webkit-transition: ease all .2s;
        }
        &:hover {
          .text {
            opacity: 1;
          }
          .custom-checkbox {
            .check {
              stroke-dashoffset: 0;
            }
          }
        }
      }
    }
  }

  .custom-checkbox {
    position: relative;
    display: inline-block;
    width: 40px;
    height: 40px;
    .background {
      fill: #ccc;
      transition: ease all .6s;
      -webkit-transition: ease all .6s;
    }
    .stroke {
      fill:none;
      stroke:#fff;
      stroke-miterlimit:10;
      stroke-width:2px;
      stroke-dashoffset: 100;
      stroke-dasharray: 100;
      transition: ease all .6s;
      -webkit-transition: ease all .6s;
    }
    .check {
      fill:none;
      stroke:#fff;
      stroke-linecap:round;
      stroke-linejoin:round;
      stroke-width:2px;
      stroke-dashoffset: 22;
      stroke-dasharray: 22;
      transition: ease all .6s;
      -webkit-transition: ease all .6s;
    }
    input[type=checkbox]{
      position: absolute;
      width: 100%;
      height: 100%;
      left: 0; top: 0;
      margin: 0;
      opacity: 0;
      -appearance: none;
      -webkit-appearance: none;
      
      &:hover {
        cursor: pointer;
      }
      
      &:checked {
        &+svg {
          .background {
            fill: #6cbe45;
          }
          .stroke {
            stroke-dashoffset: 0;
          }
          .check {
            stroke-dashoffset: 0;
          }
        }
      }
    }
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
