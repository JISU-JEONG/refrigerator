import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    data: null,
    showMaterialPage: false
  },
  mutations: {
    setValue(state, payload) {
      state.data = payload.recipeInfoArr;
    }
  },
  actions: {
    recipeInfo(context, payload) {
      context.commit("setValue", payload);
    }
  }
});
