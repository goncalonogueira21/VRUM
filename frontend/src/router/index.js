import Vue from "vue";
import VueRouter from "vue-router";
import Auth from "../components/auth.vue";

Vue.use(VueRouter);

const routes = [
 
  {
    path: "/auth",
    name: "auth",
    component: Auth,
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
