<template>
  <v-data-table
    :headers="headers"
    :items="enviados"
    item-key="name"
    class="elevation-1"
    :hide-default-footer="true"

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
            text: 'Viagem',
            align: 'start',
            sortable: false,
            value: 'viagem',
          },
          { text: 'Origem', value: 'pickupLocal' },
          { text: 'Destino', value: 'localDestino' },
          { text: 'Nrº Pessoas', value:'nrPessoas'},
          { text: 'Estado', value : 'aceite'}
        ],
        enviados: []
      }
    },
    created(){
      this.$request('get','pedido/todos/enviado/' + this.username)
        .then((response)=>{
          this.enviados=response.data.Enviado
        }).catch((error)=>{
          console.log(error.response)
        })
    }
  }
</script>

