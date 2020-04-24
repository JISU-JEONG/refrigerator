<template>
  <div class="container">
    <RecipeRecommendationMaterial />
    <RecipeRecommendationIcon />
    <br />
    <v-btn class="btn" color="light-green">레시피 검색하기</v-btn>
  </div>
</template>

<script>
import RecipeRecommendationMaterial from "../components/RecipeRecommendationMaterial";
import RecipeRecommendationIcon from "../components/RecipeRecommendationIcon";

export default {
  name: "RecipeRecommendation",
  components: {
    RecipeRecommendationMaterial,
    RecipeRecommendationIcon
  },
  data: () => ({})
};
</script>

<style scoped lang="scss">
.container {
  margin-top: 40px;
  justify-content: center;
  text-align: center;
}
.btn {
  font-family: "Cute Font", cursive;
}
</style>
