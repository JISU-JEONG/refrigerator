<template>
  <v-app>
    <navigation-bar />
    <v-content>
      <router-view></router-view>
    </v-content>

    <v-footer app></v-footer>
  </v-app>
</template>

<script>
import NavigationBar from "./components/NavigationBar";

export default {
  name: "App",
  components: {
    NavigationBar
  }
};
</script>
<style>

</style>
