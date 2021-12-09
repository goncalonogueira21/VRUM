import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import Search from "../views/Search.vue";
import Auth from "../components/auth.vue";
import Profile from "../views/Profile"
import CriarViagem from "../views/CriarViagem"
import Viagens from "../views/Viagens"
import Page404 from "../views/PageNotFound.vue"

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: 'Home',
    component: Home
  },
  {
    path: "/search",
    name: 'Search',
    component: Search
  },
  {
    path: "/auth",
    name: "auth",
    component: Auth,
  },
  {
    path: "/profile",
    name: "Profile",
    component: Profile,
  },
  {
    path: "/criarviagem",
    name: "CriarViagem",
    component: CriarViagem,
  },
  {
    path: "/viagens",
    name: "Viagens",
    component: Viagens,
  },


  { path: "/*",
    name: "Page404",
    component: Page404 
  }

];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
