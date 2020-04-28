import Vue from "vue";
import Router from "vue-router";

import main from "../view/main";
import RecipeList from "../view/RecipeList";
import RecipeDetail from "../view/RecipeDetail";
import RecipeRecommendation from "../components/RecipeRecommendation";
import RecipeNotFound from "../components/RecipeNotFound";
import test from "../components/test";
Vue.use(Router);

export default new Router({
  mode: "history",
  routes: [
    {
      path: "/",
      name: "main",
      component: main
    },
    {
      path: "/RecipeList",
      name: "RecipeList",
      component: RecipeList
    },
    {
      path: "/RecipeRecommendation",
      name: "RecipeRecommendation",
      component: RecipeRecommendation
    },
    {
      path: "/RecipeDetail/:id",
      name: "RecipeDetail",
      component: RecipeDetail
    },
    {
      path: "/test",
      name: "test",
      component: test
    },
    {
      path: "/RecipeNotFound",
      name: "RecipeNotFound",
      component: RecipeNotFound
    }
  ]
});
