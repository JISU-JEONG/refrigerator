<template>
  <div>
    <div class="intro-backaground">
      <div class="intro-container">
        <p>메인 어찌합니까</p>
        <!-- <div class="intro-card">여기에 이제 어쩌구 저쩌구 관련 내용이 들어가고 마지막에는 카메라 페이지 가기 버튼을 넣으려구요</div>
        <div class="intro-card">여기에 이제 어쩌구 저쩌구 관련 내용이 들어가고 마지막에는 카메라 페이지 가기 버튼을 넣으려구요</div>
        <div class="intro-card">여기에 이제 어쩌구 저쩌구 관련 내용이 들어가고 마지막에는 카메라 페이지 가기 버튼을 넣으려구요</div>
        <div class="intro-card">여기에 이제 어쩌구 저쩌구 관련 내용이 들어가고 마지막에는 카메라 페이지 가기 버튼을 넣으려구요</div> -->
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: "Main",
  components: {},
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
.intro-backaground {
  width: 100%;
  height: 100vh;
  background: rgb(77, 71, 71);
  padding-top: 80px;
  display: flex;
  align-items: center;
  justify-content: center;
}
.intro-container {
  width: 100%;
  max-width: 1200px;
  padding: 1rem;
  margin: 0 auto;
  box-sizing: border-box;
}
.intro-card {
  width: 90%;
  height: 250px;
  display: inline-block;
  margin: 16px;
  padding: 16px;
  box-sizing: border-box;
  border: 2px solid white;
  border-radius: 10px;
  font-size: 1.5rem;
  color: white;
}
@media (max-width: 850px) {
  .intro-card {
    width: 100%;
    height: 20vh;
    margin: 0 0 8px 0;
    font-size: 1rem;
  }
}
</style>
