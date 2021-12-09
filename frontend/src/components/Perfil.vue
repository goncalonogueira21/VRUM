<template>
  <v-container id="user-profile-view" fluid tag="section">
    <v-row justify="center">
      <v-col cols="12" md="4">
        <app-card class="mt-4 ml-16 text-center">
          <v-img
            class="rounded-circle elevation-8 mt-4 ml-4 d-inline-block"
            src="https://demos.creative-tim.com/vue-material-dashboard/img/marc.aba54d65.jpg"
            width="128"
          />

          <v-card-text class="text-center">
            <h6 class="text-h6 mb-2 text--secondary">Rating</h6>

            <v-rating
              background-color="brown lighten-3"
              color="#7e380e"
              :readonly="readonly"
              length="5"
              size="24"
              v-model="this.user.rating"
            />

            <h6 class="text-h6 mb-1 mt-4 text--secondary">About me</h6>

            <v-textarea
              flat
              solo
              class="ma-0 pa-0"
              hide-details
              v-model="this.user.about"
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
                  v-model="this.user.username"
                  :readonly="readonly"
                  color="#7e380e"
                  label="Username"
                />
              </v-col>

              <v-col cols="12" md="8">
                <v-text-field
                  :readonly="readonly"
                  v-model="this.user.email"
                  color="#7e380e"
                  label="Email"
                />
              </v-col>

              <v-col cols="12" md="6">
                <v-text-field
                  :readonly="readonly"
                  v-model="this.user.nomeProprio"
                  color="#7e380e"
                  label="Nome Próprio"
                />
              </v-col>

              <v-col cols="12" md="6">
                <v-text-field
                  :readonly="readonly"
                  v-model="this.user.apelido"
                  color="#7e380e"
                  label="Apelido"
                />
              </v-col>

              <v-col cols="12">
                <v-text-field
                  :readonly="readonly"
                  v-model="this.user.morada"
                  color="#7e380e"
                  label="Morada"
                />
              </v-col>

              <v-col cols="12" md="6">
                <v-text-field
                  :readonly="readonly"
                  v-model="this.user.telemovel"
                  color="#7e380e"
                  label="Telemóvel"
                />
              </v-col>

              <v-col cols="12" md="6">
                <v-text-field
                  :readonly="readonly"
                  v-model="this.user.dataNascimento"
                  color="#7e380e"
                  label="Data de Nascimento"
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
import axios from "axios";

export default {
  name: "UserProfileView",
  data() {
    return {
      user: {
        username: "Gonçalo",
        email: "mail@mail.com",
        nomeProprio: "Antonio",
        apelido: "Carvalho",
        telemovel: "912345678",
        morada: "Rua Nova Santa Cruz",
        dataNascimento: new Date(
          Date.now() - new Date().getTimezoneOffset() * 60000
        )
          .toISOString()
          .substr(0, 10),
        rating: "3",
        about:
          "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Ratione dolorem deserunt veniam tempora magnam quisquam quam error iusto cupiditate ducimus, et eligendi saepe voluptatibus assumenda similique temporibus placeat animi dicta?",
      },
      readonly: true,
    };
  },
  methods: {
    edit() {
      this.readonly = !this.readonly;
    },
    save() {
      const payload = this.user;
      this.readonly = !this.readonly;
      axios
        .put("http://localhost:5000/users/" + this.user.username, payload)
        .then(
          (response) => {
            console.log(response.data);
          },
          (error) => {
            console.log(error);
          }
        );
    },
  },
};
</script>
