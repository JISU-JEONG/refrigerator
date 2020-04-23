<template>
  <div class="container">
    <div class="row">
      <div
        v-for="material in Object.keys(materials)"
        :class="material"
        :key="material"
        @click="click(material)"
      >
        <div class="container-icon" :style="test(material)"></div>
        <div class="container-title">{{ materials[material] }}</div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "RecipeRecommendationIcon",
  components: {},
  data: () => ({
    materials: {
      flour: "밀가루",
      ketchup: "케찹",
      lemon: "레몬소스",
      mayonnaise: "마요네즈",
      oil: "참기름/들기름",
      pepper: "고춧가루",
      salt: "소금/후추/설탕",
      sauce: "굴소스",
      soy: "간장",
      syrup: "물엿/올리고당",
      water: "물/식용유"
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
            data = Object.values(this.materials)[i];
          } else {
            data.push(Object.values(this.materials)[i]);
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
  width: 100%;
  height: 100vh;
  margin: 0;
  padding: 70px 0 0 0;
  background: #f1f1f1;
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
