<template>
  <v-container>
    <v-card class="d-flex justify-center mb-6" flat>
      <img src="../assets/VRUM_logo.png" />
    </v-card>
    <v-card class="d-flex justify-center mb-6" flat>
      <v-btn to="/auth" color="#7e380e" class="white--text"> Entrar </v-btn>
    </v-card>

    <v-card class="center">
      <h1>My coords</h1>
      <p>{{ coordinates.lat }} : {{ coordinates.lng }}</p>
    </v-card>
  </v-container>
</template>

<script>
export default {
  name: "Home",

  data() {
    return {
    };
  },

  computed: {
    currentRouteName() {
      console.log(this.$route.name);
      return this.$route.name;
    },
  },
};
</script>

<style>
.center {
  display: block;
  margin-left: auto;
  margin-right: auto;
  width: 50%;
}
</style>
