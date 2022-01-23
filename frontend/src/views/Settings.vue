<template>
  <v-container class="my-5">
    <Header @clicked="onClickHeader"></Header>
    <NavDraw ref="navdraw"></NavDraw>
    <div>
      <h1 class="pa-md-4 mx-lg-auto text-center">Definições</h1>
    </div>
    <v-card class="mx-auto pa-5" max-width="344" outlined elevation="1">
          <v-row justify="center" align="top">
            <v-col
              ><span class="text-h6 overline mb-1">
                Notificações
              </span></v-col
            >
            <v-col >
                <v-switch dense hide-details v-model="switch1"></v-switch>
            </v-col>
          </v-row>
    </v-card>
        <v-card class="mx-auto pa-5" max-width="344" outlined elevation="1">
          <v-row justify="center" align="top">
            <v-col
              ><span class="text-h6 overline mb-1">
                Settings 2
              </span></v-col
            >
            <v-col >
                <v-switch dense hide-details v-model="switch2"></v-switch>
            </v-col>
          </v-row>
    </v-card>
            <v-card class="mx-auto pa-5" max-width="344" outlined elevation="1">
          <v-row justify="center" align="top">
            <v-col
              ><span class="text-h6 overline mb-1">
                Settings 3
              </span></v-col
            >
            <v-col >
                <v-switch dense hide-details v-model="switch3"></v-switch>
            </v-col>
          </v-row>
    </v-card>
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
    return {
      switch1: true,
      switch2: true,
      switch3: true,
    };
  },
  methods: {
    onClickHeader() {
      this.$refs.navdraw.fixNav();
    },
  },
};


</script>
