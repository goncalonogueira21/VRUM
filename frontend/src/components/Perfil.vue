<template>
  <v-container id="formData-profile-view" fluid tag="section">
    <v-row justify="center">
        <v-col cols="12">
                  <v-alert 
                    :value="alertSucesso"
                    transition="slide-y-transition"
                    dense
                    color="dark green"
                    dismissible
                    type="success" 
                    @input="alertSucesso=false">
                        Informações alteradas com sucesso
                    </v-alert>
                  </v-col>
               <v-col cols="12">
                  <v-alert 
                    :value="alertErro"
                    transition="slide-y-transition"
                    dense
                    color="dark red"
                    dismissible
                    type="error" 
                    @input="alertErro=false">
                        Erro ao salvar alterações
                    </v-alert>
                  </v-col>
      <v-col cols="12" md="4">
        
        <app-card class="mt-4 ml-16 text-center">
               
          <v-img
            class="rounded-circle elevation-8 mt-4 ml-4 d-inline-block"
            :src="`data:image/png;base64,${formData.ava}`"
            width="128"
          />
          
          <input class="text-h7 mb-2 text--secondary" v-if="!readonly" type="file" accept="image/*" @change="handleFileUpload( $event )"/>
         
          <v-card-text class="text-center">
            <h6 class="text-h6 mb-2 text--secondary">Rating</h6>
 
            <v-rating
              background-color="brown lighten-3"
              color="#7e380e"
              readonly
              length="5"
              size="24"
              v-model="formData.rating"
            />

            <h6 class="text-h6 mb-1 mt-4 text--secondary">About me</h6>

            <v-textarea
              flat
              solo
              class="ma-0 pa-0"
              hide-details
              v-model="formData.about"
              :readonly="readonly"
              row-height="10"
              auto-grow
              background-color="white"
            />
          </v-card-text>
        </app-card>
      </v-col>
      <v-col cols="12" md="8">
        <v-form>
          <v-container class="py-0">
            <v-row>
              <v-col cols="12" md="4">
                <v-text-field
                  v-model="formData.username"
                  :readonly="readonly"
                  color="#7e380e"
                  label="Username"
                />
              </v-col>

              <v-col cols="12" md="8">
                <v-text-field
                  :readonly="readonly"
                  v-model="formData.email"
                  color="#7e380e"
                  label="Email"
                />
              </v-col>

              <v-col cols="12" md="6">
                <v-text-field
                  :readonly="readonly"
                  v-model="formData.nomeProprio"
                  color="#7e380e"
                  label="Nome Próprio"
                />
              </v-col>

              <v-col cols="12" md="6">
                <v-text-field
                  :readonly="readonly"
                  v-model="formData.apelido"
                  color="#7e380e"
                  label="Apelido"
                />
              </v-col>

              <v-col cols="12">
                <v-text-field
                  :readonly="readonly"
                  v-model="formData.morada"
                  color="#7e380e"
                  label="Morada"
                />
              </v-col>

              <v-col cols="12" md="6">
                <v-text-field
                  :readonly="readonly"
                  v-model="formData.telemovel"
                  color="#7e380e"
                  label="Telemóvel"
                />
              </v-col>
              <v-col cols="12" md="6">
                <v-text-field
                  :readonly="readonly"
                  v-model="formData.dataNascimento"
                  color="#7e380e"
                  label="Data de Nascimento (dd/mm/aaaa)"
                />
              </v-col>

              <v-col cols="12" class="text-right">
                <v-btn
                  v-if="readonly"
                  class="mb-2"
                  color="#7e380e"
                  min-width="150"
                  @click="edit"
                >
                  Update Profile
                </v-btn>

                <v-btn
                  v-if="!readonly"
                  class="mb-2"
                  color="#7e380e"
                  min-width="150"
                  @click="save"
                >
                  Save Changes
                </v-btn>
              </v-col>
            </v-row>
          </v-container>
        </v-form>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import axios from "axios"
import {mapState} from "vuex"

export default {
  computed: mapState({
      username: state => state.auth.username
    }),
  name: "formDataProfileView",
  data() {
    return {
      formData: {
        username: "",
        email: "",
        nomeProprio: "",
        apelido: "",
        telemovel: "",
        morada: "",
        dataNascimento:"",
        rating:0 ,
        about:"",
        ava:''
      },
      readonly: true,
      url:'',
      base64:'',
      alertSucesso: false,
      alertErro: false
    };
  },
  mounted(){
    if(this.alertSucesso){
      this.hide_alertSucesso();
    }
    if(this.alertErro){
      this.hide_alertErro();
    }
  },
  created(){
   this.initialize()
  },
  methods: {
    hide_alertSucesso() {
      window.setInterval(() => {
        this.alertSucesso = false;
      }, 6000)    
    },
    hide_alertErro() {
      window.setInterval(() => {
        this.alertErro = false;
      }, 6000)    
    },
    initialize(){
      axios.get("http://localhost:5000/utilizador/" + this.username, {
        headers : { "Content-Type": "application/json" }
      })
        .then((response) => {
            let resp = response.data[0]
            this.formData.username = resp.username
            this.formData.email = resp.email
            this.formData.nomeProprio = resp.firstName
            this.formData.apelido = resp.lastName
            this.formData.telemovel = resp.nrTelemovel
            this.formData.morada = resp.morada
            this.formData.dataNascimento = resp.dataNascimento
            this.formData.rating = resp.rating
            this.formData.about = resp.aboutME
            this.formData.ava = resp.avatar

        })
        .catch((error)=>{
          console.log(error)
        })
    },
    edit() {
      this.readonly = !this.readonly;
    },  
    save() {
      var payload = new FormData();
      payload.append( 'username', this.formData.username);
      payload.append( 'email', this.formData.email);
      payload.append( 'firstName', this.formData.nomeProprio);
      payload.append( 'lastName', this.formData.apelido);
      payload.append('nrTelemovel', this.formData.telemovel); 
      payload.append( 'morada', this.formData.morada); 
      payload.append( 'dataNascimento', this.formData.dataNascimento); 
      payload.append( 'aboutME', this.formData.about);
      payload.append( 'avatar', this.formData.ava);
      
      

      this.readonly = !this.readonly;
      axios
        .put("http://localhost:5000/utilizador/" + this.username + "/update", payload,
          // headers: {'Content-Type': ' multipart/form-data' 
          )
        .then(
          (response) => {
            console.log(response.data);
            this.alertSucesso= true
          },
          (error) => {
            this.alertErro = true
            console.log(error);
          }
        );
      },
      handleFileUpload( event ){
        const file = event.target.files[0];
         const reader = new FileReader()

          reader.onloadend = () => {
             this.formData.ava= reader.result.split(',')[1]

          }
          reader.readAsDataURL(file);


    },
  },
};
</script>
