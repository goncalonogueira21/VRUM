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

    <template v-slot:item.id="{ item }">
          <div style="cursor: pointer" @click.stop="pushOtherPage">{{ item.id }}</div>
      </template>
      
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
          text: "ID Viagem",
          value: "id",
          sortable: false,
        },
        {
          text: "Condutor",
          value: "idCondutor",
          sortable: false,
        },
        {
          text: "Carro",
          value: "username",
          sortable: false,
        },
        {
          text: "Origem",
          value: "localInicio",
        },
        {
          text: "Destino",
          value: "localDestino",
        },
        {
          text: "Data",
          value: "dataInicio",
        },
        {
          text: "Hora",
          value: "horaInicial",
        },
        {
          text: "Lugares Disponivel",
          value: "lugaresDisp",
        },
        {
          text: "Bagagem",
          value: "bagagem",
        },
        {
          text: "Custo por Pessoa",
          value:"custoPessoa"
        }
      ],
      viagens: [],
      // viagem: [
      //   {
      //     'id': viagem.idViagem,
      //     'username': viagem.fk_Carro_matricula,
      //     'dataInicio': viagem.dataInicio,
      //     'kmsViagem': viagem.kmsViagem,
      //     'custoPessoa': viagem.custoPessoa,
      //     'localInicio':viagem.localInicio,
      //     'bagagem':viagem.bagagem,
      //     'localDestino': viagem.localDestino,
      //     'nrLugares': viagem.nrLugares,
      //     'lugaresDisp': viagem.lugaresDisp,
      //     'regularidade': viagem.regularidade,
      //     'idCondutor': viagem.idCondutor,
      //     'descricao': viagem.descricao,
      //     'estado': viagem.estado,
      //   },
      // ],
    };
  },
  created () {
      this.initialize()
    },
  methods: {
    initialize () {
        this.$request("get","viagem/todos")
            .then((response)=>{
              this.viagens=response.data.Viagens
            }).catch((error)=>{
              console.log(error)
            })
    },
    pushOtherPage() {
      this.$router.push({ name: 'Viagem' });
    },

  }
};
</script>