<template>
  <div class="container">
    <RecipeRecommendationMaterial :materials="materials"/>
    <RecipeRecommendationIcon />
    <br />
    <v-btn class="btn" color="light-green">레시피 검색하기</v-btn>
  </div>
</template>

<script>
import RecipeRecommendationMaterial from "./RecipeRecommendationMaterial";
import RecipeRecommendationIcon from "./RecipeRecommendationIcon";

export default {
  name: "RecipeRecommendation",
  components: {
    RecipeRecommendationMaterial,
    RecipeRecommendationIcon
  },
  data: () => ({}),
  props: {
    materials : {
      type: Array,
      required: true
    }
  },
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
