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
      :custom-sort="customSort"
    >

    <template v-slot:item.id="{ item }">
          <a :href="`/viagem/${item.id}`"> Mostrar Viagem </a>
      </template>
    </v-data-table>
      

  </v-card>
</template>

<script>

export default {
  name: "TabelaViagens",
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
          text: "Data",
          value: "dataInicio",
          align: "start",
          sortDesc: true
        },
        {
          text: "Hora",
          value: "horaInicio",
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
          text: "Lugares Disponivel",
          value: "lugaresDisp",
        },
        {
          text: "Bagagem",
          value: "bagagem"
        },
        {
          text: "Custo por Pessoa",
          value:"custoPessoa"
        },
        {
          text: "Está interessado?",
          value: "id",
          sortable: false,
        },
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
    customSort(items, index, isDesc) {
        items.sort((a, b) => {
          if (isDesc != "false") {
            return a[index] < b[index] ? -1 : 1
          } else {
            return b[index] < a[index] ? -1 : 1
          }
        })
        return items
      },

  }
};
</script>