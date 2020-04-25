<template>
  <RecipeRecommendation v-if="showMaterialPage" :materials="materials" />
  <div class="main-container" v-else>
    <div class="possible">
      <span>현재 판별가능한 재료 목록</span>
      <div class="possibleList">
        정지수, 정영훈, 정지수, 김기은, 김태우
      </div>
    </div>
    <Loading v-if="loading" />
    <div class="wrapper">
      <div class="logo" :class="{ rotate: rotate }">
        <label class="white-round front" for="ex_file">
          <v-icon class="center" style="font-size:140px">mdi-camera</v-icon>
        </label>
        <div class="white-round back">
          <div class="center">
            <v-icon style="font-size:140px">mdi-image-area</v-icon>
            <p>사진촬영 완료 <br />하단 버튼을 눌러 재료를 탐색하세요</p>
          </div>
        </div>
        <input type="file" @change="onFileChange" id="ex_file" />
      </div>
      <div class="intro">
        <div class="intro-button" @click="onMultiLabel" v-if="rotate">
          <span> Multi-<br />label</span>
        </div>
        <div class="intro-button" @click="onClick" v-if="rotate">
          <span>Mask <br />R-CNN</span>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import Loading from "../components/Loading";
import RecipeRecommendation from "../components/RecipeRecommendation";
import http from "../services/http-common.js";

export default {
  name: "Main",
  components: {
    Loading,
    RecipeRecommendation
  },
  data() {
    return {
      materials: [],
      uploadedImage: new FormData(),
      loading: false,
      showMaterialPage: false,
      rotate: false
    };
  },
  methods: {
    onClick() {
      (this.rotate = !this.rotate), (this.uploadedImage = new FormData());
    },
    onFileChange(e) {
      var files = e.target.files || e.dataTransfer.files;
      if (!files.length) return;
      this.uploadedImage.append("file", files[0]);
      this.rotate = !this.rotate;
    },
    onMultiLabel() {
      this.loading = !this.loading;
      http
        .post("/recipes/image_upload/", this.uploadedImage)
        .then(res => {
          this.loading = !this.loading;
          this.materials = res.data.materials;
          this.showMaterialPage = !this.showMaterialPage;
          this.removeTransparentClass();
          console.log(res.data.materials);
        })
        .catch(e => {
          alert(e);
          this.loading = false;
          (this.rotate = !this.rotate), (this.uploadedImage = new FormData());
        });
    },
    addTransparentClass() {
      const navClassList = document.querySelector("header").classList;
      navClassList.add("header-transparent");
    },
    removeTransparentClass() {
      const navClassList = document.querySelector("header").classList;
      if (navClassList.contains("header-transparent")) {
        navClassList.remove("header-transparent");
      }
    }
    // onScroll() {
    //   if (window.scrollY > 300) {
    //     this.removeTransparentClass();
    //   } else {
    //     this.addTransparentClass();
    //   }
    // }
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
  background-image: url("https://i.pinimg.com/564x/b9/26/90/b92690a0d83b7c15a7d00b5f97a1a170.jpg");
  background-size: cover;
  background-position: center;
  padding-top: 70px;
  position: relative;
  display: flex;
  justify-content: center;
  align-items: center;
}
.main-container::before {
  content: " ";
  width: 100%;
  height: 100%;
  position: absolute;
  top: 0;
  left: 0;
  background: -moz-radial-gradient(
    center,
    ellipse cover,
    rgba(0, 0, 0, 0) 0%,
    rgba(0, 0, 0, 0.4) 100%
  );
  background: -webkit-radial-gradient(
    center,
    ellipse cover,
    rgba(0, 0, 0, 0) 0%,
    rgba(0, 0, 0, 0.4) 100%
  );
  background: radial-gradient(
    ellipse at center,
    rgba(0, 0, 0, 0) 0%,
    rgba(0, 0, 0, 0.4) 100%
  );
  filter: progid:DXImageTransform.Microsoft.gradient( startColorstr='#00000000', endColorstr='#66000000',GradientType=1 );
}
.possible {
  position: absolute;
  left: 20px;
  bottom: 20px;
  color: white;
  text-decoration: underline;
}
.possibleList {
  width: 200px;
  height: 70px;
  padding: 10px;
  position: absolute;
  top: -70px;
  display: none;
  background-color: rgba(255, 255, 255, 0.75);
  border-radius: 5px;
  color: #555;
  font-weight: 700;
}
.possible:hover .possibleList {
  display: block;
}
.wrapper {
  width: 70%;
  height: 80%;
  perspective: 1000px;
  /* border: 1px blue solid; */
}
.logo {
  width: 100%;
  padding-bottom: 100%;
  position: relative;
  /* border: 1px solid red; */

  transition: 1s;
  transform-style: preserve-3d;
}
.rotate {
  transform: rotateY(-180deg);
}
.white-round {
  position: absolute;
  display: inline-block;
  width: 100%;
  height: 100%;
  background-color: rgba(255, 255, 255, 0.7);
  border-radius: 50%;
  box-shadow: 2px 4px 8px gray;
  backface-visibility: hidden;
}
.white-round p {
  margin-top: -10px;
  text-align: center;
  font-size: 16px;
  font-weight: 700;
}
.front {
  z-index: 1;
  cursor: pointer;
}
.back {
  transform: rotateY(180deg);
}
.logo input {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  border: 0;
}
.center {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  color: rgba(0, 0, 0, 0.815);
  text-align: center;
}
.intro {
  width: 100%;
  height: 30%;
  margin-top: 72px;
  font-size: 20px;
  font-weight: 700;
  color: rgba(0, 0, 0, 0.9);
  /* border: 1px solid red; */
  display: flex;
  justify-content: space-around;
  flex-wrap: wrap;
}
.intro-button {
  width: 110px;
  height: 110px;
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: rgba(255, 255, 255, 0.7);
  border-radius: 10px;
  box-shadow: 2px 4px 8px gray;
}
</style>
