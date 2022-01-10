<template>
  <v-container class="my-5">
    <Header @clicked = "onClickHeader"></Header>
    <NavDraw ref="navdraw"></NavDraw>
    <v-layout justify-space-around row wrap >
             <v-flex xs10 sm10 md9 lg9>
                <v-card class="mt-2" flat >
                  <v-tabs v-model="tab"  show-arrows color="#7e380e">
                    <v-tab v-for="item in items"  :key="item.tab">
                     {{ item.tab }}
                    </v-tab>
                  </v-tabs>
                  <v-tabs-items v-model="tab">
        
                    <v-tab-item eager>
                      <FormProcurarViagens @clicked="changeTab"/>
                   </v-tab-item>

                    <v-tab-item eager>
                      <ViagensPorFiltro :viagens="viagens"/>
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
import FormProcurarViagens from "../components/FormProcurarViagens.vue"
import ViagensPorFiltro from "../components/ViagensPorFiltros.vue"


export default {
    name: "Search",
    components: {
        Header,
        Footer,
        NavDraw,
        FormProcurarViagens,
        ViagensPorFiltro
    },
     data() {
    return{
      tab: null,
      items: [
        { tab: 'Procurar Viagem',},
        { tab: 'Resultados'}],
      viagens:[],
      }

   },
   methods:{
     onClickHeader(){
       this.$refs.navdraw.fixNav()
     },
     changeTab(value){
        this.tab='Resultados'
        this.viagens=value
     }
   }
}
</script>

