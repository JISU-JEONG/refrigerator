<template>
  <div>
    <main>
      <h2>집에있는 조미료를 선택해주세요</h2>
      <div class="row">
        <v-row
          v-for="condiment in Object.keys(condiments)"
          :key="condiment"
          :class="condiment"
          @click="seasoningSelection(condiment)"
        >
          <v-col cols="12">
            <div
              class="container-icon"
              :style="getCondimentsPath(condiments[condiment])"
            ></div>
            <div class="container-title">{{ condiment }}</div>
          </v-col>
        </v-row>
      </div>
    </main>
  </div>
</template>

<script>
export default {
  name: "RecipeRecommendationCondiments",
  data: () => ({
    condiments: {
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
    getCondimentsPath(condiment) {
      let img = require("../assets/ingredients/" + condiment + ".svg");
      return "mask-image: url(" + img + "); ";
    },
    seasoningSelection(condiment) {
      const yellowgreen = document.querySelector(
        "." + condiment + " .container-icon"
      ).style.backgroundColor;

      document.querySelector(
        "." + condiment + " .container-icon"
      ).style.backgroundColor =
        yellowgreen === "yellowgreen" ? "gray" : "yellowgreen";

      this.seasoning();
    },
    seasoning() {
      const seasoningData = document.querySelectorAll(".container-icon");
      let data = [];
      seasoningData.forEach((v, i) => {
        if (v.style.backgroundColor === "yellowgreen") {
          if (data === undefined) {
            data = Object.keys(this.condiments)[i];
          } else {
            data.push(Object.keys(this.condiments)[i]);
          }
        }
      });
      this.$emit("condimentsData", data);
    }
  }
};
</script>

<style scoped>
.container-icon {
  width: 50px;
  height: 50px;
  margin: 10px;
  background-color: gray;
}

.container-icon-color {
  background-color: yellowgreen;
}

.container-title {
  font-family: "Cute Font", cursive;
  text-align: center;
}

h2 {
  display: flex;
  justify-content: center;
  font-family: "Cute Font", cursive;
  font-size: 2em;
  margin-bottom: 0.5em;
}

main {
  background-color: white;
  padding: 0 1.3em;
  margin: 1em auto;
  max-width: 90%;
}
</style>
