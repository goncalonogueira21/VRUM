<template>
  <v-container class="my-5">
    <Header @clicked="onClickHeader"></Header>
    <NavDraw ref="navdraw"></NavDraw>
    <v-alert
      :value="alertPedidoFeito"
      transition="slide-y-transition"
      dense
      color="dark green"
      dismissible
      type="success"
      @input="alertPedidoFeito = false"
    >
      Pedido enviado
    </v-alert>
    <v-alert
      :value="alertPedidoCancelado"
      transition="slide-y-transition"
      dense
      color="dark green"
      dismissible
      type="success"
      @input="alertPedidoCancelado = false"
    >
      Pedido cancelado
    </v-alert>
    <v-alert
      :value="alertErro"
      transition="slide-y-transition"
      dense
      color="dark red"
      dismissible
      type="error"
      @input="alertErro = false"
    >
      Erro!
    </v-alert>
    <v-alert
      :value="alertViagemEditada"
      transition="slide-y-transition"
      dense
      color="dark green"
      dismissible
      type="success"
      @input="alertViagemEditada = false"
    >
      Viagem Editada
    </v-alert>
    <v-alert
      :value="alertViagemEliminada"
      transition="slide-y-transition"
      dense
      color="dark green"
      dismissible
      type="success"
      @input="alertViagemEliminada = false"
    >
      Viagem Eliminada
    </v-alert>
    <v-card class="mx-auto" max-width="344" outlined elevation="5">
      <v-list-item three-line>
        <v-list-item-content>
          <v-list-item-title class="text-h6 overline mb-1">
            Partida: {{ viagem.localInicio }}
          </v-list-item-title>
          <v-list-item-title class="text-h6 overline mb-1">
            Destino: {{ viagem.localDestino }}
          </v-list-item-title>

          <v-list-item-title class="text-h6 overline mb-1">
            Condutor: {{ viagem.idCondutor }}
          </v-list-item-title>

          <div class="text-overline mb-4">
            Lugares Disponíveis: {{ viagem.lugaresDisp }}
          </div>
          <div class="text-overline mb-4">
            Permite Bagagem: {{ viagem.bagagem ? "Sim" : "Não" }}
          </div>

          <div class="text-overline mb-4">
            Custo da Viagem: {{ viagem.custoPessoa }}€
          </div>

          <v-list-item-subtitle
            >Data e Hora: {{ viagem.dataInicio }} {{ viagem.horaInicio }}
          </v-list-item-subtitle>
          <v-spacer></v-spacer>
          <v-div v-if="viagem.descricao || viagem.descricao == 'null'">
            <v-list-item-subtitle
              >Descrição: {{ viagem.descricao }}
            </v-list-item-subtitle>
          </v-div>
        </v-list-item-content>
      </v-list-item>

      <v-spacer></v-spacer>
      <v-div v-if="aceites[0]">
        <v-list subheader>
          <v-subheader>Utilizadores Aceites</v-subheader>

          <v-list-item v-for="pedido in aceites" :key="pedido.username">
            <!-- <v-list-item-avatar>
          <v-img
            :alt="`${user.foto} avatar`"
            :src="chat.avatar"
          ></v-img>
        </v-list-item-avatar> -->

            <v-list-item-content>
              <v-list-item-title v-text="pedido.username"></v-list-item-title>
            </v-list-item-content>

            <v-list-item-icon>
              <v-icon :color="pediddo.active ? 'deep-purple accent-4' : 'grey'">
                mdi-message-outline
              </v-icon>
            </v-list-item-icon>
          </v-list-item>
        </v-list>
      </v-div>

      <div class="text-center">
        <!-- Butões de Passageiro SEM Pedido -->
        <div v-if="this.username != viagem.idCondutor && !this.pedido && !this.pedidoAceite">
          <v-btn
            class="ma-2"
            color="success"
            outlined
            @click="registarPassageiro"
          >
            Registar na viagem
            <v-icon right> mdi-account-check-outline </v-icon>
          </v-btn>
        </div>

        <!-- Butões de Passageiro COM Pedido -->
        <div v-else-if="this.username != viagem.idCondutor && pedido">
          <v-btn class="ma-2" color="primary" outlined @click="todoEnviarMsg">
            Enviar Mensagem
            <v-icon right> mdi-android-messages </v-icon>
          </v-btn>
          <!-- Pedido Aceite -->
          <v-div v-if="pedidoAceite">
            <v-btn
              disabled
              class="ma-2"
              color="red"
              outlined
              @click="deletePassageiro"
            >
              Cancelar Pedido
              <v-icon right> mdi-delete-outline </v-icon>
            </v-btn>
          </v-div>
          <!-- Pedido por aceitar -->
          <v-div v-else>
            <v-btn class="ma-2" color="red" outlined @click="deletePassageiro">
              Cancelar Pedido
              <v-icon right> mdi-delete-outline </v-icon>
            </v-btn>
          </v-div>
        </div>


        <!-- Butões de Condutor  -->
        <v-div
          v-else-if="
            this.username == viagem.idCondutor && viagem.estado == 'Agendada'
          "
        >
          <v-btn class="ma-2" color="success" outlined @click="startViagem">
            Iniciar viagem
            <v-icon right> mdi-play-circle-outline </v-icon>
          </v-btn>
          <v-btn
            class="ma-2"
            color="orange"
            outlined
            pill
            @click="dialog = !dialog"
          >
            Editar Viagem
            <v-icon right> mdi-pencil-outline </v-icon>
          </v-btn>

          <v-btn
            class="ma-2"
            color="red"
            outlined
            pill
            @click="dialogDelete = !dialogDelete"
          >
            Eliminar Viagem
            <v-icon right> mdi-delete-outline </v-icon>
          </v-btn>
        </v-div>
        <!-- Butões de Condutor depois de iniciar viagem  -->
        <v-div v-if="viagem.estado == 'A decorrer' && this.username == viagem.idCondutor">
          <v-btn class="ma-2" color="red" outlined pill @click="terminarViagem">
            Terminar Viagem {{this.username}} {{viagem.idCondutor}}
            <v-icon right> mdi-delete-outline </v-icon>
          </v-btn>
        </v-div>
        <v-div v-if="viagem.estado == 'Finalizada'">
          <h3>Viagem Terminada</h3>
        </v-div>
      </div>

      <!-- Dialog de Delete -->
      <v-dialog v-model="dialogDelete" max-width="500px">
        <v-card>
          <v-card-title color="#7e380e" class="text-h5"
            >Tem a certeza que quer eliminar a viagem?</v-card-title
          >
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="#7e380e" text @click="dialogDelete = !dialogDelete"
              >Cancel</v-btn
            >
            <v-btn color="#7e380e" text @click="eliminarViagem">Eliminar</v-btn>
            <v-spacer></v-spacer>
          </v-card-actions>
        </v-card>
      </v-dialog>

      <!-- Dialog de Editar Viagem -->
      <v-dialog v-model="dialog" max-width="800px">
        <v-card>
          <v-card-title>
            <span class="text-h5"> Editar Viagem </span>
          </v-card-title>

          <v-card-text>
            <v-container>
              <!-- <v-row>
        <v-col cols="11">
          <v-select
            height="44px"
            v-model="formData.fk_Carro_matricula"
            clear
            :rules="rules.required"
            :items="carros.map((carro) => carro.matricula)"
            label="Escolher Viatura"
            dense
          />
        </v-col>
      </v-row> -->
              <v-row>
                <v-col cols="11" md="5">
                  <v-text-field
                    v-model="viagem.localInicio"
                    id="autocomplete"
                    :rules="[...rules.required, ...rules.length30]"
                    :counter="30"
                    label="Ponto de Partida"
                  />
                </v-col>
                <v-spacer></v-spacer>
                <v-col cols="11" md="5">
                  <v-text-field
                    v-model="viagem.localDestino"
                    :rules="[...rules.required, ...rules.length30]"
                    :counter="30"
                    label="Ponto de Chegada"
                  />
                </v-col>
              </v-row>
              <v-row>
                <v-col cols="11" sm="5">
                  <v-menu
                    ref="menu"
                    v-model="menu"
                    :close-on-content-click="false"
                    :return-value.sync="viagem.dataInicio"
                    transition="scale-transition"
                    offset-y
                    min-width="auto"
                  >
                    <template v-slot:activator="{ on, attrs }">
                      <v-text-field
                        :rules="rules.required"
                        v-model="viagem.dataInicio"
                        label="Data da viagem"
                        prepend-icon="mdi-calendar"
                        readonly
                        v-bind="attrs"
                        v-on="on"
                      ></v-text-field>
                    </template>
                    <v-date-picker
                      v-model="viagem.dataInicio"
                      no-title
                      scrollable
                    >
                      <v-spacer></v-spacer>
                      <v-btn text color="primary" @click="menu = false">
                        Cancel
                      </v-btn>
                      <v-btn
                        text
                        color="primary"
                        @click="$refs.menu.save(viagem.dataInicio)"
                      >
                        OK
                      </v-btn>
                    </v-date-picker>
                  </v-menu>
                </v-col>
                <v-spacer></v-spacer>
                <v-col cols="11" sm="5">
                  <v-menu
                    ref="menuTime"
                    v-model="menuTime"
                    :close-on-content-click="false"
                    :nudge-right="40"
                    :return-value.sync="viagem.horaInicio"
                    transition="scale-transition"
                    offset-y
                    max-width="290px"
                    min-width="290px"
                  >
                    <template v-slot:activator="{ on, attrs }">
                      <v-text-field
                        :rules="rules.required"
                        v-model="viagem.horaInicio"
                        label="Hora de Ínicio"
                        prepend-icon="mdi-clock-time-four-outline"
                        readonly
                        v-bind="attrs"
                        v-on="on"
                      ></v-text-field>
                    </template>
                    <v-time-picker
                      v-if="menuTime"
                      v-model="viagem.horaInicio"
                      full-width
                      @click:minute="$refs.menuTime.save(viagem.horaInicio)"
                    ></v-time-picker>
                  </v-menu>
                </v-col>
              </v-row>
              <v-row>
                <v-col cols="11" md="5">
                  <v-select
                    height="44px"
                    v-model="viagem.lugaresDisp"
                    clear
                    :rules="rules.required"
                    :items="lugares"
                    label="Lugares Disponíveis"
                    dense
                  />
                </v-col>

                <v-spacer />
                <v-col cols="11" md="5">
                  <v-text-field
                    v-model="viagem.regularidade"
                    :rules="rules.length30"
                    :counter="30"
                    label="Regularidade"
                  />
                </v-col>
              </v-row>
              <v-row>
                <v-col cols="11" md="5">
                  <v-text-field
                    v-model="viagem.custoPessoa"
                    label="Custo mínimo por pessoa"
                  />
                </v-col>
                <v-spacer />
                <v-col cols="11" md="5">
                  <v-checkbox v-model="viagem.bagagem" label="Bagagem" />
                </v-col>
              </v-row>
              <v-row>
                <v-col cols="12">
                  <v-text-field v-model="viagem.descricao" label="Descrição" />
                </v-col>
              </v-row>
            </v-container>
          </v-card-text>

          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="#7e380e" text @click="close"> Cancelar </v-btn>
            <v-btn color="#7e380e" text @click="editarViagem"> Guardar </v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </v-card>

    <!-- 
    <p>Mostrar dados da viagem</p>
    <p>Mostrar mapa da viagem</p>
    <p>Butoes para editar a viagem</p> 
    -->
  </v-container>
</template>

<script>
import Header from "../components/Header.vue";
import NavDraw from "../components/NavDraw.vue";
import { mapState } from "vuex";

export default {
  name: "Viagem",

  components: {
    Header,
    NavDraw,
  },

  data() {
    return {
      tab: null,
      viagem: {},
      dialog: false,
      dialogDelete: false,
      dialogTerminar: false,
      rules: {
        required: [(v) => !!v || "Field is required"],
        length30: [
          (v) =>
            (v && v.length <= 30) ||
            "Field must be less or equal than 30 characters",
        ],
        length75: [
          (v) =>
            (v && v.length <= 75) ||
            "Field must be less or equal than 75 characters",
        ],
        length100: [
          (v) =>
            (v && v.length <= 100) ||
            "Field must be less or equal than 100 characters",
        ],
      },
      lugares: ["1", "2", "3", "4", "5", "6"],
      pedido: false,
      pedidoID: 0,
      pedidoAceite: false,
      aceites: [],
      alertPedidoFeito: false,
      alertPedidoCancelado: false,
      alertViagemEditada: false,
      alertViagemEliminada: false,
      alertErro: false,
    };
  },
  computed: mapState({
    username: (state) => state.auth.username,
  }),
  created() {
    this.initialize();
  },
  watch: {
    dialog(val) {
      val || this.close();
    },
    dialogDelete(val) {
      val || this.closeDelete();
    },
  },
  methods: {
    initialize() {
      this.$request("get", "viagem/" + this.$route.params.id)
        .then((response) => {
          this.viagem = response.data.Viagem[0];
        })
        .catch((error) => {
          console.log(error);
        });

      // Verifica se o user fez um pedido nesta viagem
      this.$request("get", "pedido/todos")
        .then((response) => {
          console.log("RESPONSE", response);
          response.data.Pedidos.map((pedido) => {
            console.log("ITEM", pedido);
            console.log("USER", this.username);
            if (
              pedido.viagem == this.viagem.id &&
              pedido.username == this.username
            ) {
              this.pedido = true;
              this.pedidoID = pedido.id;
            }

            if (pedido.estado == "Aceite" && pedido.viagem == this.viagem.id && pedido.username == this.username) {
              this.pedidoAceite = true;
              this.aceites.push(pedido);
              this.pedido = true;

            }
          });
        })
        .catch((error) => {
          console.log(error);
        });
    },

    registarPassageiro() {
      var payload = new FormData();
      payload.append("username", this.username);
      payload.append("idViagem", this.$route.params.id);
      payload.append("nrPessoas", 1);
      payload.append("pickupLocal", this.viagem.localInicio);
      payload.append("localDestino", this.viagem.localDestino);

      this.$request("post", "pedido/registo", payload)
        .then((response) => {
          console.log(response.data);
          this.alertPedidoFeito = true;
        })
        .catch((error) => {
          console.log(error);
          this.alertErro = true;
        });

      this.pedido = true;
    },

    deletePassageiro() {
      this.$request("delete", "pedido/" + this.pedidoID + "/remove")
        .then((response) => {
          console.log(response);
          this.alertPedidoCancelado = true;
        })
        .catch((error) => {
          console.log(error);
          this.alert = true;
        });
      this.pedido = false;
      this.pedidoID = 0;
    },

    editViagemDialog() {
      this.dialog = !this.dialog;
    },
    editarViagem() {
      var payload = new FormData();
      payload.append("lugaresDisp", this.viagem.lugaresDisp);
      payload.append("localInicio", this.viagem.localInicio);
      payload.append("fk_Carro_matricula", this.viagem.username);
      payload.append("localDestino", this.viagem.localDestino);
      payload.append("regularidade", this.viagem.regularidade);
      payload.append("dataInicio", this.viagem.dataInicio);
      payload.append("bagagem", this.viagem.bagagem ? 1 : 0);
      payload.append("horaInicio", this.viagem.horaInicio);
      payload.append("custoPessoa", this.viagem.custoPessoa);
      payload.append("kmsViagem", this.viagem.kmsViagem);
      payload.append("idCondutor", this.username);
      payload.append("descricao", this.viagem.descricao);
      console.log(this.viagem);

      this.$request("put", "viagem/" + this.viagem.id + "/update", payload)
        .then((response) => {
          console.log(response);
          this.dialog = !this.dialog;
          this.alertViagemEditada = true;
        })
        .catch((error) => {
          console.log(error);
          this.alertErro = true;
        });
    },
    startViagem() {
      var payload = new FormData();
      payload.append("estado", "A decorrer");
      this.$request("put", "viagem/" + this.viagem.id + "/update", payload)
        .then((response) => {
          console.log(response);
          this.$router.go();
        })
        .catch((error) => {
          console.log(error);
        });
    },
    eliminarViagem() {
      this.$request("delete", "viagem/" + this.$route.params.id + "/remove")
        .then((response) => {
          console.log(response);
          this.alertViagemEliminada = true;
        })
        .catch((error) => {
          console.log(error);
          this.alertErro = true;
        });
      this.dialogDelete = !this.dialogDelete;
    },
    terminarViagem() {
      var payload = new FormData();
      payload.append("estado", "Finalizada");
      this.$request("put", "viagem/" + this.viagem.id + "/update", payload)
        .then((response) => {
          console.log(response);
          this.$router.go();
        })
        .catch((error) => {
          console.log(error);
        });
    },
    // getCarros() {
    //   console.log("user", this.username);
    //   this.$request("get", "carro/" + this.username)
    //     .then((response) => {
    //       this.carros = response.data.Carros;
    //       console.log(this.carros);
    //     })
    //     .catch((error) => {
    //       console.log(error);
    //     });
    // },
    close() {
      this.dialog = false;
    },

    onClickHeader() {
      this.$refs.navdraw.fixNav();
    },
  },
};
</script>
