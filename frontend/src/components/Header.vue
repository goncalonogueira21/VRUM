<template>
    <v-app-bar app color="#7e380e" height="80" clipped-left>
        
        <v-list
            nav
            dense
            dark
            color="#7e380e"
            
        >
        <v-list-item two-line class="px-4" >               
            <v-list-item-content>
                <v-list-item-title><h2>VRUM</h2></v-list-item-title>
                <v-list-item-subtitle>Vehicle Rides UM</v-list-item-subtitle>
                </v-list-item-content>
            </v-list-item>
                  
        </v-list>
        <div class="spacer"></div>
               <v-btn
                    class="ma-4"
                    color="gray"
                    dense
                    dark
                    elevation="10"
                    to="/search"
                >
                    <v-icon dark>
                    mdi-home-circle-outline
                    </v-icon>
                </v-btn>
        <v-list-item-group>
            <v-list-item disabled dark>
                <v-list-item-content>
                    <v-list-item-title>Nome do utilizador</v-list-item-title>
                </v-list-item-content>
            </v-list-item>
        </v-list-item-group> 
    </v-app-bar>
</template>

<script>
//import axios from 'axios'
export default {
    data() {
        return{
            parametro:'',
        }
    },
    methods:{
        logout: function(){
            //Função de logout
        }
    }
};
</script>

<style scoped>
/* css do cabeçalho */
.v-toolbar__content, .v-toolbar__extension{
    position: relative;
}
.spacer{
    flex-grow: 1;
}
h1{
    color:white;
    text-align:center;
}
</style>