<template>
  <v-container class="my-5">
    <Header @clicked="onClickHeader"></Header>
    <NavDraw ref="navdraw"></NavDraw>
    <p> Mostrar dados da viagem </p>
    <p> Mostrar mapa da viagem </p>
    <p> Butoes para editar a viagem </p> 

    <Footer></Footer>
  </v-container>
</template>

<script>
import Header from "../components/Header.vue";
import Footer from "../components/Footer.vue";
import NavDraw from "../components/NavDraw.vue";

export default {
  name: "Viagem",
  components: {
    Header,
    Footer,
    NavDraw,
  },

  data() {
    return {
      tab: null,
      openHelp: false,
    };
  },
  methods: {
    onClickHeader() {
      this.$refs.navdraw.fixNav();
    },
  },
};
</script>
