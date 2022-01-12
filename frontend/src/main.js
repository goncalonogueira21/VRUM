import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import vuetify from "./plugins/vuetify";
import store from "./store"
import axios from "axios"
import titleMixin from './mixins/titleMixin'
import request from "./services/request";

const token = localStorage.getItem('user-token')
if (token) {
  axios.defaults.headers.common['Authorization'] = token
}

Vue.config.productionTip = false;
Vue.use(request)
Vue.mixin(titleMixin)


new Vue({
  router,
  vuetify,
  store,
  render: (h) => h(App),
}).$mount("#app");
