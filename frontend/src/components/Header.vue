<template>
  <v-app-bar app color="#7e380e" height="80" clipped-left>
    <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>

    <v-list nav dense dark color="#7e380e">
      <v-list-item two-line class="px-4">
        <v-list-item-content>
          <v-list-item-title><h2>VRUM</h2></v-list-item-title>
          <v-list-item-subtitle>Vehicle Rides UM</v-list-item-subtitle>
        </v-list-item-content>
      </v-list-item>
    </v-list>
    <div class="spacer"></div>
    <v-list-item-group>
      <v-list-item disabled dark>
        <v-list-item-content>
          <v-list-item-title>Nome do utilizador</v-list-item-title>
        </v-list-item-content>
      </v-list-item>
    </v-list-item-group>
  </v-app-bar>
</template>

<script>
//import axios from 'axios'
//import NavDraw from "../NavDraw.vue"

export default {
  components: {
    //'navDraw':NavDraw
  },
  data() {
    return {
      parametro: "",
      drawer: false,
      group: null,
    };
  },
  methods: {
    logout: function () {
      //Função de logout
    },
  },
  watch: {
    group() {
      this.drawer = false;
    },
  },
};
</script>

<style scoped>
/* css do cabeçalho */
.v-toolbar__content,
.v-toolbar__extension {
  position: relative;
}
.spacer {
  flex-grow: 1;
}
h1 {
  color: white;
  text-align: center;
}
</style>
