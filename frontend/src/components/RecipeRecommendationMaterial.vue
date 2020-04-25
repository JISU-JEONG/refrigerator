<template>
  <div>
    <main>
      <h2>냉장고에서 꺼낸 재료</h2>
      <v-row class="row">
        <v-col
          v-for="material in materials"
          :key="material"
          cols="4"
          class="col"
        >
          {{ material }}
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
    }
  },
  data: () => ({
    // materialItem: [
    //   "계란",
    //   "전분",
    //   "부침가루",
    //   "밀가루",
    //   "배추",
    //   "호박",
    //   "대파",
    //   "다짐육",
    //   "콩",
    //   "마늘"
    // ]
  })
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
</style>
