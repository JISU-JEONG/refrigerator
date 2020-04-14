<template>
  <div>
    <h1>요리재료</h1>
    <div v-for="(recipeItem, i) in recipeMeterial" :key="i">
      <v-card class="mx-auto" max-width="344" outline>
        <v-card-text v-for="(meterial, i) in recipeItem" :key="i">
          <p>{{ meterial }}</p>
          <v-divider></v-divider>
        </v-card-text>
      </v-card>
      <br />
    </div>
  </div>
</template>

<script>
export default {
  name: "RecipeMeterial",
  props: {
    recipeMeterial: {
      type: Object
    }
  }
};
</script>

<style></style>
