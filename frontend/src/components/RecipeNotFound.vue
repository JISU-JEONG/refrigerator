<template>
  <div class="back">
    <div class="container">
      <div class="caption">
        <div class="hat-cont">
          <div class="lines"></div>
          <div class="hat"></div>
          <div class="left"></div>
          <div class="top"></div>
          <div class="left-opp"></div>
        </div>
        <div class="head-text">Recipe Not Found !</div>
      </div>
      <div class="head">
        <div class="pan-wrapper">
          <div class="center">
            <div class="sub-center">
              <div class="egg">
                <div class="yolk"></div>
              </div>
            </div>
          </div>
          <div class="handle"></div>
          <div class="handle-sub"></div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {};
</script>

<style lang="scss" scoped>
$sec-color: #8a8f99;
$pri-color: #232731;
$bg: #ffe566;
$color-yolk: #f9d010;
.back {
  background-color: $bg;
  width: 100%;
  height: 100vh;
}
.container {
  width: 80%;
  height: 60%;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}

.caption {
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
}

.head-text {
  font-family: "Satisfy", cursive;
  color: $pri-color;
  font-size: 20px;
  position: relative;
  left: 30px;
}

.hat-cont {
  width: 75px;
  height: 75px;
  position: relative;
  transform: rotate(-30deg);
  top: -15px;
  animation: hat 1s infinite forwards;
}

.hat {
  width: 40px;
  height: 30px;
  border: 2px solid black;
  border-top: none;
  position: absolute;
  bottom: 0px;
  left: 15px;

  &:after {
    width: 40px;
    content: "";
    display: inline-block;
    border: 1px solid black;
    position: absolute;
    bottom: 7px;
    left: 0px;
  }
}

.line {
  width: 0px;
  height: 6px;
  border: 1px solid black;
  position: absolute;
}
.lines {
  @extend .line;
  top: 50px;
  left: 45%;
  &:after {
    @extend .line;
    content: "";
    top: -1px;
    left: 10px;
  }
  &:before {
    @extend .line;
    content: "";
    top: -1px;
    right: 10px;
  }
}
.hat-base {
  height: 30px;
  width: 15px;
  position: absolute;
}
.left {
  @extend .hat-base;
  border-bottom-left-radius: 30px;
  border-top-left-radius: 30px;
  border: 2px solid black;
  border-right: none;
  top: 13px;
  z-index: 2;
  background: $bg;
}
.left-opp {
  @extend .left;
  transform: rotate(180deg);
  right: 5px;
}
.top {
  height: 20px;
  width: 40px;
  position: absolute;
  border-top-right-radius: 30px;
  border-top-left-radius: 30px;
  left: 14px;
  border: 2px solid black;
  border-bottom: none;
}

.pan-wrapper {
  transform: scale(0.6);
  position: relative;
  left: 20%;
}

.center {
  width: 300px;
  height: 300px;
  border-radius: 50%;
  background-color: $sec-color;
  position: relative;
  z-index: 2;
  border: 1px solid black;

  .sub-center {
    width: 270px;
    height: 270px;
    border-radius: 50%;
    background-color: $pri-color;
    position: absolute;
    top: 0px;
    left: 0px;
    bottom: 0px;
    right: 0px;
    margin: auto;
  }
}

.handle {
  width: 40px;
  height: 150px;
  position: absolute;
  left: 263px;
  top: 280px;
  transform: rotate(-35deg);
  background: $pri-color;
  z-index: 2;
  border-radius: 2px;
}

.handle-sub {
  width: 25px;
  height: 50px;
  content: "";
  display: inline-block;
  position: absolute;
  left: 220px;
  top: 260px;
  transform: rotate(-38deg);
  background: $sec-color;
}

.egg {
  width: 130px;
  height: 130px;
  background: white;
  border-radius: 50%;
  position: absolute;
  top: 0px;
  left: 0px;
  right: 0px;
  bottom: 0px;
  margin: auto;
  animation: egg 2s ease-in infinite forwards;
}

.yolk {
  position: absolute;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  margin: auto;
  background-color: $color-yolk;
  width: 50%;
  height: 50%;
  border-radius: 50%;
  box-shadow: inset $color-yolk 0 0 0 4px,
    inset rgba(white, 0.3) 2px 2px 4px 6px, inset $color-yolk 2px 2px 4px 16px,
    inset rgba(white, 0.3) -2px -2px 12px 12px, rgba(black, 0.05) 0 0 2px 2px;
}

.text {
  font-size: 240px;
  font-family: "Satisfy", cursive;
  position: absolute;
  top: 20%;
  color: $pri-color;
}

.center::after {
  @extend .text;
  right: -150px;
}
.center::before {
  @extend .text;
  left: -150px;
}

@keyframes egg {
  0%,
  100% {
    transform: scale(1);
  }
  50% {
    transform: scale(1.2);
  }
}

@keyframes hat {
  0%,
  100% {
    transform: rotate(-30deg);
  }
  50% {
    transform: rotate(-25deg);
  }
}

@media only screen and (min-width: 1000px) {
  .pan-wrapper {
    top: 50px;
  }
}
</style>