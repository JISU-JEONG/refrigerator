<template>
  <div>
    <div class="vuex-example-container">
      <v-btn @click="VuexTestButtonClick()">Vuex Test</v-btn>
      {{ receivedVuexValue }}
    </div>
  </div>
</template>

<script>
export default {
  name: "VuexExample",
  data: () => ({}),
  computed: {
    receivedVuexValue() {
      return this.$store.state.name;
    }
  },
  methods: {
    VuexTestButtonClick() {
      const payload = {
        name: "abc"
      };
      this.$store.dispatch("VuexTest", payload);
    }
  }
};
</script>

<style scoped>
.vuex-example-container {
  width: 100%;
  height: 100vh;
  padding-top: 80px;
}
</style>
