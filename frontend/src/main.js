import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import vuetify from "./plugins/vuetify";
import store from "./store"
import axios from "axios"
import titleMixin from './mixins/titleMixin'
import request from "./services/request";
import VueGeolocation from 'vue-browser-geolocation';
import * as VueGoogleMaps from 'vue2-google-maps'

const token = localStorage.getItem('user-token')
if (token) {
  axios.defaults.headers.common['Authorization'] = token
}

Vue.config.productionTip = false;
Vue.use(VueGeolocation);
Vue.use(request)
Vue.mixin(titleMixin)
Vue.use(VueGoogleMaps, {
  load: {
    key: 'AIzaSyDUllI61bsFW7A0eti3Ks7dsVfcRfwMtDc',
    libraries: 'places',
  },
})



new Vue({
  router,
  vuetify,
  store,
  render: (h) => h(App),
}).$mount("#app");
