<template>
    <v-app-bar app color="#2A3F54" height="100" clipped-left>
        <v-list
            nav
            dense
            dark
            color="#2A3F54"
        >
            <v-list-item two-line class="px-0">
                <v-list-item-avatar min-width="55px" tile class="ava" @click="about = true">
                    <img src= "../assets/VRUM_logo.png" > 
                </v-list-item-avatar>
            </v-list-item>
        </v-list>
        <div class="spacer"></div>
       
        <!-- Menú do cabeçalho-->
        <v-menu>
            <template v-slot:activator="{ on: menu }">
                <v-tooltip bottom>
                    <template v-slot:activator="{ on: tooltip }">
                        <v-btn
                        fab
                        v-on="{ ...tooltip, ...menu }"
                        >
                            <v-avatar>
                                <v-img v-bind:src="foto"/>
                            </v-avatar>
                        </v-btn>
                    </template>
                    <span>
                        
                    </span>
                </v-tooltip>
            </template>
            <v-list>
                <v-list-item link :to="link">
                    <v-list-item-title>Página para mudar</v-list-item-title>
                </v-list-item>
                <!-- Se se quiser fazer logout -->
                <v-list-item @click="logout();" text>
                    <v-list-item-title>Logout</v-list-item-title>
                </v-list-item>
            </v-list>
        </v-menu>
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