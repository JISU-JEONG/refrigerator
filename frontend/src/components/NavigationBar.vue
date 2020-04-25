<template>
  <header>
    <h1>
      <router-link to="/">냉장고를 부탁해</router-link>
    </h1>
    <nav>
      <ul>
        <li>
          <router-link to="/RecipeList">A</router-link>
        </li>
        <li>
          <router-link to="/RecipeRecommendation">B</router-link>
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
  height: 70px;
  width: 100%;
  max-width: 600px;
  background: white;
  position: fixed;
  top: 0;
  z-index: 100;
  border-bottom: 1px solid #cacaca;
  box-shadow: 1px 2px 4px rgba(180, 180, 180, 0.3);
}
header h1 {
  display: inline-block;
  position: absolute;
  left: 24px;
}
header h1 a {
  text-decoration: none;
  display: inline-block;
  height: 70px;
  line-height: 70px;
  font-size: 25px;
  font-family: "Gugi", cursive;
  color: rgba(0, 0, 0, 0.9) !important;
}
header nav {
  display: inline-block;
  position: absolute;
  top: 0;
  right: 24px;
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
  height: 70px;
  line-height: 70px;
  font-size: 18px;
  color: rgba(0, 0, 0, 0.9) !important;
}
.header-transparent {
  background: transparent;
  border-bottom: none;
  box-shadow: none;
}
.header-transparent a {
  color: white !important;
}
@media (max-width: 850px) {
  header nav li {
    padding: 0 5px;
  }
  header nav li a {
    font-size: 12px;
  }
}
</style>
