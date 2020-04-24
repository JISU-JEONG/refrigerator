<template>
  <div class="container">{{material}}</div>
</template>

<script>
export default {
  name: "RecipeRecommendationMaterial",
  components: {},
  data: () => ({
    material: [
      "계란",
      "전분",
      "부침가루",
      "밀가루",
      "배추",
      "호박",
      "대파",
      "다짐육",
      "콩",
      "마늘"
    ]
  }),
  methods: {}
};
</script>

<style scoped>
.container {
  margin-top: 40px;
}
</style>
