<template>
  <v-container class="my-5">
    <Header @clicked = "onClickHeader"></Header>
    <NavDraw ref="navdraw"></NavDraw>
    <v-layout justify-space-around row wrap >
             <v-flex xs10 sm10 md9 lg9>
                <v-card class="mt-2" flat >
                  <v-tabs v-model="tab"  show-arrows color="#7e380e">
                    <v-tab v-for="item in items" :key="item.tab">
                     {{ item.tab }}
                    </v-tab>
                  </v-tabs>
                  <v-tabs-items v-model="tab">
        
                    <v-tab-item eager>
                      <FormCriarViagem ref="criarviagem"/>
                   </v-tab-item>

                  
                  

                 </v-tabs-items>
              </v-card>
              
              

        </v-flex>
    </v-layout> 
  
    <Footer></Footer>
</v-container>
</template>

<script>
import Header from "../components/Header.vue"
import Footer from "../components/Footer.vue"
import NavDraw from "../components/NavDraw.vue"
import FormCriarViagem from "../components/FormCriarViagem.vue"


export default {
    name: "Search",
    components: {
        Header,
        Footer,
        NavDraw,
        FormCriarViagem
    },
     data() {
    return{
      tab: null,
      openHelp: false,
      items: [
        { tab: 'Inserir Viagem'}
      ]}
   },
   methods:{
     reset(){
       this.$refs.criarviagem.reset()
     },
     onClickHeader(){
       this.$refs.navdraw.fixNav()
     }
   },

   
}
</script>
