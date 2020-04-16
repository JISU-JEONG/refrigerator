<template>
  <div>
    <div class="meterial-container">
      <div class="meterial-container-title">
        <b>재료</b>
        <span>Meterial</span>
      </div>
      <div class="meterial-list" id="divConfirmedMaterialArea">
        <ul class="case1">
          <li v-for="(meterial, i) in recipeMeterial" :key="i">
            {{meterial.IRDNT_NM}}
            <span class="meterial-unit">{{meterial.IRDNT_CPCTY}}</span>
          </li>
        </ul>
      </div>
    </div>

    <!-- <div v-for="(recipeItem, i) in recipeMeterial" :key="i">
      <v-card class="mx-auto" max-width="344" outline>
        <v-card-text v-for="(meterial, i) in recipeItem" :key="i">
          <p>{{ meterial }}</p>
          <v-divider></v-divider>
        </v-card-text>
      </v-card>
      <br />
    </div>-->
  </div>
</template>

<script>
export default {
  name: "RecipeMeterial",
  props: {
    recipeMeterial: {
      type: Array
    }
  }
};
</script>

<style scoped>
/*
xs = 600px 
sm = 600px > < 960px
md = 960px > < 1264px*
ld = 1264px* > < 1904px*

*/
@media all and (min-width: 600px) and (max-width: 960px) {
  .meterial-list ul.case1 li {
    width: 100%;
    display: inline-block;
    vertical-align: top;
  }
  .meterial-list {
    margin-right: 50px;
  }
}
@media all and (min-width: 961px) and (max-width: 1904px) {
  .meterial-list ul.case1 li {
    width: 43%;
    display: inline-block;
    vertical-align: top;
  }
}

.meterial-container {
  padding: 35px 20px 0 25px;
}

.meterial-container .meterial-container-title {
  margin: 0 -25px;
}

.meterial-container-title {
  font-size: 20px;
  color: #000;
  padding: 0 35px 30px 35px;
}
.meterial-container-title b {
  font-weight: 500;
}
.meterial-container-title span {
  color: #ccc;
  font-size: 14px;
  font-style: italic;
  padding-left: 4px;
}

.menu_best .meterial-container-title {
  position: absolute;
  left: 50%;
  top: 25px;
  margin-left: -185px;
  z-index: 100;
}

.meterial-container .meterial-container-title {
  margin: 0 -25px;
}

.meterial-list {
  padding: 0 20px 18px 24px;
  vertical-align: top;
}
.meterial-list ul {
  padding: 0 0 25px 0;
  width: 49%;
  display: inline-block;
  vertical-align: top;
}
.meterial-list ul.case1 {
  width: 100%;
}
.meterial-list li {
  border-bottom: 1px solid #ececec;
  padding: 10px 6px;
  list-style: none;
  margin: 0 35px;
  font-size: 16px;
}
.meterial-list li a {
  margin: -1px 0 0 5px;
  vertical-align: top;
  display: inline-block;
}
.meterial-list li a img {
  width: 20px;
  height: 20px;
}
.meterial-list li .meterial-unit {
  float: right;
  color: #999;
}
</style>