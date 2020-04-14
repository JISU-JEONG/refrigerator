<template>
  <div class="hello">
    <h1>{{ message }}</h1>
    <ul>
      <li><input type="text" v-model="frist" /></li>
      <li><input type="text" v-model="second" /></li>
      <li>= {{ total }}</li>
    </ul>
    <ul>
      <li>
        <input type="button" value="더하기" @click="plus(frist, second)" />
      </li>
      <li>
        <input type="button" value="빼기" @click="minus(frist, second)" />
      </li>
      <li>
        <input type="button" value="곱하기" @click="multiply(frist, second)" />
      </li>
      <li>
        <input
          type="button"
          value="나누기(반올림)"
          @click="divide(frist, second)"
        />
      </li>
    </ul>
    <h2></h2>
    <!-- 결과값 -->
  </div>
</template>

<script>
export default {
  name: "HelloWorld",
  data() {
    return {
      message: "Unit Test",
      frist: 7,
      second: 2,
      total: 0
    };
  },
  methods: {
    plus(frist, second) {
      this.total = parseInt(frist) + parseInt(second);
      return this.total;
    },
    minus(frist, second) {
      this.total = parseInt(frist) - parseInt(second);
      return this.total;
    },
    multiply(frist, second) {
      if (parseInt(frist) == 0 || parseInt(second) == 0) {
        return false;
      }
      this.total = parseInt(frist) * parseInt(second);
      return this.total;
    },
    divide(frist, second) {
      if (parseInt(frist) == 0 || parseInt(second) == 0) {
        return false;
      }
      this.total = parseInt(frist) / parseInt(second);
      this.total = Math.round(this.total); // 소스점 반올림
      return this.total;
    }
  }
};
</script>
