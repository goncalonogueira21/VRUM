<template>
  <v-form ref="form">
    <v-container>
      <v-row>
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
      </v-row>
      <v-row>
        <v-col cols="11" md="5">
          <v-text-field
            v-model="formData.localInicio"
            id="autocomplete"
            :rules="[...rules.required, ...rules.length30]"
            :counter="30"
            label="Ponto de Partida"
          />
        </v-col>
        <v-spacer></v-spacer>
        <v-col cols="11" md="5">
          <v-text-field
            v-model="formData.localDestino"
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
            :return-value.sync="formData.dataInicio"
            transition="scale-transition"
            offset-y
            min-width="auto"
          >
            <template v-slot:activator="{ on, attrs }">
              <v-text-field
                :rules="rules.required"
                v-model="formData.dataInicio"
                label="Data da viagem"
                prepend-icon="mdi-calendar"
                readonly
                v-bind="attrs"
                v-on="on"
              ></v-text-field>
            </template>
            <v-date-picker v-model="formData.dataInicio" no-title scrollable>
              <v-spacer></v-spacer>
              <v-btn text color="primary" @click="menu = false"> Cancel </v-btn>
              <v-btn text color="primary" @click="$refs.menu.save(formData.dataInicio)">
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
            :return-value.sync="formData.horaInicio"
            transition="scale-transition"
            offset-y
            max-width="290px"
            min-width="290px"
          >
            <template v-slot:activator="{ on, attrs }">
              <v-text-field
                :rules="rules.required"
                v-model="formData.horaInicio"
                label="Hora de Ínicio"
                prepend-icon="mdi-clock-time-four-outline"
                readonly
                v-bind="attrs"
                v-on="on"
              ></v-text-field>
            </template>
            <v-time-picker
              v-if="menuTime"
              v-model="formData.horaInicio"
              full-width
              @click:minute="$refs.menuTime.save(formData.horaInicio)"
            ></v-time-picker>
          </v-menu>
        </v-col>
      </v-row>
      <v-row>
        <v-col cols="11" md="5">
          <v-select
            height="44px"
            v-model="formData.lugaresDisp"
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
            v-model="formData.regularidade"
            :rules="rules.length30"
            :counter="30"
            label="Regularidade"
          />
        </v-col>
      </v-row>
      <v-row>
        <v-col cols="11" md="5">
          <v-text-field
            v-model="formData.custoPessoa"
            label="Custo mínimo por pessoa"
          />
        </v-col>
        <v-spacer />
        <v-col cols="11" md="5">
          <v-checkbox v-model="formData.bagagem" label="Bagagem" />
        </v-col>
      </v-row>
    </v-container>
    <v-card  flat>
      <v-row class="px-2 pb-2 ma-0 py-2" justify="center">
      
          <v-btn  class="ml-2 mr-2 mb-2" color="#7e380e" elevation="5" @click="reset">
            Clean
            <v-icon color="white">mdi-broom</v-icon>
          </v-btn>
          
          <v-btn
            @click="registaViagem"
            color="#7e380e"
            elevation="5"
            class="ml-2 mr-2 mb-2"
          >
          Submit
            <v-icon color="white">mdi-checkbox-marked-outline</v-icon>
          </v-btn>
        
      </v-row>
    </v-card>
  </v-form>
</template>

<script>
import { mapState } from "vuex";
export default {
  data() {
    return {
      randomdata: "",
      formData: {
        id: "",
        lugaresDisp: 0,
        localInicio: "",
        fk_Carro_matricula: "",
        localDestino: "",
        regularidade: "",
        bagagem: false,
        dataInicio: '',
        horaInicio: null,
        custoPessoa: 0,
        kmsViagem: 0,
      },
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
      menu: false,
      menu2: false,
      menuTime: false,
      carros: [],
      openHelp: false,
    };
  },
  computed: mapState({
    username: (state) => state.auth.username,
  }),
  /* mounted(){
        new google.maps.places.Autocomplete(
            document.getElementById("autocomplete")
        )
    },*/

  methods: {
    reset() {
      this.$refs.form.reset();
    },
    getCarros() {
      console.log("user", this.username);
      this.$request("get", "carro/" + this.username)
        .then((response) => {
          this.carros = response.data.Carros;
          console.log(this.carros);
        })
        .catch((error) => {
          console.log(error);
        });
    },
    registaViagem(){
      var payload = new FormData();
      payload.append('lugaresDisp', this.formData.lugaresDisp);
      payload.append('localInicio', this.formData.localInicio );
      payload.append('fk_Carro_matricula',this.formData.fk_Carro_matricula );
      payload.append('localDestino', this.formData.localDestino);
      payload.append('regularidade',this.formData.regularidade );
      payload.append('dataInicio',this.formData.dataInicio );
      payload.append('bagagem', this.formData.bagagem ? 1 : 0);
      payload.append('horaInicio', this.formData.horaInicio);
      payload.append('custoPessoa', this.formData.custoPessoa);
      payload.append('kmsViagem', this.formData.kmsViagem);
      payload.append('idCondutor', this.username);

      this.$request("post", "viagem/registo", payload, {'Content-Type': ' multipart/form-data'})
        .then((response) => {
          console.log(response);
        })
        .catch((error) => {
          console.log(error);
        });
    },

  },
  created() {
    this.getCarros();
  },
};
</script>
