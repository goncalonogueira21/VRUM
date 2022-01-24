<template>
  <v-container class="my-5">
    <Header @clicked="onClickHeader"></Header>
    <NavDraw ref="navdraw"></NavDraw>
    <v-layout justify-space-around row wrap>
      <v-flex xs10 sm10 md9 lg9>
        <v-card class="mt-2" flat>
          <div v-if="viagensPorClassificar" class="text-xs-center">
            <v-row justify="center">
              <v-col cols="12">
                <v-btn outline link to="historico">Viagens por classificar
                  <v-icon dark right> mdi-star </v-icon>
                </v-btn>
              </v-col>
            </v-row>
          </div>
        </v-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import Header from "../components/Header.vue";
import NavDraw from "../components/NavDraw.vue";
import { mapState } from "vuex";

export default {
  computed: mapState({
    username: (state) => state.auth.username
  }),

  components: {
    Header,
    NavDraw,
  },
  name: "HomeLogado",
  data() {
    return {
      tab: null,
      viagensPorClassificar:false
    };
  },
  created(){
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
  },
};
</script>
