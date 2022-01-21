<template>
  <v-data-table
    :headers="headers"
    :items="viagens"
    class="elevation-1"
    :custom-sort="customSort"
  >
    <template v-slot:item.id="{ item }">
      <a :href="`/viagem/${item.id}`"> Mostrar Viagem </a>
    </template>
  </v-data-table>
</template>

<script>
import { mapState } from "vuex";

export default {
  computed: mapState({
    username: (state) => state.auth.username,
  }),
  data() {
    return {
      headers: [
        {
          text: "Data",
          align: "start",
          sortable: false,
          value: "dataInicio",
        },
        { text: "Carro", value: "matricula" },
        { text: "Origem", value: "localInicio" },
        { text: "Destino", value: "localDestino" },

        {
          text: "Viagem",
          value: "id",
          sortable: false,
        },
        //{ text: 'Ganho', value: 'custoGanho' }
      ],
      viagens: [],
    };
  },
  created() {
    this.$request("get", "viagem/todos/condutor/" + this.username)
      .then((response) => {
        this.viagens = response.data.Viagem;
      })
      .catch((error) => {
        console.log(error.response);
      });
  },
  methods: {
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
