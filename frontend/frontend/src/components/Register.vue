<template>
  <form>
    <v-text-field
      v-model="name"
      :error-messages="usernameErrors"
      label="name"
      required
      @input="$v.name.$touch()"
      @blur="$v.name.$touch()"
    ></v-text-field>

    <v-text-field
      v-model="email"
      :error-messages="emailErrors"
      label="E-mail"
      required
      @input="$v.email.$touch()"
      @blur="$v.email.$touch()"
    ></v-text-field>

    <v-text-field
      v-model="password"
      :error-messages="passwordErrors"
      :counter="20"
      label="password"
      required
      @input="$v.password.$touch()"
      @blur="$v.password.$touch()"
    ></v-text-field>

    <v-text-field
      v-model="repeatpassword"
      :error-messages="repeatpasswordErrors"
      :counter="20"
      label="repeatpassword"
      required
      @input="$v.repeatpassword.$touch()"
      @blur="$v.repeatpassword.$touch()"
    ></v-text-field>

    <v-btn class="mr-4" @click="submit"> register </v-btn>
    <v-btn @click="clear"> clear </v-btn>
  </form>
</template>

<script>
import { validationMixin } from "vuelidate";
import { required, maxLength, email } from "vuelidate/lib/validators";

export default {
  mixins: [validationMixin],

  validations: {
    email: { required, email },
    password: { required, maxLength: maxLength(20) },
    repeatpassword: { required, maxLength: maxLength(20) },
  },

  data: () => ({
    name: "",
    password: "",
    repeatpassword: "",
    email: "",
  }),

  computed: {
    nameErrors() {
      const errors = [];
      if (!this.$v.name.$dirty) return errors;
      !this.$v.name.maxLength &&
        errors.push("name must be at most 20 characters long");
      !this.$v.name.required && errors.push("username is required.");
      return errors;
    },
    passwordErrors() {
      const errors = [];
      if (!this.$v.password.$dirty) return errors;
      !this.$v.password.maxLength &&
        errors.push("password must be at most 20 characters long");
      !this.$v.password.required && errors.push("password is required.");
      return errors;
    },
    emailErrors() {
      const errors = [];
      if (!this.$v.email.$dirty) return errors;
      !this.$v.email.email && errors.push("Must be valid e-mail");
      !this.$v.email.required && errors.push("E-mail is required");
      return errors;
    },
    repeatpasswordErrors(){
      const errors=[];
      if (!this.$v.repeatpassword.$dirty) return errors;
      if (this.$v.password === this.$v.repeatpassword) { console.log("iguais")} else {console.log("merda")}
      return errors;
    }
  },

  methods: {
    submit() {
      this.$v.$touch();
    },
    clear() {
      this.$v.$reset();
      this.username = "";
      this.password = "";
      this.email = "";
    },
  },
};
</script>
