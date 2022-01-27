<template>
  <div class="text-center ma-2">
        <v-snackbar 
           v-model="showMensagem"
            :timeout="timeout"
            multi-line>
            {{mensagem}}
              <template v-slot:action="{ attrs }">
              <v-btn
                color="white"
                text
                v-bind="attrs"
                @click="verMensagem"
              >
                Ver
              </v-btn>
              <v-btn
                color="white"
                text
                v-bind="attrs"
                @click="closeMensagem"
              >
                Fechar
              </v-btn>
            </template>
        </v-snackbar>
         <v-snackbar 
           v-model="showViagem"
           :timeout="timeout"
           multi-line>
            {{mensagem}}
              <template v-slot:action="{ attrs }">
               <v-btn
                color="white"
                text
                v-bind="attrs"
                @click="verViagem"
              >
                Ver
              </v-btn>
              <v-btn
                color="white"
                text
                v-bind="attrs"
                @click="closeViagem"
              >
                Fechar
              </v-btn>
            </template>
        </v-snackbar>
         <v-snackbar 
           v-model="showPedido"
           :timeout="timeout"
           multi-line>
            {{mensagem}}
              <template v-slot:action="{ attrs }">
               <v-btn
                color="white"
                text
                v-bind="attrs"
                @click="verPedido"
              >
                Ver
              </v-btn>
              <v-btn
                color="white"
                text
                v-bind="attrs"
                @click="closePedido"
              >
                Fechar
              </v-btn>
            </template>
        </v-snackbar>
        </div>
</template>

<script>
import { mapState } from "vuex";


export default {
    computed: mapState({
    username: (state) => state.auth.username
  }),
  name: "notificacao",
   data() {
    return {
        showViagem: false,
        showMensagem: false,
        showPedido: false,
        mensagem: "",
        idViagem:"",
        timeout: 8000,
        }
    },
    sockets: {
    connect() {
      // Fired when the socket connects.
      console.log("Conectou", this.username)
      
    },
    disconnect() {
      console.log("Desconectou")
    },
  
    viagem(data){
      console.log("socket viagem" +  data.viagem)
      this.showViagem=true
      this.mensagem = data.mensagem
      this.idViagem= data.viagem 
      
    },
    message(data){
        console.log("socket mensagem" + data.mensagem)
        this.showMensagem=true
        this.mensagem=data.mensagem
    },
    pedido(data){
      console.log("socket pedido" + data.mensagem)
      this.showPedido= true
      this.mensagem= data.mensagem
    }
    
  },
  methods:{
    closeMensagem(){
      this.showMensagem= false,
      this.mensagem= ""
    },
    closeViagem(){
      this.showViagem=false,
      this.mensagem="",
      this.idViagem=''
    },
    closePedido(){
      this.showPedido= false,
      this.mensagem=""
    },
    verMensagem(){
      this.showMensagem= false,
      this.mensagem= "",
      this.$router.push({name : "inbox"})
    },
    verViagem(){
      this.showViagem=false,
      this.mensagem="",
      this.$router.push("/viagem/" + this.idViagem)
    },
    verPedido(){
      this.showPedido=false,
      this.mensagem="",
      this.$router.push({name: "pedidos"})
    }
  }
}
</script>

