<template>
  <v-app>
    <NavigationBar />
    <v-content>
      <RouterView />
    </v-content>
    <Footer />
  </v-app>
</template>

<script>
import NavigationBar from "./components/NavigationBar";
import Footer from "./components/Footer";

export default {
  name: "App",
  components: {
    NavigationBar,
    Footer
  }
};
</script>
<style></style>
