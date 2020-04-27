<template>
  <div>
    <main>
      <h2>냉장고에서 꺼낸 재료</h2>
      <v-row class="row">
        <v-col v-for="(material, i) in materials" :key="i" cols="4" class="col">
          <img class="container-icon" :src="getCondimentsPath(material, i)" />
        </v-col>
      </v-row>
    </main>
  </div>
</template>

<script>
export default {
  name: "RecipeRecommendationMaterial",
  props: {
    materials: {
      type: Array
    },
    percentages: {
      type: Array
    }
  },
  data: () => ({
    // materialItem: [
    // "감자", "고추", "사과", "스팸", "양파", "계란"
    // ]
    materialItem: {
      감자: "potato",
      고추: "chili",
      사과: "apple",
      스팸: "spam",
      양파: "onion",
      계란: "egg"
    }
  }),
  methods: {
    getCondimentsPath(material, i) {
      let img = null;
      if (this.percentages[i] > 90) {
        img = require("../assets/ingredients/" +
          this.materialItem[material] +
          "_color.svg");
      } else {
        img = require("../assets/ingredients/" +
          this.materialItem[material] +
          ".svg");
      }
      return img;
    }
  },
  beforeMounted() {
    this.percentages.push(0);
    this.materials.push("계란");
  }
};
</script>

<style scoped>
main {
  text-align: center;
  background-color: white;
  padding: 0 1.3em;
  margin: 1em auto;
  max-width: 85%;
}

h2 {
  font-family: "Cute Font", cursive;
  font-size: 2.5em;
  border-bottom: 5px double #dceda2;
  margin-bottom: 0.5em;
}

.row .col {
  font-family: "Cute Font", cursive;
  font-weight: bold;
}

.material {
  font-family: "Cute Font", cursive;
  font-size: 1.4em;
  font-weight: bold;
  letter-spacing: 1px;
}

.container-icon {
  width: 50px;
  height: 50px;
  margin: 10px;
}
</style>
