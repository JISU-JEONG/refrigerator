<template>
  <div class="container">
    <RecipeRecommendationMaterial />
    <div class="row">
      <div
        v-for="material in Object.keys(materials)"
        :class="material"
        :key="material"
        @click="click(material, materials[material])"
      >
        <div class="container-icon" :style="test(materials[material])"></div>
        <div class="container-title">{{ material }}</div>
      </div>
    </div>
  </div>
</template>

<script>
import RecipeRecommendationMaterial from "../components/RecipeRecommendationMaterial";

export default {
  name: "RecipeRecommendationIcon",
  components: {
    RecipeRecommendationMaterial
  },
  data: () => ({
    materials: {
      소금: "salt",
      밀가루: "flour",
      올리고당: "syrup",
      식용유: "water",
      버터: "butter",
      식초: "soy",
      케찹: "ketchup",
      레몬소스: "lemon",
      마요네즈: "mayonnaise",
      부침가루: "flour",
      후추: "salt",
      참기름: "oil",
      고춧가루: "pepper",
      굴소스: "sauce",
      간장: "soy",
      카레가루: "flour",
      물엿: "syrup",
      물: "water",
      들기름: "oil",
      설탕: "salt"
    }
  }),
  methods: {
    test(material) {
      let img = require("../assets/ingredients/" + material + ".svg");
      return "mask-image: url(" + img + "); ";
    },
    click(material) {
      const red = document.querySelector("." + material + " .container-icon")
        .style.backgroundColor;

      document.querySelector(
        "." + material + " .container-icon"
      ).style.backgroundColor = red === "red" ? "gray" : "red";

      this.seasoning();
    },
    seasoning() {
      const seasoningData = document.querySelectorAll(".container-icon");
      let data = [];
      seasoningData.forEach((v, i) => {
        if (v.style.backgroundColor === "red") {
          if (data === undefined) {
            data = Object.keys(this.materials)[i];
          } else {
            data.push(Object.keys(this.materials)[i]);
          }
        }
      });

      console.log(data);
    }
  }
};
</script>

<style scoped lang="scss">
.container {
  padding: 30px 0 0 0;
}

.container-icon {
  width: 50px;
  height: 50px;
  margin: 20px;
  background-color: gray;
}

.container-icon-color {
  background-color: red;
}

.container-title {
  text-align: center;
}
</style>
