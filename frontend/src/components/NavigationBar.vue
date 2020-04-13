<template>
  <header>
    <h1>
      <router-link to="/">HOME</router-link>
    </h1>
    <nav>
      <ul>
        <li>
          <router-link to="/food">음식 목록(공공데이터 확인용)</router-link>
        </li>
        <li>
          <router-link to="/foodlist">음식 목록(찐)</router-link>
        </li>
        <li>
          <router-link to="/recipe">레시피</router-link>
        </li>
        <li>
          <router-link to="/meterial">재료</router-link>
        </li>
        <li>
          <router-link to="/camera">카메라</router-link>
        </li>
      </ul>
    </nav>
  </header>
</template>

<script>
export default {
  name: "NavigationBar"
};
</script>
<style>
header {
  height: 80px;
  width: 100%;
  background: #ffffff;
  position: fixed;
  top: 0;
  z-index: 1;
  border-bottom: 1px solid #dbdbdb;
}
header h1 {
  display: inline-block;
  position: absolute;
  left: 50px;
}
header h1 a {
  text-decoration: none;
  display: inline-block;
  height: 80px;
  line-height: 80px;
  color: #888888 !important;
}
header nav {
  display: inline-block;
  position: absolute;
  top: 0;
  right: 50px;
}
header nav li {
  list-style: none;
  float: left;
  padding: 0 10px;
}
header nav li:last-child {
  padding-right: 0;
}
header nav li a {
  text-decoration: none;
  display: inline-block;
  height: 80px;
  line-height: 80px;
  font-size: 18px;
  color: #888888 !important;
}
.header-transparent {
  background: transparent;
  border-bottom: none;
}
.header-transparent a {
  color: white !important;
}
</style>
