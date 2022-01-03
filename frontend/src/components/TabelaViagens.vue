<template> 
  <v-card class="transparent">
    <v-data-table
      class="transparent"
      :headers="headers"
      :items="viagens"
      :page="page"
      :pageCount="numberOfPages"
      :hide-default-footer="true"
      :options.sync="options"
      sort-by="name"
    >
      
    </v-data-table>

  </v-card>
</template>

<script>
//import axios from 'axios'

export default {
  name: "Home",
  data: () => {
    return {
      itemid: 0,
      page: 1,
      totalItems: 0,
      numberOfPages: 0,
      loading: true,
      options: {},
      headers: [
        {
          text: "Utilizador",
          value: "user",
          sortable: false,
        },
        {
          text: "Origem",
          value: "origem",
        },
        {
          text: "Destino",
          value: "destino",
        },
        {
          text: "Data",
          value: "dataViagem",
        },
        {
          text: "Hora",
          value: "horaInicial",
        },
        {
          text: "Lugares Disponivel",
          value: "disponiveis",
        },
        {
          text: "Bagagem",
          value: "bagagem",
        },
        {
          text: "Preço",
          value:"preco"
        }
      ],
      viagens: [
          {
            user: 'User Teste',
            origem: 'Gualtar',
            destino: 'Azurem',
            dataViagem: '12/01/2022',
            horaInicial: '12:00',
            disponiveis: 3,
            bagagem: false,
            preco:'10'
          },{
            user: 'User Teste2',
            origem: 'Gualtar',
            destino: 'Azurem',
            dataViagem: '12/01/2022',
            horaInicial: '12:00',
            disponiveis: 3,
            bagagem: false,
            preco:'5'
          },
      ],
    };
  },
  /*created(){
    this.initialize()
  },
  methods: {
    initialize(){
      axios.get('http://localhost:5000/viagem/todas')
        .then((response)=>{

        })
        .catch((error)=> {
          console.log(error)
        })
    }
  }*/
};
</script>