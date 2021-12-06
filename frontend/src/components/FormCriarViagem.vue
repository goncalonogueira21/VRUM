<template>
  <v-form  ref="form" >
    <v-container>
      <v-row>
          <v-col cols="11" md="5">
          <v-text-field v-model="formData.pontoPartida" 
            :rules="[...rules.required,...rules.length30]" 
            :counter="30" label="Ponto de Partida"
            /> 
        </v-col>
        <v-spacer></v-spacer>
        <v-col cols="11" md="5">
        <v-text-field v-model="formData.pontoChegada" 
            :rules="[...rules.required,...rules.length30]" 
            :counter="30" label="Ponto de Chegada"
            /> 
        </v-col>
        </v-row>
        <v-row>
          <v-col
                cols="11"
                sm="5"
       
                >
                <v-menu
                    ref="menu"
                    v-model="menu"
                    :close-on-content-click="false"
                    :return-value.sync="date"
                    transition="scale-transition"
                    offset-y
                    min-width="auto"
                >
                    <template v-slot:activator="{ on, attrs }">
                    <v-text-field
                        :rules="rules.required"
                        v-model="date"
                        label="Data da viagem"
                        prepend-icon="mdi-calendar"
                        readonly
                        v-bind="attrs"
                        v-on="on"
                    ></v-text-field>
                    </template>
                    <v-date-picker
                    v-model="date"
                    no-title
                    scrollable
                    >
                    <v-spacer></v-spacer>
                    <v-btn
                        text
                        color="primary"
                        @click="menu = false"
                    >
                        Cancel
                    </v-btn>
                    <v-btn
                        text
                        color="primary"
                        @click="$refs.menu.save(date)"
                    >
                        OK
                    </v-btn>
                    </v-date-picker>
                </v-menu>
                </v-col>
                <v-spacer></v-spacer>
                <v-col
                  cols="11"
                  sm="5"
                >
                  <v-menu
                    ref="menuTime"
                    v-model="menuTime"
                    :close-on-content-click="false"
                    :nudge-right="40"
                    :return-value.sync="horaInicio"
                    transition="scale-transition"
                    offset-y
                    max-width="290px"
                    min-width="290px"
                  >
                    <template v-slot:activator="{ on, attrs }">
                      <v-text-field
                        :rules="rules.required"
                        v-model="time"
                        label="Hora de Ínicio"
                        prepend-icon="mdi-clock-time-four-outline"
                        readonly
                        v-bind="attrs"
                        v-on="on"
                      ></v-text-field>
                    </template>
                    <v-time-picker
                      v-if="menu2"
                      v-model="horaInicio"
                      full-width
                      @click:minute="$refs.menuTime.save(horaInicio)"
                    ></v-time-picker>
                  </v-menu>
                </v-col>
        </v-row>
        <v-row >
           <v-col cols="11" md="4">
             <v-select height="44px" v-model="formData.lugaresDisponiveis" clear :rules="rules.required" :items="lugares" label="Lugares Disponíveis" dense/>
          </v-col>

        <v-col cols="11" md="4">
        <v-text-field v-model="formData.regularidade" 
            :rules="rules.length30" 
            :counter="30" label="Regularidade"
            /> 
        </v-col>
        <v-col cols="12" md="4">
          <v-checkbox v-model="formData.bagagem"
              label="Bagagem"
              />
        </v-col>
        </v-row>
    </v-container>
  </v-form>
</template>

<script>
export default {
    data() {    
      return{
        randomdata: '',
        formData:{
            id: '',
            lugaresDisponiveis:'',
            pontoPartida:'',
            pontoChegada:'',
            regularidade:'',
            bagagem: false,
            date: (new Date(Date.now() - (new Date()).getTimezoneOffset() * 60000)).toISOString().substr(0, 10),
            horaInicio:''
        },
        rules: {
            required: [(v) => !!v || "Field is required"],
            length30: [v => (v && v.length <= 30) || "Field must be less or equal than 30 characters"],
            length75: [v => (v && v.length <= 75) || "Field must be less or equal than 75 characters"],
            length100: [v => (v && v.length <= 100) || "Field must be less or equal than 100 characters"],
        },
        lugares:['1','2','3','4','5','6'],
        menu: false,
        menu2: false
      }
    } ,
    methods:{
         reset () {
            this.$refs.form.reset()
            }
         }     
}
</script>

