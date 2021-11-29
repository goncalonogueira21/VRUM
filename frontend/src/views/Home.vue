<template>
  <v-container>
     <img src= "../assets/VRUM_logo.png" class="center" >
      <v-btn to="/auth" color="#7e380e" class="white--text">
      Login/Signup
    </v-btn>  
    <Footer class="mt-5"></Footer>
  </v-container>
</template>

<script>

import Footer from "../components/Footer.vue"
//import Header from "../components/Header.vue"

export default {
  name: "Home",

  components: {
      Footer //,Header
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
