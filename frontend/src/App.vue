<template>
  <v-app>
    <v-main>
        <router-view></router-view>
        <v-container/>
        <Footer></Footer>
    </v-main>
  </v-app>
</template>

<script>
import Footer from "./components/Footer.vue";

export default {
  name: "App",
  title: "VRUM",
  components: {
    Footer,
  },

  data: () => ({
    home: true
  }),
}
</script>
