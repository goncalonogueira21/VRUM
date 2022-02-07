import Vue from "vue";
import SocketIO from "socket.io-client";
import VueSocketIO from "vue-socket.io";
import App from "./App.vue";
import router from "./router";
import vuetify from "./plugins/vuetify";
import store from "./store"
import axios from "axios"
import titleMixin from './mixins/titleMixin'
import request from "./services/request";
import VueGeolocation from 'vue-browser-geolocation';
import * as VueGoogleMaps from 'vue2-google-maps'
import VueGooglePlaces from 'vue-google-places'


const token = localStorage.getItem('user-token')
if (token) {
  axios.defaults.headers.common['Authorization'] = token
}

Vue.config.productionTip = false;



Vue.use(VueGeolocation);
Vue.use(VueGooglePlaces)
Vue.use(VueGoogleMaps, {
  load: {
    key: 'AIzaSyA0NR6fs6UYHQaq6jlrpLqIiUCIRzEhN9A',
    libraries: 'places',
  },
})

Vue.use(request)
Vue.use(new VueSocketIO({
  debug: true,
  connection: SocketIO('http://127.0.0.1:5000'), //options object is Optional
})
);

Vue.mixin(titleMixin)


new Vue({
  router,
  vuetify,
  store,
  render: (h) => h(App),
}).$mount("#app");
