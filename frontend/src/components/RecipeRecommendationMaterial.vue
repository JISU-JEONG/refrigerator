<template>
  <div class="container">
    <div class="row">
      <img class="container-icon" src="https://img.icons8.com/color/48/000000/steak.png" />
      <img class="container-icon" src="https://img.icons8.com/color/48/000000/bacon.png" />
      <img class="container-icon" src="https://img.icons8.com/officexs/48/000000/potato.png" />
      <img class="container-icon" src="https://img.icons8.com/emoji/48/000000/onion-emoji.png" />
    </div>
    <div class="row">
      <div class="container-title">소고기</div>
      <div class="container-title">돼지고기</div>
      <div class="container-title">감자</div>
      <div class="container-title">양파</div>
    </div>
  </div>
</template>

<script>
export default {
  name: "RecipeRecommendationMaterial",
  components: {},
  data: () => ({
    materials: ["소고기", "닭고기", "감자", "양파", "파", "마늘"]
  }),
  methods: {}
};
</script>

<style scoped lang="scss">
.container-title {
  margin: 25px;
  text-align: center;
}
.container-icon {
  margin: 20px;
}
</style>
