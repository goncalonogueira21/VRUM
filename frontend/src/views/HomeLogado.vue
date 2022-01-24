<template>
  <v-container class="my-5">
    <Header @clicked="onClickHeader"></Header>
    <NavDraw ref="navdraw"></NavDraw>
    <p>Token is {{ token }}</p>
    <h1>TODO: Mostrar viagem que está a decorrer</h1>
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
    </v-card>
    <VueGooglePlaces
      :api-key="apiKey"
      types="(cities)"
      country="ua"
      placeholder="Input your place"
      @placechanged="onPlaceChanged"
      @noresult="onNoResult"
    />
  </v-container>
</template>

<script>
import Header from "../components/Header.vue";
import NavDraw from "../components/NavDraw.vue";
import { mapState } from "vuex";

export default {
  computed: mapState({
    token: (state) => state.auth.token,
  }),

  components: {
    Header,
    NavDraw,
  },
  name: "HomeLogado",
  data() {
    return {
      tab: null,
      openHelp: false,
      viagem: {},
    };
  },
  created() {
    this.$request("get", "viagem/" + this.$route.params.id)
      .then((response) => {
        this.viagem = response.data.Viagem[0];
      })
      .catch((error) => {
        console.log(error);
      });
  },
  methods: {
    onClickHeader() {
      this.$refs.navdraw.fixNav();
    },
  },
};
</script>
