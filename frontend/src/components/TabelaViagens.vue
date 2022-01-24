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

import { mapState } from "vuex";

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
          sortDesc: true,
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
          value: "bagagem",
        },
        {
          text: "Custo por Pessoa",
          value: "custoPessoa",
        },
        {
          text: "Está interessado?",
          value: "id",
          sortable: false,
        },
      ],
      viagens: [],
    };
  },
  created() {
    this.initialize();
  },
  computed: mapState({
    username: (state) => state.auth.username,
  }),
  methods: {
    initialize() {
      this.$request("get", "viagem/todos")
        .then((response) => {
          for (let i = 0; i < response.data.Viagens.length; i++) {
            if (response.data.Viagens[i].estado == "Agendada") {
              this.viagens.push(response.data.Viagens[i]);
            }

            if (
              response.data.Viagens[i].estado == "A decorrer" &&
              response.data.Viagens[i].idCondutor == this.username
            ) {
              this.viagens.push(response.data.Viagens[i]);
            }
            // this.$request("get", "pedido/todos")
            //   .then((response2) => {
            //       console.log(response2.data.Pedidos)
            //       for(let j = 0; j < response2.data.Pedidos.length; j++){
            //         if(response2.data.Pedidos[j].viagem == response.data.Viagens[i].idViagem && 
            //            response2.data.Pedidos[j].username == this.username){
            //              this.viagens.push(response.data.Viagens[i]);
            //         }
            //       }
            //   })
            //   .catch((error) => {
            //     console.log(error);
            //   });
          }
        })
        .catch((error) => {
          console.log(error);
        });
    },
    pushOtherPage() {
      this.$router.push({ name: "Viagem" });
    },
    customSort(items, index, isDesc) {
      items.sort((a, b) => {
        if (isDesc != "false") {
          return a[index] < b[index] ? -1 : 1;
        } else {
          return b[index] < a[index] ? -1 : 1;
        }
      });
      return items;
    },
  },
};
</script>
