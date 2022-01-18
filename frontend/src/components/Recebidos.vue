<template>
  <v-data-table
    :headers="headers"
    :items="recebidos"
    :hide-default-footer="true"
    class="elevation-1"
    :custom-sort="customSort"
  >
    <template v-slot:item.actions="{ item }">
      <div v-if="item.estado!= 'Aceite'" class="text-center">
        <v-btn color="#7e380e" dark @click="verPedido(item)"> Ver Pedido </v-btn>
        <v-bottom-sheet max-width v-model="sheet">
          <v-sheet class="text-center" height="200px">
            <v-btn class="mt-6" text color="green" @click="aceitarPedido(item)">
              Aceitar
            </v-btn>
            <v-btn class="mt-6" text color="red" @click="rejeitarPedido(item)">
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
          text: "Data",
          align: "start",
          value: "data",
        },
        {text: "Passageiro",value: "username"},
        { text: "Viagem", value: "viagem" },
        { text: "Origem", value: "pickupLocal" },
        { text: "Destino", value: "localDestino" },
        { text: "Nrº Pessoas", value: "nrPessoas" },
        { text: "Estado", value: "estado" },
        { text: "", value: "actions"},
      ],
      recebidos: [],
      sheet: false,
      editedIndex: -1,
      editedItem: {
        data: '',
        username: '',
        viagem: '',
        pickupLocal: '',
        localDestino: '',
        nrPessoas: '',
        estado: ''
      },
      defaultItem: {
        data: '',
        username: '',
        viagem: '',
        pickupLocal: '',
        localDestino: '',
        nrPessoas: '',
        estado: ''
      },
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
    con(item) {
      console.log(item);
      this.sheet = !this.sheet;
    },

    verPedido(item){
      var payload = new FormData();
      payload.append("notificacao", 0);
      
      this.$request("put", "pedido/" + item.idPedido + "/update",payload)
        .then((response) => {
          console.log(response.data);
          this.sheet= !this.sheet
        })
        .catch((error) => {
          console.log(error);
        });
        this.editedIndex = this.carros.indexOf(item)
        this.editedItem = Object.assign({}, item)
    },
    aceitarPedido(item){
      this.$request("put", "pedido/" + item.idPedido + "/aceitar")
        .then((response) => {
          console.log(response.data);
          this.sheet= !this.sheet
        })
        .catch((error) => {
          console.log(error);
        });
        if (this.editedIndex > -1) {
          Object.assign(this.carros[this.editedIndex], this.editedItem)
        } else {
          this.carros.push(this.editedItem)
        }
    },
    rejeitaPedido(item){
        var payload = new FormData();
        payload.append("notificacao", 1);
        payload.append('estado', 'Rejeitado')
      
      this.$request("put", "pedido/" + item.idPedido + "/update",payload)
        .then((response) => {
          console.log(response.data);
          this.sheet= !this.sheet
          this.$router.go();
        })
        .catch((error) => {
          console.log(error);
        });
    }
  },
};
</script>
