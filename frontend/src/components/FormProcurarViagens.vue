<template>
    <v-form ref= "form">
        <v-container> 
            <v-row >
                <v-col
                cols="12"
                sm="6"
                md="4"
                >
                <v-menu
                    ref="menuFrom"
                    v-model="menuFrom"
                    :close-on-content-click="false"
                    :return-value.sync="dateFrom"
                    transition="scale-transition"
                    offset-y
                    min-width="auto"
                >
                    <template v-slot:activator="{ on, attrs }">
                    <v-text-field
                        v-model="dateFrom"
                        label="Desde"
                        prepend-icon="mdi-calendar"
                        readonly
                        v-bind="attrs"
                        v-on="on"
                    ></v-text-field>
                    </template>
                    <v-date-picker
                    v-model="dateFrom"
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
                        @click="$refs.menuFrom.save(dateFrom)"
                    >
                        OK
                    </v-btn>
                    </v-date-picker>
                </v-menu>
                </v-col>
                <v-spacer></v-spacer>
                <v-col
                cols="12"
                sm="6"
                md="4"
                >
                <v-menu
                    ref="menuTo"
                    v-model="menu"
                    :close-on-content-click="false"
                    :return-value.sync="dateTo"
                    transition="scale-transition"
                    offset-y
                    min-width="auto"
                >
                    <template v-slot:activator="{ on, attrs }">
                    <v-text-field
                        v-model="dateTo"
                        label="Até"
                        prepend-icon="mdi-calendar"
                        readonly
                        v-bind="attrs"
                        v-on="on"
                    ></v-text-field>
                    </template>
                    <v-date-picker
                    v-model="dateTo"
                    no-title
                    scrollable
                    >
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
                        @click="$refs.menuTo.save(dateTo)"
                    >
                        OK
                    </v-btn>
                    </v-date-picker>
                </v-menu>
                </v-col>
                <v-spacer></v-spacer>
            </v-row>
            <v-row>
                <v-col cols="12" sm="6" md="4">
                   <v-text-field v-model="formData.PontoPartida" 
                    :rules="[...rules.required,...rules.length30]" 
                    :counter="30" label="Ponto de Partida"
                    /> 
                </v-col>
                <v-spacer></v-spacer>
                <v-col cols="12" sm="6" md="4">
                   <v-text-field v-model="formData.PontoChegada" 
                    :rules="[...rules.required,...rules.length30]" 
                    :counter="30" label="Ponto de Chegada"
                    /> 
                </v-col>
                <v-spacer></v-spacer>
           </v-row>
        </v-container>
    </v-form>
</template>


<script>
  export default {
    data(){
        return{
        formData:{
            dateFrom: (new Date(Date.now() - (new Date()).getTimezoneOffset() * 60000)).toISOString().substr(0, 10),
            dateTo: (new Date(Date.now() - (new Date()).getTimezoneOffset() * 60000)).toISOString().substr(0, 10),
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
        } 
    }
}
</script>