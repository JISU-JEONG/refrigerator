<template>
  <div>
    <div class="view2_box">
      <div class="best_tit">
        <b>조리순서</b>
        <span>Steps</span>
      </div>
      <div v-for="(sequence, i) in recipeSequence" :key="i">
        <div class="view_step_cont" :style="getSequnceNumber(i + 1)">
          <div>{{ sequence.process_info }}</div>
          <img :src="sequence.process_imgurl" />
        </div>
      </div>

      <div class="view_tip">
        *토마토 씨를 제거 해 주면 즙이 덜 생겨요
        <p></p>
        *참기름 대신 올리브오일 넣어도 됩니다
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
        ".gif) no-repeat 48px 6px; background-size: 36px;"
      );
    }
  }
};
</script>

<style scope>
.view2_box {
  padding: 0 12px 15px;
  line-height: 1.8;
  letter-spacing: -0.02em;
}
.view2_box .tit {
  font-size: 20px;
  font-weight: bold;
  margin: 30px 0 10px;
}
.view2_box p {
  margin: 0;
}
.view2_box dt {
  margin: 15px 0;
}
.view2_box dd {
  margin-bottom: 24px;
  line-height: 1.8;
}
.view2_box dl {
  margin-bottom: 10px;
}
.best_tit {
  font-size: 20px;
  color: #000;
  padding: 0 35px 30px 35px;
}
.best_tit b {
  font-weight: 500;
}
.best_tit span {
  color: #ccc;
  font-size: 14px;
  font-style: italic;
  padding-left: 4px;
}
.view_step {
  padding: 35px 0 10px;
}

.view_step_cont {
  padding: 6px 0 60px 96px;
  width: 100%;
  font-size: 22px;
}

.view_step_cont img {
  border-radius: 10px;
  max-width: 100%;
  height: auto;
  margin: 20px 0 10px;
}
.view_step_cont .media-right {
  padding-left: 20px;
}
.view_step_cont .media-right img {
  margin: 0;
}

.view_tip {
  background: url(https://recipe1.ezmember.co.kr/img/mobile/tit_tip.png) left
    top no-repeat;
  background-size: 110px;
  padding: 38px 18px 15px 20px;
  margin-left: 50px;
  font-size: 14px;
  line-height: 1.6;
}
</style>
