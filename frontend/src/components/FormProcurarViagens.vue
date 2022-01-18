<template>
    <v-form ref= "form">
        <v-container> 
            <v-row >
                <v-col
                cols="12"
                sm="8"
                md="6"
                >
                <v-menu
                    ref="menuFrom"
                    v-model="menuFrom"
                    :close-on-content-click="false"
                    :return-value.sync="formData.dateFrom"
                    transition="scale-transition"
                    offset-y
                    min-width="auto"
                >
                    <template v-slot:activator="{ on, attrs }">
                    <v-text-field
                        v-model="formData.dateFrom"
                        label="Desde"
                        prepend-icon="mdi-calendar"
                        readonly
                        v-bind="attrs"
                        v-on="on"
                    ></v-text-field>
                    </template>
                    <v-date-picker
                    v-model="formData.dateFrom"
                    no-title
                    scrollable
                    >
                    <v-spacer></v-spacer>
                    <v-btn
                        text
                        color="primary"
                        @click="menuFrom = false"
                    >
                        Cancel
                    </v-btn>
                    <v-btn
                        text
                        color="primary"
                        @click="$refs.menuFrom.save(formData.dateFrom)"
                    >
                        OK
                    </v-btn>
                    </v-date-picker>
                </v-menu>
                </v-col>
                <v-spacer></v-spacer>
                <v-col
                cols="12"
                sm="8"
                md="6"
                >
                <v-menu
                    ref="menuTo"
                    v-model="menuTo"
                    :close-on-content-click="false"
                    :return-value.sync="formData.dateTo"
                    transition="scale-transition"
                    offset-y
                    min-width="auto"
                >
                    <template v-slot:activator="{ on, attrs }">
                    <v-text-field
                        v-model="formData.dateTo"
                        label="Até"
                        prepend-icon="mdi-calendar"
                        readonly
                        v-bind="attrs"
                        v-on="on"
                    ></v-text-field>
                    </template>
                    <v-date-picker
                    v-model="formData.dateTo"
                    no-title
                    scrollable
                    >
                    <v-spacer></v-spacer>
                    <v-spacer></v-spacer>   
                    <v-btn
                        text
                        color="primary"
                        @click="menuTo = false"
                    >
                        Cancel
                    </v-btn>
                    <v-btn
                        text
                        color="primary"
                        @click="$refs.menuTo.save(formData.dateTo)"
                    >
                        OK
                    </v-btn>
                    </v-date-picker>
                </v-menu>
                </v-col>
                <v-spacer></v-spacer>
            </v-row>
            <v-row>
                <v-col cols="12" sm="8" md="6">
                   <v-text-field v-model="formData.PontoPartida" 
                    :rules="[...rules.required,...rules.length30]" 
                    :counter="30" label="Ponto de Partida"
                    /> 
                </v-col>
                <v-spacer></v-spacer>
                <v-col cols="12" sm="8" md="6">
                   <v-text-field v-model="formData.PontoChegada" 
                    :rules="[...rules.required,...rules.length30]" 
                    :counter="30" label="Ponto de Chegada"
                    /> 
                </v-col>
                <v-spacer></v-spacer>
           </v-row>
           <v-row>
               <v-col cols="11" md="6">
                    <v-checkbox v-model="formData.bagagem"
                    label="Bagagem"
              />
               </v-col>
           </v-row>
           <v-row>
                <v-col cols="12" class="text-center">
                   <v-btn
                  class="mb-2"
                  color="#7e380e"
                  min-width="150"
                  @click="search()"
                >
                  Procurar
                </v-btn>
                </v-col>
           </v-row>
        </v-container>
    </v-form>
</template>


<script>
  export default {
    data(){
        return{
        formData:{
            dateFrom: '',
            dateTo: '',
            PontoPartida:'',
            PontoChegada:'',
            bagagem: false
        },
        menuFrom: false,
        menuTo: false,
        rules: {
            required: [(v) => !!v || "Field is required"],
            length30: [v => (v && v.length <= 30) || "Field must be less or equal than 30 characters"],
            length75: [v => (v && v.length <= 75) || "Field must be less or equal than 75 characters"],
            length100: [v => (v && v.length <= 100) || "Field must be less or equal than 100 characters"],
            }
        };
    },
    methods:{
            search(){
                var payload = new FormData();
                payload.append('localInicio', this.formData.PontoPartida);
                payload.append('localDestino',this.formData.PontoChegada);
                payload.append('bagagem', this.formData.bagagem ? 1 : 0);
                this.$request("post", "viagem/filtros?dataInicio=" + this.formData.dateFrom + "&" + this.formData.dateTo, payload)
                    .then((response)=>{
                        console.log(response.data)
                        this.$emit('clicked', response.data.Viagens)
                    }).catch((error)=>{
                        console.log(error)
                    })
            }
        }
}
</script>