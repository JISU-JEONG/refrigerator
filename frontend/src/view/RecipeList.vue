<template>
  <div class="recipe-list-container">
    <v-row no-gutters>
      <v-col v-for="recipeInfo in recipeInfoArr" :key="recipeInfo.id" cols="12">
        <RecipeCard :recipeInfo="recipeInfo" />
      </v-col>
    </v-row>
  </div>
</template>

<script>
import http from "../services/http-common";
import RecipeCard from "../components/RecipeCard";

export default {
  name: "RecipeList",
  components: {
    RecipeCard
  },
  computed: {
    recipeInfoArr() {
      return this.$store.state.data;
    }
  },
  mounted: () => {
    // document.querySelector('header').style.background = 'red'
    // document.querySelector('header').classList.remove('test-red')
    // document.querySelector('header').classList.add('test-black')
  }
};
</script>

<style scoped>
.recipe-list-container {
  width: 100%;
  height: 100vh;
  padding-top: 70px;
}
</style>
