<template>
  <v-container class ="my-5">
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
                      <ViagensCondutor/>
                   </v-tab-item>

                   <v-tab-item eager>
                      <ViagensPassageiro/>
                   </v-tab-item>
                  

                 </v-tabs-items>
              </v-card>
              
              

        </v-flex>
    </v-layout> 
      <Footer></Footer>
  </v-container>
</template>

<script>
import Footer from "../components/Footer.vue"
import Header from "../components/Header.vue"
import NavDraw from "../components/NavDraw.vue" 
import ViagensCondutor from "../components/ViagensCondutor.vue"
import ViagensPassageiro from "../components/ViagensPassageiro.vue"


export default {
    name: "HistoricoViagens",

     components: {
      Footer,Header,NavDraw, ViagensCondutor, ViagensPassageiro
  },
  data() {
    return{
      tab: null,
      items: [
        { tab: 'Viagens como condutor'},
        { tab: 'Viagens como passageiro'}
      ]}
   },
   methods:{
     onClickHeader(){
       this.$refs.navdraw.fixNav()
     }
   }
}
</script>
