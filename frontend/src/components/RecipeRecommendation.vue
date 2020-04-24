<template>
  <div class="container">
    <RecipeRecommendationMaterial :materials="materials" />
    <RecipeRecommendationIcon @icondata="parents" />
    <br />
    <v-btn class="btn" color="light-green" @click="click"
      >레시피 검색하기</v-btn
    >
  </div>
</template>

<script>
import RecipeRecommendationMaterial from "./RecipeRecommendationMaterial";
import RecipeRecommendationIcon from "./RecipeRecommendationIcon";
import http from "../services/http-common.js";

export default {
  name: "RecipeRecommendation",
  components: {
    RecipeRecommendationMaterial,
    RecipeRecommendationIcon
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
    parents(name) {
      this.components = name;
      console.log(name);
    },
    click() {
      const data = {
        materials: this.materials,
        condiments: this.components
        // condiments: ["설탕", "소금", "후추", "참기름"]
      };
      http.post("/recipes/get_dishes/", data).then(res => {
        console.log(res);
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
