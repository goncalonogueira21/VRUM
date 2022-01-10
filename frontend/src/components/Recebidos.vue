<template>
  <v-data-table
    :headers="headers"
    :items="recebidos"
    item-key="name"
    class="elevation-1"
  >
    
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
        headers: [
          {
            text: 'Passageiro',
            align: 'start',
            sortable: false,
            value: 'username',
          },
          { text: 'Viagem', value: 'viagem' },
          { text: 'Origem', value: 'pickupLocal'},
          { text: 'Destino', value: 'localDestino'},
          { text: 'Nrº Pessoas', value:'nrPessoas'},
          { text: 'Estado', value : 'aceite'}
        ],
        recebidos: []
      }
    },
    created(){
      this.$request('get','pedido/todos/recebido/' + this.username)
        .then((response)=>{
          this.recebidos=response.data.Recebido
        }).catch((error)=>{
          console.log(error.response)
        })
    }
  }
</script>

