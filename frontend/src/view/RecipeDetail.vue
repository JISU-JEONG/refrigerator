<template>
  <div class="recipe-detail-container">
    <div
      :style="{ backgroundImage: `url(${imagePath})` }"
      class="thumbnail"
    ></div>
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
    recipeSequence: null,
    imagePath: null
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
      http.get(`/recipes/basicinfo/${this.$route.params.id}`).then(res => {
        this.imagePath = res.data[0].basic_imgurl;
      });
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
  height: 100vh;
  padding: 70px 0 0 0;
}
.thumbnail {
  width: 100%;
  height: 50%;
}
</style>
