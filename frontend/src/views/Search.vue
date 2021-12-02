<template>
  <v-container class="my-5">
      <Header></Header>
      <TabsWrapper></TabsWrapper>
      <Footer></Footer>
</v-container>
</template>

<script>
import Header from "../components/Header.vue"
import Footer from "../components/Footer.vue"
import TabsWrapper from "../components/tabsWrapper.vue" 

export default {
    name: "Search",
    components: {
        Header,
        Footer,
        TabsWrapper
    }
}
</script>

