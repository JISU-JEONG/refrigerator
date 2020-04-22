<template>
  <div class="recipe-detail-container">
    <img :src="getImgPath()" />
    <RecipeMeterial :recipeMeterial="recipeMeterial" />
    <RecipeSequence :recipeSequence="recipeSequence" />
  </div>
</template>
<script>
import http from "../services/http-common.js";
import RecipeMeterial from "../components/RecipeMeterial";
import RecipeSequence from "../components/RecipeSequence";

export default {
  name: "RecipeDetail",
  components: {
    RecipeMeterial,
    RecipeSequence
  },
  data: () => ({
    recipeMeterial: null,
    recipeSequence: null
  }),
  methods: {
    getRecipeSequence() {
      http.get(`/recipes/processinfo/${this.$route.params.id}`).then(res => {
        this.recipeSequence = res.data;
      });
    },

    getRecipeMeterial() {
      http.get(`/recipes/materialinfo/${this.$route.params.id}`).then(res => {
        this.recipeMeterial = res.data;
      });
    },
    getImgPath() {
      return this.$route.params.id;
    }
  },
  beforeMount() {
    console.log(this.$route.params.id);
    this.getRecipeSequence();
    this.getRecipeMeterial();
    this.getImgPath();
  }
};
</script>

<style>
.recipe-detail-container {
  width: 100%;
  max-width: 960px;
  height: 100vh;
  padding: 70px 0 0 0;
  margin: 0 auto;
}
</style>
