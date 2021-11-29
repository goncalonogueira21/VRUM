<template>
  <v-container>
     <img src= "../assets/VRUM_logo.png" class="center" >
     <v-card class="d-flex justify-center mb-6" flat >
      <v-btn to="/auth" color="#7e380e" class="white--text">
      Login/Signup
    </v-btn> 
     </v-card> 
    <Footer class="mt-5"></Footer>
  </v-container>
</template>

<script>

import Footer from "../components/Footer.vue"


export default {
  name: "Home",

  components: {
      Footer
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
