<template>
  <v-app>
    <NavigationBar />
    <v-content>
      <RouterView />
    </v-content>
    <Footer app />
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
<style></style>
