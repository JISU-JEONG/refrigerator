<template>
  <div class="main-container">
    <div class="wrapper">
      <div class="logo" >
        <label for="ex_file">
          <v-icon>mdi-camera</v-icon>
        </label>
        <input type="file" @change="onFileChange" id="ex_file"/>
      </div>
      <div class="intro">
        <p>이곳에는 이런 저런 설명이 들어 갈거고 위에 카메라 버튼을 누르면 바로 사진을 찍을 겁니다.</p>
      </div>
      
      
    </div>
    <!-- <RecipeCategory /> -->
    <!-- <input type="file" /> -->
  </div>
</template>
<script>
// import RecipeCategory from "../components/RecipeCategory";
export default {
  name: "Main",
  components: {
    // RecipeCategory
  },
  data() {
    return {
      uploadedImage: new FormData(),    
    }
  },
  methods: {
    onFileChange(e) {
      var files = e.target.files || e.dataTransfer.files;
      if (!files.length) return;
      this.uploadedImage.append('image', files[0])
      console.log(this.uploadedImage.get('image'))
    },
    addTransparentClass() { // nav 조작하던거. 이제 빼도 될 듯?
      const navClassList = document.querySelector("header").classList;
      navClassList.add("header-transparent");
    },
    removeTransparentClass() { // nav 조작하던거. 이제 빼도 될 듯?
      const navClassList = document.querySelector("header").classList;
      if (navClassList.contains("header-transparent")) {
        navClassList.remove("header-transparent");
      }
    },
    onScroll() { // nav 조작하던거. 이제 빼도 될 듯?
      if (window.scrollY > 300) {
        this.removeTransparentClass();
      } else {
        this.addTransparentClass();
      }
    }
  },
  mounted() {
    this.addTransparentClass();
    window.addEventListener("scroll", this.onScroll);
  },
  beforeDestroy() {
    this.removeTransparentClass();
    window.removeEventListener("scroll", this.onScroll);
  }
};
</script>
<style scoped>
  * {
    box-sizing: border-box;
  }
  .main-container {
    width: 100%;
    height: 100%;
    background-color: #f1f1f1;
    padding-top:70px;
    display: flex;
    justify-content: center;
    align-items: center;
    border: 1px solid black;
  }
  .wrapper {
    width: 70%;
    height: 80%;
    /* border: 1px blue solid; */
  }
  .logo {
    width:100%;
    padding-bottom:100%;
    position:relative;
    /* border: 1px solid red; */
   }
  .logo label { position: absolute; display: inline-block; width:100%; height: 100%; background-color: cadetblue; border-radius: 50%; cursor: pointer; box-shadow: 0px 0px 2px #5f5f5f, 0px 0px 0px 5px #ecf0f3, 8px 8px 15px #a7aaaf, -8px -8px 15px #ffffff; }
  .logo input { position: absolute; width: 1px; height: 1px; padding: 0; margin: -1px; overflow: hidden; clip:rect(0,0,0,0); border: 0; }
  .logo i {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    font-size: 150px;
    color: white;
  }
  .intro {
    width: 100%;
    margin-top: 24px;
    font-size: 20px;
    font-weight: 700;
    border: 1px solid black;
  }
</style>
