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
  props: {
    recipeInfoArr: {
      type: Array
    }
  },
  data: () => ({
    // recipeInfoArr: []
  }),
  methods: {
    getRecipeData() {
      http
        .get("/recipes/basicinfo/")
        .then(res => {
          for (let i = 1000; i < 1010; i++) {
            console.log(res.data[i]);
            this.recipeInfoArr.push(res.data[i]);
          }
        })
        .catch(err => {
          console.log(err);
        });
    }
  },
  // beforeMount() {
  //   this.getRecipeData();
  // },
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
