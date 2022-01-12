<template>
  <v-container class="my-5">
    <Header @clicked="onClickHeader"></Header>
    <NavDraw ref="navdraw"></NavDraw>
    <p>Token is {{ token }}</p>
  </v-container>
</template>

<script>
import Header from "../components/Header.vue";
import NavDraw from "../components/NavDraw.vue";
import { mapState } from "vuex";

export default {
  computed: mapState({
    token: (state) => state.auth.token,
  }),

  components: {
    Header,
    NavDraw,
  },
  name: "HomeLogado",
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
