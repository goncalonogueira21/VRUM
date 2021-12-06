<template>
  <v-container>
      <Header></Header>
      
      <Footer></Footer>
  </v-container>
</template>

<script>
import Footer from "../components/Footer.vue"
import Header from "../components/Header.vue"

export default {
    name: "Profile",

     components: {
      Footer,Header
  },
}
</script>
