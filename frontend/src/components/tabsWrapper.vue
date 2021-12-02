<template>
    <v-layout justify-space-around row wrap >
             <v-flex xs10 sm10 md9 lg9>
                <v-card class="mt-2" elevation="10" >
                  <v-tabs v-model="tab"  show-arrows>
                    <v-tab v-for="item in items" :key="item.tab">
                     {{ item.tab }}
                    </v-tab>
                  </v-tabs>
                  <v-tabs-items v-model="tab">
                   <v-tab-item eager> 
                      
                   </v-tab-item>
                   <v-tab-item eager>
                      <FormCriarViagem/>
                   </v-tab-item>
                 </v-tabs-items>
              </v-card>
              
              <v-card class="mx-auto" >
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
                            Gestão de Questões
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
</template>

<script>
import FormCriarViagem from "../components/FormCriarViagem.vue"

export default {
    name:"tabsWrpper",
    components:{
        FormCriarViagem
    },
   data() {
    return{
      tab: null,
      openHelp: false,
      items: [
        { tab: 'Procurar Viagem'},
        { tab: 'Inserir Viagem'}
      ]}
   }
}

</script>
