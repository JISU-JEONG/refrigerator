import Vue from "vue";
import Router from "vue-router";

import main from "../view/main";
import RecipeList from "../view/RecipeList";
import VuexExample from "../view/VuexExample";
import RecipeDetail from "../view/RecipeDetail";
import RecipeRecommendationIcon from "../components/RecipeRecommendation";
import Loading from "../components/Loading";

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
      component: RecipeRecommendationIcon
    },
    {
      path: "/RecipeDetail/:id",
      name: "RecipeDetail",
      component: RecipeDetail
    },
    {
      path: "/VuexExample",
      name: "VuexExample",
      component: VuexExample
    },
    {
      path: "/test",
      name: "test",
      component: Loading
    }
  ]
});
