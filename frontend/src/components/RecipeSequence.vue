<template>
  <div>
    <div class="sequence-container">
      <div class="sequence-container-title">
        <b>조리순서</b>
        <span>Steps</span>
      </div>
      <div v-for="(sequence, i) in recipeSequence" :key="i">
        <div class="sequence_step" :style="getSequnceNumber(i + 1)">
          <div>{{ sequence.process_info }}</div>
          <img :src="sequence.process_imgurl" />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "RecipeSequence",
  props: {
    recipeSequence: {
      type: Array
    },
    recipeCarousel: {
      type: Array
    }
  },
  methods: {
    getSequnceNumber(index) {
      return (
        "background: url(https://recipe1.ezmember.co.kr/img/icon_step_" +
        index +
        ".gif) no-repeat; background-size: 36px;"
      );
    }
  }
};
</script>

<style scope>
.sequence-container-title {
  font-size: 20px;
  color: #000;
  padding: 0 35px 30px 35px;
}

.sequence-container {
  padding: 35px 20px 0 25px;
}

.sequence-container .sequence-container-title {
  margin: 0 -25px;
}

.sequence-container-title {
  font-size: 20px;
  color: #000;
  padding: 0 35px 30px 35px;
}

.sequence-container-title b {
  font-weight: 500;
}

.sequence-container-title span {
  color: #ccc;
  font-size: 14px;
  font-style: italic;
  padding-left: 4px;
}

.sequence .sequence-container-title {
  position: absolute;
  left: 50%;
  top: 25px;
  margin-left: -185px;
  z-index: 100;
}

.sequence-container .sequence-container-title {
  margin: 0 -25px;
}

.sequence_step {
  margin: 10px 20px 0 20px;
}

.sequence_step > div {
  min-height: 35px;
  margin-bottom: 15px;
  margin-left: 50px;
  display: flex;
  align-items: center;
}

.sequence_step > img {
  max-width: 100%;
  margin-bottom: 15px;
}
</style>
