<template>
  <v-form  ref="form" >
    <v-container>
      <v-row>
          <v-col cols="12" md="4">
             <v-select v-model="formData.lugaresDisponiveis" clear :rules="rules.required" :items="lugares" label="Lugares Disponíveis" dense/>
          </v-col>

          <v-col cols="12" md="4">
          <v-text-field v-model="formData.pontoPartida" 
            :rules="[...rules.required,...rules.length30]" 
            :counter="30" label="Ponto de Partida"
            /> 
        </v-col>
        <v-col cols="12" md="4">
        <v-text-field v-model="formData.pontoChegada" 
            :rules="[...rules.required,...rules.length30]" 
            :counter="30" label="Ponto de Chegada"
            /> 
        </v-col>
        </v-row>
        <v-row>
        <v-col cols="12" md="4">
        <v-text-field v-model="formData.regularidade" 
            :rules="[...rules.required,...rules.length30]" 
            :counter="30" label="Regularidade"
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
            bagagem: false 
        },
        rules: {
            required: [(v) => !!v || "Field is required"],
            length30: [v => (v && v.length <= 30) || "Field must be less or equal than 30 characters"],
            length75: [v => (v && v.length <= 75) || "Field must be less or equal than 75 characters"],
            length100: [v => (v && v.length <= 100) || "Field must be less or equal than 100 characters"],
        },
        lugares:['1','2','3','4','5','6']
      }
    } ,
    methods:{
         reset () {
            this.$refs.form.reset()
            }
         }     
}
</script>

