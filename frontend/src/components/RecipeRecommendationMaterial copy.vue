<template>
  <div>
    <main>
      <h2>냉장고에서 꺼낸 재료</h2>
      <v-row class="row">
        <v-col v-for="(material, i) in materials" :key="i" cols="4" class="col">
          <v-img class="image" :src="getMaterialsPath(material, i)">
            <div class="forward"></div>
          </v-img>
          <!-- <img class="material-icon" :src="getMaterialsPath(material, i)" /> -->
          <div
            class="container-title"
            :style="getMaterialStyle(material, i)"
          >{{material}} ({{percentages[i]}}%)</div>
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
      계란: "egg5"
    }
  }),
  methods: {
    getMaterialsPath(material, i) {
      console.log(this.materialItem[material]);
      let img = null;
      img = require("../assets/ingredients/" +
        this.materialItem[material] +
        ".svg");
      return img;
    },
    getMaterialsColorPath(material, i) {
      let img = null;
      img = require("../assets/ingredients/" +
        this.materialItem[material] +
        "_color.svg");

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
    },
    test(material, i) {
      let height = 50 * (this.percentages[i] / 100) + 10;
      console.log(height);
      return (
        "position: relative; overflow: hidden; max-height: " + height + "px"
      );
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

.image {
  width: 50px;
  height: 50px;
  margin: 10px;
}

.forward {
  height: 40px;
  background: #ffffff33;
  animation-duration: 1s;
  animation-name: slideToBottom;
}

@keyframes slideToBottom {
  from {
    height: 0px;
  }

  to {
    height: 50px;
  }
}
</style>
