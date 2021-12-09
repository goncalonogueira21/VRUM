<template>
  <v-container class="my-5">
    <Header></Header>
    <NavDraw></NavDraw>
    <TabelaViagens/>
    <Footer></Footer>
  </v-container>
</template>

<script>
import Header from "../components/Header.vue"
import Footer from "../components/Footer.vue"
import NavDraw from "../components/NavDraw.vue"
import TabelaViagens from "../components/TabelaViagens.vue"


export default {
    name: "Search",
    components: {
        Header,
        Footer,
        NavDraw,
        TabelaViagens
    },
     data() {
    return{
      tab: null,
      openHelp: false,
      items: [
        { tab: 'Inserir Viagem'}
      ]}
   }
}
</script>

