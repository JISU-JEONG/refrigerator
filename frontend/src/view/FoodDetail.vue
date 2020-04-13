<template>
  <div>
    <slider_recipe :recipes_img="recipes_img" />
    <cooking_meterial :cooking_meterial="cooking_meterial" />
    <cooking_order :recipes_order="recipes_order" />
  </div>
</template>
<script>
import slider_recipe from "../components/slider_recipe";
import cooking_order from "../components/cooking_order";
import cooking_meterial from "../components/cooking_meterial";

export default {
  name: "FoodDetail",
  components: {
    slider_recipe,
    cooking_order,
    cooking_meterial
  },
  data: () => ({
    recipes_img: null,
    recipes_order: null,
    cooking_meterial: null
  }),
  methods: {
    get_food_data() {
      this.$axios
        .get(
          "/openapi/59bcdda005827dab577c5d693e6d162d49bd93d6c087f359d170465129ae5a5d/json/Grid_20150827000000000228_1/1/10"
        )
        .then(res => {
          this.recipes_img = [];

          this.recipes_order = res.data.Grid_20150827000000000228_1.row.reduce(
            (obj, v) => {
              // 이미지
              if (v.COOKING_NO === 1 || v.COOKING_NO === 2) {
                this.recipes_img.push(v.STRE_STEP_IMAGE_URL);
              }

              // 요리순서
              if (obj[v.RECIPE_ID] === undefined) {
                obj[v.RECIPE_ID] = [v.COOKING_DC];
              } else {
                obj[v.RECIPE_ID].push(v.COOKING_DC);
              }
              return obj;
            },
            {}
          );
        });

      this.$axios
        .get(
          "/openapi/59bcdda005827dab577c5d693e6d162d49bd93d6c087f359d170465129ae5a5d/json/Grid_20150827000000000227_1/1/30"
        )
        .then(res => {
          this.cooking_meterial = res.data.Grid_20150827000000000227_1.row.reduce(
            (obj, v) => {
              // 요리재료
              if (obj[v.RECIPE_ID] === undefined) {
                obj[v.RECIPE_ID] = [v];
              } else {
                obj[v.RECIPE_ID].push(v);
              }
              return obj;
            },
            {}
          );
        });
    }
  },
  beforeMount() {
    console.log(this.$route.params.id);
    this.get_food_data();
  }
};
</script>
