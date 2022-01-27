<template>
  <v-app>
    <v-main>
        <router-view></router-view>
        <v-container/>
        <Notificacao/>
        <Footer></Footer>
    </v-main>
  </v-app>
</template>

<script>
import Footer from "./components/Footer.vue";
import Notificacao from "./components/notificacao.vue"

export default {
  name: "App",
  title: "VRUM",
  components: {
    Footer, Notificacao
  },

  data: () => ({
    home: true
  }),
}
</script>
