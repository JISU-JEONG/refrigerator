<template>
  <div>
    <h1>요리순서</h1>
    <div v-for="(recipe, i) in recipes_order" :key="i">
      <v-card class="mx-auto" max-width="344" outline>
        <v-card-text v-for="(order, i) in recipe" :key="i">
          <p>{{ order }}</p>
          <v-divider></v-divider>
        </v-card-text>
      </v-card>
      <br />
    </div>
  </div>
</template>

<script>
export default {
  name: "cooking_order",
  props: {
    recipes_order: {
      type: Object
    }
  }
};
</script>

<style></style>
