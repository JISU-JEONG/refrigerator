<template>
  <div class="container">
    <RecipeList v-if="showListPage" :recipeInfoArr="recipeInfoArr" />
    <div v-else>
      <RecipeRecommendationMaterial :materials="materials" />
      <RecipeRecommendationIcon @icondata="parents" />
      <br />
      <v-btn class="btn" color="light-green" @click="searchRecipe"
        >레시피 검색하기</v-btn
      >
    </div>
  </div>
</template>

<script>
import RecipeRecommendationMaterial from "./RecipeRecommendationMaterial";
import RecipeRecommendationIcon from "./RecipeRecommendationIcon";
import RecipeList from "../view/RecipeList";
import http from "../services/http-common.js";

export default {
  name: "RecipeRecommendation",
  components: {
    RecipeRecommendationMaterial,
    RecipeRecommendationIcon,
    RecipeList
  },
  data: () => ({
    condiments: [],
    recipeInfoArr: [],
    showListPage: false
  }),
  props: {
    materials: {
      type: Array
    }
  },
  methods: {
    parents(name) {
      this.components = name;
      console.log(name);
    },
    searchRecipe() {
      const data = {
        materials: this.materials,
        condiments: this.components
        // condiments: ["설탕", "소금", "후추", "참기름"]
      };
      http.post("/recipes/get_dishes/", data).then(res => {
        this.recipeInfoArr = res.data;
        this.showListPage = !this.showListPage;
        console.log(res);
      });
    },
    onMultiLabel() {
      this.loading = !this.loading;
      http.post("/recipes/image_upload/", this.uploadedImage).then(res => {
        this.loading = !this.loading;
        this.materials = res.data.materials;
        this.showMaterialPage = !this.showMaterialPage;
        this.removeTransparentClass();
        console.log(res.data.materials);
      });
    }
  }
};
</script>

<style scoped lang="scss">
.container {
  margin-top: 50px;
  text-align: center;
}
.btn {
  font-family: "Cute Font", cursive;
}
</style>
