<template>

      <v-container class="my-5">
          <Header @clicked="onClickHeader"></Header>
          <NavDraw ref="navdraw"></NavDraw>

          
        
          <v-card
                class="mx-auto"
                max-width="500"
            >
               
            <v-row  v-if="viagensPorClassificar" >
              <v-col align-self="center">
                <v-btn outlined link to="historico">Viagens por classificar
                  <v-icon dark right> mdi-star </v-icon>
                </v-btn>
              </v-col>
            </v-row>
     

                <v-list two-line>
                <v-list-item-group
                   
                    active-class="brown--text"
                    multiple
                >
                    <template v-for="(item, index) in items">
                    <v-list-item :key="item.sent">
                        <template v-slot:default="{ active }">
                        <v-list-item-content>
                            <v-list-item-title v-text="item.titulo"></v-list-item-title>


                            <v-list-item-subtitle class="text--primary" v-text="item.mensagem"></v-list-item-subtitle>
                        </v-list-item-content>

                        <v-list-item-action>
                            <v-list-item-action-text v-text="item.sent"></v-list-item-action-text>

                            <v-icon
                            v-if="!active"
                            color="brown lighten-1"
                            >
                            mdi-star-outline
                            </v-icon>

                            <v-icon
                            v-else
                            color="brown darken-3"
                            >
                            mdi-star
                            </v-icon>
                        </v-list-item-action>
                        </template>
                    </v-list-item>

                    <v-divider
                        v-if="index < items.length - 1"
                        :key="index"
                    ></v-divider>
                    </template>
                </v-list-item-group>
                </v-list>
            </v-card>
      </v-container>
</template>

<script>
import Header from "../components/Header.vue";
import NavDraw from "../components/NavDraw.vue";
import {mapState} from "vuex";

export default {
    computed: mapState({
    username: (state) => state.auth.username
  }),

  components: {
    Header,
    NavDraw,
  },
  data() {
    return {
      selected: [],
      items: [],
      viagensPorClassificar:false
    }
  },
  created(){
      this.$request("get", "notificacao/todos/" + this.username)
        .then((response) => {
        this.items = response.data.Notificacoes;
        this.items.forEach((element,i) => {
            if (element.visto==0){
                this.selected.push(i)
            }
        });
         
      })
        .catch((error) => {
        console.log(error);
      });

      this.$request("get","avaliacao/yetToRate/" + this.username)
        .then((response)=>{
          console.log(response.data.ViagensPorClassificar)
          this.viagensPorClassificar=response.data.ViagensPorClassificar
        }).catch((error)=>{
          console.log(error)
        })
  },
  methods: {
    onClickHeader() {
      this.$refs.navdraw.fixNav();
    },
  }
};
</script>
