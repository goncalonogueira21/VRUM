import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import Search from "../views/Search.vue";
import Auth from "../components/auth.vue";
import Profile from "../views/Profile"
import CriarViagem from "../views/CriarViagem"
import Viagens from "../views/Viagens"
import Viagem from "../views/Viagem"
import Mensagens from "../views/Mensagens"
import Pedidos from "../views/Pedidos"
import Historico from "../views/HistoricoViagens"
import Carteira from "../views/Carteira"
import HomeLogado from "../views/HomeLogado"
import Page404 from "../views/PageNotFound.vue"
import Settings from "../views/Settings.vue"

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
  {
    path: "/viagem/:id",
    name: "Viagem",
    component: Viagem,
  },
  {
    path: "/inbox",
    name: "inbox",
    component: Mensagens,
  },
  {
    path: "/pedidos",
    name: "pedidos",
    component: Pedidos,
  },
  {
    path: "/historico",
    name: "historico",
    component: Historico,
  },
  {
    path: "/carteira",
    name: "carteira",
    component: Carteira,
  },
  {
    path: "/homeLogado",
    name: "homeLogado",
    component: HomeLogado,
  },
  {
    path: "/settings",
    name: "settings",
    component: Settings,
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


router.beforeEach((to, from, next) => {
  // redirect to login page if not logged in and trying to access a restricted page
  const publicPages = ['/','/auth'];
  const authRequired = !publicPages.includes(to.path);
  const loggedIn = localStorage.getItem('user-token');

  if (authRequired && !loggedIn) {
    return next('/auth');
  }

  next();
})
export default router;
