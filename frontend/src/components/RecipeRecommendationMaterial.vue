<template>
  <div>
    <main>
      <h2>냉장고에서 꺼낸 재료</h2>
      <ul v-for="material in materials" :key="material" class="row">
        <li class="col">
          {{ material }}
        </li>
      </ul>

      <!-- <ul v-for="(materials, i) in materialItem" :key="i" class="row">
        <li class="col" v-for="(material, i) in materials" :key="i">
          {{ material }}
        </li>
      </ul> -->
    </main>
  </div>
</template>

<script>
export default {
  name: "RecipeRecommendationMaterial",
  components: {},
  props: {
    materials: {
      type: Array
    }
  },
  data: () => ({
    materialItem: [
      ["계란", "전분", "부침가루"],
      ["밀가루", "배추", "호박"],
      ["대파", "다짐육", "콩"],
      ["마늘"]
    ]
  }),
  methods: {}
};
</script>

<style scoped>
h2 {
  font-family: "Cute Font", cursive;
  font-size: 2.5em;
  border-bottom: 5px double #dceda2;
  margin-bottom: 0.5em;
}

ul li {
  font-family: "Cute Font", cursive;
  list-style-type: none;
  margin-left: -1.3em;
  font-weight: bold;
}

li {
  font-family: "Handlee", cursive;
  font-size: 1.2em;
  line-height: 2em;
  letter-spacing: 1px;
}

.material {
  font-family: "Cute Font", cursive;
  font-size: 1.4em;
  font-weight: bold;
  letter-spacing: 1px;
}

main {
  text-align: center;
  background-color: white;
  padding: 0 1.3em;
  margin: 1em auto;
  max-width: 85%;
}
</style>
