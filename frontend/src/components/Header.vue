<template>
    <v-app-bar app color="#7e380e" height="80" clipped-left>
        
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
                    <v-list-item-title>Editar Perfil</v-list-item-title>
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