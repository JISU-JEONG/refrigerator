<template>
  <div>
    <v-row style="display:flex; justify-content:center">
      <v-card
        class="col-xs-12 col-sm-6 col-md-4 col-lg-2"
        v-for="category in categorys"
        :key="category[0]"
        width="170"
        style="margin:5px;"
      >
        <strong v-if="category[1] === undefined">{{ category[0] }}</strong>
        <strong v-else>{{ category[1] }}</strong>

        <v-img
          class="white--text align-end pa-md-4 mx-lg-auto"
          :src="getImgPath(category[0])"
        ></v-img>
      </v-card>
    </v-row>

    <br />
  </div>
</template>

<script>
export default {
  name: "category",

  data: () => ({
    categorys: [
      ["밥"],
      ["떡", "떡 / 한과"],
      ["면류"],
      ["국"],
      ["샐러드", "나물 / 생체 / 샐러드"],
      ["구이"],
      ["볶음"],
      ["밑반찬", "밑반찬 / 김치"],
      ["조림"],
      ["찜"],
      ["튀김", "튀김 / 커틀릿"],
      ["찌개", "찌개 / 전골 / 스튜"],
      ["도시락", "도시락 / 간식"],
      ["부침"],
      ["양식"],
      ["샌드위치", "샌드위치 / 햄버거"],
      ["빵", "빵 / 과자"],
      ["음료"],
      ["피자"],
      ["리조트", "그라탕 / 리조트"]
    ]
  }),

  methods: {
    getImgPath(name) {
      return require("../assets/category/" + name + ".png");
    }
  }
};
</script>
