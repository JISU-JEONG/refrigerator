import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    name: null
  },
  mutations: {
    setValue(state, payload) {
      state.name = payload.name;
    }
  },
  actions: {
    VuexTest(context, payload) {
      context.commit("setValue", payload);
    }
  }
});
