<template>
  <div>
    <main>
      <v-row class="row">
        <v-col v-for="(material, i) in materials" :key="i" cols="4" class="col">
          <img class="material-icon" :src="getMaterialsPath(material, i)" />

          <div class="container-title" :style="getMaterialStyle(material, i)">
            {{ material }}<br />({{ percentages[i] }}%)
          </div>
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
    getMaterialsPath(material, i) {
      let img = null;
      if (this.percentages[i] > 80) {
        img = require("../assets/ingredients/" +
          this.materialItem[material] +
          "_color.svg");
      } else {
        img = require("../assets/ingredients/" +
          this.materialItem[material] +
          ".svg");
      }
      return img;
    },

    getMaterialStyle(material, i) {
      let style = null;
      let img = null;
      if (this.percentages[i] > 90) {
        img = require("../assets/ingredients/" +
          this.materialItem[material] +
          ".svg");
        style = "font-weight: bold; color:red";
      } else {
        style = "color: gray";
      }

      return style;
    }
  }
};
</script>

<style scoped>
main {
  text-align: center;
  background-color: white;
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
.material-icon {
  width: 50px;
  height: 50px;
  margin: 10px;
}
</style>
