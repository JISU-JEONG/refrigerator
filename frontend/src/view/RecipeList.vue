<template>
  <div class="recipe-list-container">
    <v-row no-gutters>
      <v-col
        v-for="recipeInfo in recipeInfoArr"
        :key="recipeInfo.id"
        cols="12"
      >
        <RecipeCard :recipeInfo="recipeInfo" />
      </v-col>
    </v-row>
  </div>
</template>

<script>
import http from "../services/http-common"
import RecipeCard from "../components/RecipeCard";

export default {
  name: "RecipeList",
  components: {
    RecipeCard
  },
  data: () => ({
    recipeInfoArr: [
      // {
      //   id: 1,
      //   RECIPE_NM_KO: "나물비빔밥",
      //   SUMRY: "육수로 지은 밥에 야채를 듬뿍 넣은 영양만점 나물비빔밥!",
      //   CALORIE: "580Kcal",
      //   IMG_URL: "http://file.okdab.com/UserFiles/searching/recipe/000200.jpg"
      // },
      // {
      //   id: 2,
      //   RECIPE_NM_KO: "오곡밥",
      //   SUMRY: "정월대보름에 먹던 오곡밥! 영양을 한그릇에 담았습니다.",
      //   CALORIE: "338Kcal",
      //   IMG_URL: "http://file.okdab.com/UserFiles/searching/recipe/000300.jpg"
      // },
      // {
      //   id: 3,
      //   RECIPE_NM_KO: "잡채밥",
      //   SUMRY:
      //     "잡채밥 한 그릇이면 오늘 저녁 끝! 입 맛 없을 때 먹으면 그만이지요~",
      //   CALORIE: "520Kcal",
      //   IMG_URL: "http://file.okdab.com/UserFiles/searching/recipe/000400.jpg"
      // },
      // {
      //   id: 4,
      //   RECIPE_NM_KO: "콩나물밥",
      //   SUMRY:
      //     "다이어트에 으뜸인 콩나물밥. 밥 물 넣을때 평소보다 적게 넣는거 잊지마세요!",
      //   CALORIE: "401Kcal",
      //   IMG_URL: "http://file.okdab.com/UserFiles/searching/recipe/000600.jpg"
      // },
      // {
      //   id: 5,
      //   RECIPE_NM_KO: "오므라이스",
      //   SUMRY:
      //     "각종 채소를 계란 속에 꼭꼭 숨겨 편식하는 아이들도 맛있게 먹어요~",
      //   CALORIE: "630Kcal",
      //   IMG_URL: "http://file.okdab.com/UserFiles/searching/recipe/001800.jpg"
      // },
      // {
      //   id: 6,
      //   RECIPE_NM_KO: "감자수제비",
      //   SUMRY: "쫀득쫀득한 수제비와 담백한 맛의 감자가 이뤄내는 하모니!",
      //   CALORIE: "410Kcal",
      //   IMG_URL: "http://file.okdab.com/UserFiles/searching/recipe/001900.jpg"
      // }
    ]
  }),
  methods: {
    getRecipeData() {
      http.get("/recipes/basicinfo/").then(res => {
        for (let i = 1000; i < 1010; i++) {
          console.log(res.data[i])
          this.recipeInfoArr.push(res.data[i]);
        }
      })
      .catch(err => {
        console.log(err)
      })
    }
  },
  beforeMount() {
    this.getRecipeData();
  },
  mounted: () => {
    // document.querySelector('header').style.background = 'red'
    // document.querySelector('header').classList.remove('test-red')
    // document.querySelector('header').classList.add('test-black')
  }
};
</script>

<style>
.recipe-list-container {
  width: 100%;
  height: 100vh;
  padding-top: 80px;
}
</style>
