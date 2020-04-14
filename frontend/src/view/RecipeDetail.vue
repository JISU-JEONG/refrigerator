<template>
  <div class="recipe-detail-container">
    <RecipeCarousel :recipeCarousel="recipeCarousel" />
    <RecipeMeterial :recipeMeterial="recipeMeterial" />
    <RecipeSequence :recipeSequence="recipeSequence" />
  </div>
</template>
<script>
import RecipeCarousel from "../components/RecipeCarousel";
import RecipeMeterial from "../components/RecipeMeterial";
import RecipeSequence from "../components/RecipeSequence";

export default {
  name: "RecipeDetail",
  components: {
    RecipeCarousel,
    RecipeMeterial,
    RecipeSequence
  },
  data: () => ({
    recipeCarousel: null,
    recipeMeterial: null,
    recipeSequence: null
  }),
  methods: {
    get_food_data() {
      this.$axios
        .get(
          "/openapi/59bcdda005827dab577c5d693e6d162d49bd93d6c087f359d170465129ae5a5d/json/Grid_20150827000000000228_1/1/10"
        )
        .then(res => {
          this.recipeCarousel = [];

          this.recipeSequence = res.data.Grid_20150827000000000228_1.row.reduce(
            (obj, v) => {
              // 이미지
              if (v.COOKING_NO === 1 || v.COOKING_NO === 2) {
                this.recipeCarousel.push(v.STRE_STEP_IMAGE_URL);
              }

              // 요리순서
              if (obj[v.RECIPE_ID] === undefined) {
                obj[v.RECIPE_ID] = [v.COOKING_DC];
              } else {
                obj[v.RECIPE_ID].push(v.COOKING_DC);
              }
              return obj;
            },
            {}
          );
        });

      this.$axios
        .get(
          "/openapi/59bcdda005827dab577c5d693e6d162d49bd93d6c087f359d170465129ae5a5d/json/Grid_20150827000000000227_1/1/30"
        )
        .then(res => {
          this.recipeMeterial = res.data.Grid_20150827000000000227_1.row.reduce(
            (obj, v) => {
              // 요리재료
              if (obj[v.RECIPE_ID] === undefined) {
                obj[v.RECIPE_ID] = [v];
              } else {
                obj[v.RECIPE_ID].push(v);
              }
              return obj;
            },
            {}
          );
        });
    }
  },
  beforeMount() {
    console.log(this.$route.params.id);
    this.get_food_data();
  }
};
</script>

<style>
.recipe-detail-container {
  width: 100%;
  height: 100vh;
  padding-top: 80px;
}
</style>
