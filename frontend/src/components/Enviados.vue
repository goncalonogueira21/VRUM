<template>
  <v-data-table
    :headers="headers"
    :items="enviados"
    item-key="name"
    class="elevation-1"
    :hide-default-footer="true"
    :custom-sort="customSort"

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
          {text: 'Data',align: 'start', value:'data'},
          {text: 'Viagem',value: 'viagem'},
          { text: 'Origem', value: 'pickupLocal' },
          { text: 'Destino', value: 'localDestino' },
          { text: 'Nrº Pessoas', value:'nrPessoas'},
          { text: 'Estado', value : 'estado'}
        ],
        enviados: []
      }
    },
    created(){
      this.$request('get','pedido/todos/enviado/' + this.username)
        .then((response)=>{
          console.log(response.data.Enviado)
          this.enviados=response.data.Enviado
        }).catch((error)=>{
          console.log(error.response)
        })
    },
    methods:{
      customSort(items, index, isDesc) {
        items.sort((a, b) => {
          if (isDesc != "false") {
            return a[index] < b[index] ? -1 : 1
          } else {
            return b[index] < a[index] ? -1 : 1
          }
        })
        return items
      }
    }
  }
</script>

