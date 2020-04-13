<template>
  <div class="food-container" @click="DetailFood($event, foodInfo)">
    <div
      class="food-card"
      :style="{ backgroundImage: `url(${foodInfo.IMG_URL})` }"
    ></div>
    <v-container class="food-info">
      <p class="food-name">
        {{ foodInfo.RECIPE_NM_KO }}
        <span class="food-detail">{{ foodInfo.CALORIE }}</span>
      </p>
      <p class="food-detail">{{ foodInfo.SUMRY }}</p>
    </v-container>
  </div>
</template>

<script>
export default {
  name: "FoodCard",
  data: () => ({}),
  props: {
    foodInfo: {
      type: Object,
      required: true
    }
  },
  methods: {
    DetailFood(event, foodInfo) {
      this.$router.push({
        name: "fooddetail",
        params: { id: foodInfo.id }
      });
      console.log(event, foodInfo);
    }
  }
};
</script>

<style scoped>
.food-container {
  width: 100%;
  position: relative;
  padding-bottom: 100%;
  overflow: hidden;
}
.food-container:hover .food-card {
  transform: scale(1.05);
}
.food-card {
  width: 100%;
  height: 100%;
  position: absolute;
  background-repeat: no-repeat;
  background-size: cover;
  transition: transform 0.2s linear;
}
.food-info {
  width: 100%;
  height: 100%;
  position: absolute;
  font-weight: 600;
  font-size: 32px;
  color: white;
  background: linear-gradient(rgba(0, 0, 0, 0.4), rgba(255, 255, 255, 0));
  cursor: pointer;
}
.food-detail {
  font-size: 16px;
  font-weight: 500;
}
</style>
