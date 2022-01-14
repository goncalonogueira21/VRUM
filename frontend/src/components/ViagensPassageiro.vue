<template>
  <v-data-table
    :headers="headers"
    :items="viagens"
    sort-by="Data"
    class="elevation-1"
  >
    <template v-slot:top>
      <v-toolbar
        flat
      >
        
        <v-dialog v-model="dialogRate" max-width="1000px">
          <v-card>
            <v-card-title class="text-h5" >Classificação de Condutor</v-card-title>
            <v-card-text>
              <v-container>
                <v-row>
                  <v-col cols="12" sm="6" md="4">
                      <v-text-field v-model="formRating.idViagem" readonly label="Viagem"/>
                      
                  </v-col>
                  <v-col cols="12" sm="6" md="4">
                     <v-text-field v-model="formRating.condutor" readonly label="Condutor"/> 
                  </v-col>
                  <v-col cols="12" sm="6" md="4">
                      <v-rating
                        background-color="grey"
                        color="brown"
                        length="5"
                        size="20"
                        class="mr-4"
                        v-model="formRating.rating"
                      ></v-rating>
                  </v-col>
                </v-row>
              </v-container>
            </v-card-text>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="#7e380e" text @click="closeRate">Cancel</v-btn>
              <v-btn color="#7e380e" text @click="rateUserConfirm">Confirm</v-btn>
              <v-spacer></v-spacer>
            </v-card-actions>
          </v-card>
        </v-dialog>
      </v-toolbar>
    </template>
    <template v-slot:item.actions="{ item }">
      <v-icon
        class="ml-2"
        color='#7e380e'
        @click="rateUser(item)"
      >
        mdi-star
      </v-icon>
    </template>
    
  </v-data-table>
</template>

<script>
import {mapState} from "vuex"

 export default {
      computed: mapState({
      username: state => state.auth.username
    }),
    data () {
      return {
        dialogRate: false,
        search:'',
        headers: [
          {
            text: 'Data',
            align: 'start',
            sortable: false,
            value: 'dataInicio',
          },
          { text: 'Condutor', value: 'condutor' },
          { text: 'Carro', value: 'matricula' },
          { text: 'Origem', value: 'localInicio' },
          { text: 'Destino', value: 'localDestino' },
          { text: 'Custo', value: 'custo' },
          { text: 'Classificar', value: 'actions', sortable: false}
        ],
        viagens: [],
        formRating:{
          idViagem: '',
          condutor:'',
          rating:''
        }

      }
    },
     watch: {
      dialogRate (val) {
        val || this.closeRate()
      },
    },
    created(){
      this.$request('get','viagem/todos/passageiro/' + this.username)
        .then((response)=>{
          this.viagens=response.data.Viagem
        }).catch((error)=>{
          console.log(error.response)
        })
    },
    methods:{
      closeRate () {
        this.dialogRate = false
      },
      rateUser(item) {
        this.formRating.idViagem = item.idViagem,
        this.formRating.condutor= item.condutor,
        this.dialogRate = true
      },
      rateUserConfirm() {
         var payload = new FormData();
         payload.append('rating', this.formRating.rating);
         payload.append('username', this.username)
        this.$request('post','avaliacao/'+ this.formRating.idViagem,payload)
            .then((response) =>{
              console.log(response)
            }).catch((error)=>{
              console.log(error)
            })
        this.closeRate()
    }
  }
 }
</script>

