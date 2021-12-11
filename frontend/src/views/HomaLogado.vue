<template>
  <v-container class="my-5">
    <Header></Header>
    <NavDraw></NavDraw>
    <Footer></Footer>
  </v-container>
</template>

<script>
import Header from "../components/Header.vue"
import Footer from "../components/Footer.vue"
import NavDraw from "../components/NavDraw.vue"


export default {
    name: "HomeLogado",
    components: {
        Header,
        Footer,
        NavDraw,
    },
     data() {
    return{
      tab: null,
      openHelp: false,
    }
   }
}
</script>