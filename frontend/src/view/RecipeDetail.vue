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
    getRecipeImage(v) {
      if (v.STRE_STEP_IMAGE_URL !== "") {
        this.recipeCarousel.push(v.STRE_STEP_IMAGE_URL);
      }
    },

    getTestApi() {
      this.$axios.get("http://localhost:8080/hello").then(res => {
        console.log(res);
      });
    },
    getRecipeData() {
      this.$axios
        .get(
          "/openapi/59bcdda005827dab577c5d693e6d162d49bd93d6c087f359d170465129ae5a5d/json/Grid_20150827000000000228_1/1/5"
        )
        .then(res => {
          this.recipeCarousel = [];

          this.recipeSequence = res.data.Grid_20150827000000000228_1.row.reduce(
            (arr, v) => {
              this.getRecipeImage(v);
              arr.push(v);
              return arr;
            },
            []
          );
          console.log(this.recipeSequence);
        });
    },

    getRecipeMeterial() {
      this.$axios
        .get(
          "/openapi/59bcdda005827dab577c5d693e6d162d49bd93d6c087f359d170465129ae5a5d/json/Grid_20150827000000000227_1/1/24"
        )
        .then(res => {
          this.recipeMeterial = res.data.Grid_20150827000000000227_1.row.reduce(
            (arr, v) => {
              // if (obj[v.RECIPE_ID] === undefined) {
              //   obj[v.RECIPE_ID] = [v];
              // } else {
              //   obj[v.RECIPE_ID].push(v);
              // }
              arr.push(v);
              return arr;
            },
            []
          );
        });
    }
  },
  beforeMount() {
    console.log(this.$route.params.id);
    this.getRecipeData();
    this.getRecipeMeterial();
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
