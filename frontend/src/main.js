import Vue from "vue";
import App from "./App.vue";
import router from "./router/index";
import vuetify from "./plugins/vuetify";
import AxiosPlugin from "vue-axios-cors";
import store from "./store";
import "./registerServiceWorker";

import "fullpage.js/vendors/scrolloverflow"; // Optional. When using scrollOverflow:true
import VueFullPage from "vue-fullpage.js";

Vue.config.productionTip = false;
Vue.use(AxiosPlugin);
Vue.use(VueFullPage);

new Vue({
  render: h => h(App),
  vuetify,
  router,
  store
}).$mount("#app");
