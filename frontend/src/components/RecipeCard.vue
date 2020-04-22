<template>
  <div class="recipe-container" @click="recipeDetail($event, recipeInfo)">
    <div
      class="recipe-card"
      :style="{ backgroundImage: `url(${recipeInfo.basic_imgurl})` }"
    ></div>
    <v-container class="recipe-info">
      <p class="recipe-name">
        {{ recipeInfo.basic_name }}
        <span class="recipe-detail">{{ recipeInfo.basic_kcal }}</span>
      </p>
      <p class="recipe-detail">{{ recipeInfo.basic_intro }}</p>
    </v-container>
  </div>
</template>

<script>
export default {
  name: "RecipeCard",
  data: () => ({}),
  props: {
    recipeInfo: {
      type: Object,
      required: true
    }
  },
  methods: {
    recipeDetail(event, recipeInfo) {
      this.$router.push({
        name: "RecipeDetail",
        params: { id: recipeInfo.basic_code }
      });
    }
  }
};
</script>

<style scoped>
.recipe-container {
  width: 100%;
  position: relative;
  padding-bottom: 100%;
  overflow: hidden;
}
.recipe-container:hover .recipe-card {
  transform: scale(1.05);
}
.recipe-card {
  width: 100%;
  height: 100%;
  position: absolute;
  background-repeat: no-repeat;
  background-size: cover;
  transition: transform 0.2s linear;
}
.recipe-info {
  width: 100%;
  height: 100%;
  position: absolute;
  font-weight: 600;
  font-size: 32px;
  color: white;
  background: linear-gradient(rgba(0, 0, 0, 0.4), rgba(255, 255, 255, 0));
  cursor: pointer;
}
.recipe-detail {
  font-size: 16px;
  font-weight: 500;
}
</style>
