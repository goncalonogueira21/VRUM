<template>
  <v-container class="my-5">
    <Header @clicked="onClickHeader"></Header>
    <NavDraw ref="navdraw"></NavDraw>

    <v-card class="mx-auto" max-width="344" outlined elevation="5"
>
      <v-list-item three-line>
        <v-list-item-content>
          <!-- 'username': viagem.fk_Carro_matricula, 'dataInicio':
          viagem.dataInicio, 'kmsViagem': viagem.kmsViagem, 'custoPessoa':
          viagem.custoPessoa, 'localInicio':viagem.localInicio,
          'bagagem':viagem.bagagem, 'localDestino': viagem.localDestino,
          'nrLugares': viagem.nrLugares, 'lugaresDisp': viagem.lugaresDisp,
          'regularidade': viagem.regularidade, 'idCondutor': viagem.idCondutor,
          'descricao': viagem.descricao, 'estado': viagem.estado, -->
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
            Permite Bagagem: {{ viagem.bagagem ? 'Sim' : 'Não' }}
          </div>

          <div class="text-overline mb-4">
            Custo da Viagem: {{ viagem.custoPessoa }}€
          </div>

          <v-list-item-subtitle 
            >Data e Hora: {{ viagem.dataInicio }}
          </v-list-item-subtitle>
        </v-list-item-content>

      </v-list-item>
      <v-spacer></v-spacer>
      <div class="text-center">
        <v-btn class="ma-2" color="success" outlined @click="registarPassageiro">
          <!-- TODO: No caso de passageiro -->
          Registar na viagem
          <v-icon right> mdi-account-check-outline </v-icon>
        </v-btn>

        <v-btn class="ma-2" color="orange" outlined pill @click="editarViagem">
          <!-- TODO: No caso de condutor -->
          Editar Viagem
          <v-icon right> mdi-pencil-outline </v-icon>
        </v-btn>

        <v-btn class="ma-2" color="red" outlined pill @click="eliminarViagem">
          <!-- TODO: No caso de condutor -->
          Eliminar Viagem
          <v-icon right> mdi-delete-outline </v-icon>
        </v-btn>
      </div>
    </v-card>

    <!-- 
    <p>Mostrar dados da viagem</p>
    <p>Mostrar mapa da viagem</p>
    <p>Butoes para editar a viagem</p> 
    -->
    <Footer></Footer>
  </v-container>
</template>

<script>
import Header from "../components/Header.vue";
import Footer from "../components/Footer.vue";
import NavDraw from "../components/NavDraw.vue";

export default {
  name: "Viagem",
  components: {
    Header,
    Footer,
    NavDraw,
  },

  data() {
    return {
      tab: null,
      openHelp: false,
      viagem: {},
    };
  },
  created() {
    this.initialize();
  },
  methods: {
    onClickHeader() {
      this.$refs.navdraw.fixNav();
    },
    initialize() {
      this.$request("get", "viagem/" + this.$route.params.id)
        .then((response) => {
          this.viagem = response.data.Viagem[0];
        })
        .catch((error) => {
          console.log(error);
        });
    },
    registarPassageiro(){
      //TODO
    },
    editarViagem(){
      //TODO
    },
    eliminarViagem(){
      this.$request("delete",this.$route.params.id + "/remove")
        .then((response) => {
          console.log(response);
        })
        .catch((error) => {
          console.log(error);
        });
    }
  },
};
</script>
