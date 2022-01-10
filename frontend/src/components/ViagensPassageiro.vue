<template>
  <v-data-table
    :headers="headers"
    :items="viagens"
    item-key="Data"
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
            text: 'Data',
            align: 'start',
            sortable: false,
            value: 'dataInicio',
          },
          { text: 'Condutor', value: 'idCondutor' },
          { text: 'Carro', value: 'matricula' },
          { text: 'Origem', value: 'localInicio' },
          { text: 'Destino', value: 'localDestino' },
          { text: 'Custo', value: 'custoGanho' }
        ],
        viagens: []
      }
    },
    created(){
      this.$request('get','viagem/todos/passageiro/' + this.username)
        .then((response)=>{
          this.viagens=response.data.Viagem
        }).catch((error)=>{
          console.log(error.response)
        })
    }
  }
</script>

