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
              
              <v-card class="mx-auto" flat>
                <v-row class="px-2 pb-2 ma-0 py-2" justify="space-between">
                    
                <v-btn-toggle v-model="alignment"
                    dense class="ml-5 mr-5 mb-3"  >
                    <v-btn color="#2A3F54" class="ml-2" elevation="5" @click="help">
                      <v-icon color="white">mdi-help</v-icon>
                    </v-btn>

                    <v-dialog v-model="openHelp" max-width="500px">
                      <v-card color="white">
                        <v-card-title >
                          <p>
                            Ajuda
                          </p>
                        </v-card-title>
                        <v-card-text>
                          asdasdas
                        </v-card-text>
                        <v-card-actions>
                          <v-btn @click="closeHelp" color="#2A3F54">
                            <v-icon color="white">mdi-close</v-icon>
                          </v-btn>  
                        </v-card-actions>

                      </v-card>
                        
                    </v-dialog>
                </v-btn-toggle>

                <v-btn-toggle v-model="formatting" multiple dense class="ml-4 mb-3"  >
                    <v-btn @click="submit" color="#F0B62B" elevation="5" class="ml-2 mr-2">
                      <v-icon color="white">mdi-checkbox-marked-outline</v-icon>
                      
                    </v-btn>

                   

                    <v-btn color="#29E898" elevation="5" @click="reset">
                      <v-icon color="white">mdi-broom</v-icon>
                    </v-btn>
                  </v-btn-toggle>
                </v-row>

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
     }
   },
     onClickHeader(){
       this.$refs.navdraw.fixNav()
     }
   
}
</script>
