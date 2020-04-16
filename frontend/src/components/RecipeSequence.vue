<template>
  <div>
    <div class="view2_box">
      <div class="best_tit">
        <b>조리순서</b>
        <span>Steps</span>
      </div>
      <div v-for="(sequence, i) in recipeSequence" :key="i">
        <div :class="getClassPath(i+1)">
          <div>{{sequence.COOKING_DC}}</div>
        </div>
      </div>

      <div class="view_tip">
        *토마토 씨를 제거 해 주면 즙이 덜 생겨요
        <p></p>*참기름 대신 올리브오일 넣어도 됩니다
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
    }
  },
  methods: {
    getClassPath(index) {
      return "view_step_cont step" + index;
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
  width: 300px;
  font-size: 22px;
}
.view_step_cont.step1 {
  background: url(https://recipe1.ezmember.co.kr/img/icon_step_1.gif) no-repeat
    48px 6px;
  background-size: 36px;
}
.view_step_cont.step2 {
  background: url(https://recipe1.ezmember.co.kr/img/icon_step_2.gif) no-repeat
    48px 6px;
  background-size: 36px;
}
.view_step_cont.step3 {
  background: url(https://recipe1.ezmember.co.kr/img/icon_step_3.gif) no-repeat
    48px 6px;
  background-size: 36px;
}
.view_step_cont.step4 {
  background: url(https://recipe1.ezmember.co.kr/img/icon_step_4.gif) no-repeat
    48px 6px;
  background-size: 36px;
}
.view_step_cont.step5 {
  background: url(https://recipe1.ezmember.co.kr/img/icon_step_5.gif) no-repeat
    48px 6px;
  background-size: 36px;
}
.view_step_cont.step6 {
  background: url(https://recipe1.ezmember.co.kr/img/icon_step_6.gif) no-repeat
    48px 6px;
  background-size: 36px;
}
.view_step_cont.step7 {
  background: url(https://recipe1.ezmember.co.kr/img/icon_step_7.gif) no-repeat
    48px 6px;
  background-size: 36px;
}
.view_step_cont.step8 {
  background: url(https://recipe1.ezmember.co.kr/img/icon_step_8.gif) no-repeat
    48px 6px;
  background-size: 36px;
}
.view_step_cont.step9 {
  background: url(https://recipe1.ezmember.co.kr/img/icon_step_9.gif) no-repeat
    48px 6px;
  background-size: 36px;
}
.view_step_cont.step10 {
  background: url(https://recipe1.ezmember.co.kr/img/icon_step_10.gif) no-repeat
    48px 6px;
  background-size: 36px;
}
.view_step_cont.step11 {
  background: url(https://recipe1.ezmember.co.kr/img/icon_step_11.gif) no-repeat
    48px 6px;
  background-size: 36px;
}
.view_step_cont.step12 {
  background: url(https://recipe1.ezmember.co.kr/img/icon_step_12.gif) no-repeat
    48px 6px;
  background-size: 36px;
}
.view_step_cont.step13 {
  background: url(https://recipe1.ezmember.co.kr/img/icon_step_13.gif) no-repeat
    48px 6px;
  background-size: 36px;
}
.view_step_cont.step14 {
  background: url(https://recipe1.ezmember.co.kr/img/icon_step_14.gif) no-repeat
    48px 6px;
  background-size: 36px;
}
.view_step_cont.step15 {
  background: url(https://recipe1.ezmember.co.kr/img/icon_step_15.gif) no-repeat
    48px 6px;
  background-size: 36px;
}
.view_step_cont.step16 {
  background: url(https://recipe1.ezmember.co.kr/img/icon_step_16.gif) no-repeat
    48px 6px;
  background-size: 36px;
}
.view_step_cont.step17 {
  background: url(https://recipe1.ezmember.co.kr/img/icon_step_17.gif) no-repeat
    48px 6px;
  background-size: 36px;
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
