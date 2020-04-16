<template>
  <div>
    <h1>요리순서</h1>
    <div v-for="(recipeItem, i) in recipeSequence" :key="i">
      <v-card class="mx-auto" max-width="344" outline>
        <v-card-text v-for="(sequence, i) in recipeItem" :key="i">
          <p>{{ sequence }}</p>
          <v-divider></v-divider>
        </v-card-text>
      </v-card>
      <br />
    </div>
  </div>
</template>

<script>
export default {
  name: "RecipeSequence",
  props: {
    recipeSequence: {
      type: Object
    }
  }
};
</script>

<style></style>
