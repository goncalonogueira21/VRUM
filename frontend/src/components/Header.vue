<template>
  <v-app-bar app color="#7e380e" height="80" clipped-left>
    <v-app-bar-nav-icon @click.stop="openNavDraw"></v-app-bar-nav-icon>

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
          <v-list-item-title> {{username}} </v-list-item-title>
        </v-list-item-content>
      </v-list-item>
    </v-list-item-group>
  </v-app-bar>
</template>

<script>
import {mapState} from "vuex"

export default {
  computed: mapState({
      username: state => state.auth.username
    }),
  data() {
    return {
      parametro: "",
      drawer: false,
      group: null,
    };
  },
  methods: {
   
    openNavDraw() {
      this.drawer = !this.drawer
      this.$emit('clicked',this.drawer)
    }
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
