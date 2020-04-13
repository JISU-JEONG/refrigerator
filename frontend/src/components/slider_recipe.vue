<template>
  <div>
    <vueper-slides
      v-if="recipes_img !== null"
      ref="vueperslides1"
      fixed-height="500px"
      @slide="
        $refs.vueperslides2 &&
          $refs.vueperslides2.goToSlide($event.currentSlide.index, {
            emit: false
          })
      "
      :slide-ratio="1 / 4"
      :bullets="false"
    >
      <vueper-slide
        v-for="(recipe, i) in recipes_img"
        :key="i"
        :image="recipe"
      />
    </vueper-slides>
    <br />
    <vueper-slides
      v-if="recipes_img != null"
      ref="vueperslides2"
      :slide-ratio="1 / 8"
      :dragging-distance="50"
      @slide="
        $refs.vueperslides1 &&
          $refs.vueperslides1.goToSlide($event.currentSlide.index, {
            emit: false
          })
      "
      :visible-slides="4"
      fixed-height="130px"
    >
      <vueper-slide
        v-for="(recipe, i) in recipes_img"
        :key="i"
        @click.native="$refs.vueperslides2 && $refs.vueperslides2.goToSlide(i)"
      >
        <template v-slot:content>
          <img :src="recipe" />
        </template>
      </vueper-slide>
    </vueper-slides>
  </div>
</template>

<script>
import { VueperSlides, VueperSlide } from "vueperslides";
import "vueperslides/dist/vueperslides.css";

export default {
  name: "silder_recipe",
  components: { VueperSlides, VueperSlide },
  data: () => ({}),
  props: {
    recipes_img: {
      type: Array
    }
  }

  // watch: {
  //   recipes: function(v) {
  //     this.recipes = v;
  //   }
  // },
};
</script>
