<template>
  <div>
    <div class="banner"></div>
    <RecipeCategory />
    <!-- <input type="file" /> -->
  </div>
</template>
<script>
import RecipeCategory from "../components/RecipeCategory";
export default {
  name: "Main",
  components: {
    RecipeCategory
  },
  data: () => ({}),
  methods: {
    addTransparentClass() {
      const navClassList = document.querySelector("header").classList;
      navClassList.add("header-transparent");
    },
    removeTransparentClass() {
      const navClassList = document.querySelector("header").classList;
      if (navClassList.contains("header-transparent")) {
        navClassList.remove("header-transparent");
      }
    },
    onScroll() {
      if (window.scrollY > 300) {
        this.removeTransparentClass();
      } else {
        this.addTransparentClass();
      }
    }
  },
  mounted() {
    this.addTransparentClass();
    window.addEventListener("scroll", this.onScroll);
  },
  beforeDestroy() {
    this.removeTransparentClass();
    window.removeEventListener("scroll", this.onScroll);
  }
};
</script>
<style scoped>
.banner {
  width: 100%;
  height: 500px;
  /* background-image: url('https://images.food52.com/ABp9BlnO_4sKOVA1asXsC7G_tCs=/1008x672/filters:format(webp)/333bee7e-8eb7-4282-8769-c83fc408abd3--pjimage_1-.jpg'); */
  background: rgb(77, 71, 71);
}
</style>
