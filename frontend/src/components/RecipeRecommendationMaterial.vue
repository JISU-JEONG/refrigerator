<template>
  <div class="container">
    <div class="blackboard">
      <ul class="paper">
        <li>소고기</li>
      </ul>
      <ul class="paper">
        <li>감자</li>
      </ul>
      <ul class="paper">
        <li>양파</li>
      </ul>
      <ul class="paper">
        <li>계란</li>
      </ul>
      <ul class="paper">
        <li>당근</li>
      </ul>
      <ul class="paper">
        <li>바나나</li>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  name: "RecipeRecommendationMaterial",
  components: {},
  data: () => ({}),
  methods: {}
};
</script>

<style scoped>
.blackboard {
  position: relative;
  margin: 3% auto;
  width: 90%;
  overflow: hidden;
  background-image: url("https://res.cloudinary.com/dovbrtmkv/image/upload/v1494873393/cork_mlmb4o.jpg");
  background-size: 650px;
  border: 20px solid #805500;
}

ul.paper li {
  position: relative;
  width: 70px;
  font-size: 11px;
  padding: 30px;
  list-style-type: none;
  background: #ffff66;
  overflow-wrap: break-word;
  overflow: hidden;
  -webkit-hyphens: auto;
  -ms-hyphens: auto;
  hyphens: auto;
  margin: 10px;
  padding: 30px 20px;
  float: left;
  -webkit-box-shadow: 0 0 4px rgba(0, 0, 0, 0.2),
    inset 0 0 50px rgba(0, 0, 0, 0.1);
  box-shadow: 0 0 5px rgba(0, 0, 0, 0.2), inset 0 0 50px rgba(0, 0, 0, 0.1);
  border-radius: 60px 60px 120px 120px / 4px 4px 8px 8px;
}
</style>