<template>
  <v-container class="my-5">
      <Header></Header>
      <div>
        <NavDraw></NavDraw>
      </div>
      <Footer></Footer>
</v-container>
</template>

<script>
import Header from "../components/Header.vue"
import Footer from "../components/Footer.vue"
import NavDraw from "../components/NavDraw.vue"

export default {
    name: "Search",
    components: {
        Header,
        Footer,
        NavDraw
    }
}
</script>

