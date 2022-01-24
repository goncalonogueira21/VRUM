<template>

      <v-container class="my-5">
          <Header @clicked="onClickHeader"></Header>
          <NavDraw ref="navdraw"></NavDraw>
  <div>
    <h1 class="pa-md-4 mx-lg-auto text-center">Carteira em desenvolvimento</h1>
  </div>
      </v-container>
</template>

<script>
import Header from "../components/Header.vue";
import NavDraw from "../components/NavDraw.vue";
export default {

  components: {
    Header,
    NavDraw,
  },
  data() {
    return {};
  },
  methods: {
    onClickHeader() {
      this.$refs.navdraw.fixNav();
    },
  }
};
</script>
