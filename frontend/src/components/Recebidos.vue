<template>
  <v-data-table
    :headers="headers"
    :items="recebidos"
    :hide-default-footer="true"
    class="elevation-1"
  >
    <template v-slot:item.actions="{ item }">
      <div v-if="!item.aceite" class="text-center">
        <v-btn color="#7e380e" dark @click="sheet = !sheet"> Ver Pedido </v-btn>
        <v-bottom-sheet block max-width v-model="sheet">
          <v-sheet class="text-center" height="200px" v-model="sheet">
            <v-btn class="mt-6" text color="green" @click="aceitarPedido(item)">
              Aceitar
            </v-btn>
            <v-btn class="mt-6" text color="red" @click="con(item)">
              Rejeitar
            </v-btn>
            <div class="py-7">
              Pretende aceitar {{item.username}} como Passageiro?
            </div>
          </v-sheet>
        </v-bottom-sheet>
      </div>
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
          text: "Passageiro",
          align: "start",
          value: "username",
        },
        { text: "Viagem", value: "viagem" },
        { text: "Origem", value: "pickupLocal" },
        { text: "Destino", value: "localDestino" },
        { text: "Nrº Pessoas", value: "nrPessoas" },
        { text: "Estado", value: "estado" },
        { text: "", value: "actions"},
      ],
      recebidos: [],
      sheet: false,
    };
  },
  created() {
    this.$request("get", "pedido/todos/recebidoAceitar/" + this.username)
      .then((response) => {
        this.recebidos = response.data.Recebido;
      })
      .catch((error) => {
        console.log(error.response);
      });
  },
  methods: {
    con(item) {
      console.log(item);
      this.sheet = !this.sheet;
    },
    aceitarPedido(item){
      console.log(item)
      this.$request("put", "pedido/" + item.idPedido + "/aceitar")
      .then((response) => {
        console.log(response)
      })
      .catch((error) => {
        console.log(error.response);
      });
    }
  },
};
</script>
