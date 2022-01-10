<template>
  <v-data-table
    :headers="headers"
    :items="viagens"
    multiple-expand
    :expanded.sync="expanded"
    item-key="name"
    show-expand
    class="elevation-1"
  >
    
    <template v-slot:expanded-item="{ headers, item }">
      <td :colspan="headers.length">
        More info about {{ item.name }}
      </td>
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
        expanded: [],
        singleExpand: true,
        headers: [
          {
            text: 'Data',
            align: 'start',
            sortable: false,
            value: 'data',
          },
          { text: 'Carro', value: 'carro' },
          { text: 'Origem', value: 'origem' },
          { text: 'Destino', value: 'destino' },
          { text: 'Ganho', value: 'ganho' },
          { text: '', value: 'data-table-expand' }
        ],
        viagemDefault:{
            carro: '',
            origem:'',
            destino:'',
            data:'',
            ganho:''
        },
        viagens: []
      }
    },
    created(){
      this.$request('get','viagem/condutor/' + this.username)
        .then((response)=>{
          this.viagens=response.data.Viagens
        }).catch((error)=>{
          console.log(error.response)
        })
    }
  }
</script>

