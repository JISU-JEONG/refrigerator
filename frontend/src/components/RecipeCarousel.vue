<template>
  <div>
    <vueper-slides
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
        v-for="(recipeItem, i) in recipeCarousel"
        :key="i"
        :image="recipeItem"
      />
    </vueper-slides>
    <br />
    <vueper-slides
      ref="vueperslides2"
      :slide-ratio="1 / 4"
      :dragging-distance="50"
      @slide="
        $refs.vueperslides1 &&
          $refs.vueperslides1.goToSlide($event.currentSlide.index, {
            emit: false
          })
      "
      :visible-slides="2"
      fixed-height="130px"
    >
      <vueper-slide
        v-for="(recipeItem, i) in recipeCarousel"
        :key="i"
        @click.native="$refs.vueperslides2 && $refs.vueperslides2.goToSlide(i)"
      >
        <template v-slot:content>
          <img :src="recipeItem" />
        </template>
      </vueper-slide>
    </vueper-slides>
  </div>
</template>

<script>
import { VueperSlides, VueperSlide } from "vueperslides";
import "vueperslides/dist/vueperslides.css";

export default {
  name: "RecipeCarousel",
  components: { VueperSlides, VueperSlide },
  data: () => ({}),
  props: {
    recipeCarousel: {
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
