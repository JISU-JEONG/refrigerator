<template>
  <div class="container">
    <RecipeRecommendationMaterial :materials="materials" />
    <RecipeRecommendationCondiments @condimentsData="getCondiments" />
    <v-btn
      class="search-recipe-button"
      color="light-green"
      @click="searchRecipe"
      >레시피 검색하기</v-btn
    >
  </div>
</template>

<script>
import http from "../services/http-common.js";
import RecipeRecommendationMaterial from "./RecipeRecommendationMaterial";
import RecipeRecommendationCondiments from "./RecipeRecommendationCondiments";

export default {
  name: "RecipeRecommendation",
  components: {
    RecipeRecommendationMaterial,
    RecipeRecommendationCondiments
  },

  data: () => ({
    condiments: []
  }),
  props: {
    materials: {
      type: Array
    }
  },
  methods: {
    getCondiments(data) {
      this.condiments = data;
      console.log(data);
    },
    searchRecipe() {
      const data = {
        // 상위 컴포넌트에서 가져온 것 (냉장고에서 찾은 재료)
        materials: this.materials,

        // 하위 컴포넌트에서 가져온 것 (사용자가 선택한 양념정보)
        condiments: this.components
      };
      http.post("/recipes/get_dishes/", data).then(res => {
        const payload = {
          // 찾은 레시피정보 vuex에 저장
          recipeInfoArr: res.data
        };
        this.$store.dispatch("recipeInfo", payload);
        this.$router.push("/RecipeList");
      });
    }
  }
};
</script>

<style scoped>
.container {
  margin-top: 50px;
  text-align: center;
}
.search-recipe-button {
  margin-top: 30px;
  font-family: "Cute Font", cursive;
}
</style>
