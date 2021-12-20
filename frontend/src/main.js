import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import vuetify from "./plugins/vuetify";
import store from "./store"
import titleMixin from './mixins/titleMixin'

Vue.config.productionTip = false;

Vue.mixin(titleMixin)

new Vue({
  router,
  vuetify,
  store,
  render: (h) => h(App),
}).$mount("#app");
