<template>
  <form>
    <!-- <v-text-field
      v-model="email"
      :error-messages="emailErrors"
      label="E-mail"
      required
      @input="$v.email.$touch()"
      @blur="$v.email.$touch()"
    ></v-text-field>-->
    <v-text-field
      v-model="username"
      :error-messages="usernameErrors"
      label="User"
      required
      @input="$v.username.$touch()"
      @blur="$v.username.$touch()"
    ></v-text-field>
    <v-text-field
      v-model="password"
      :error-messages="passwordErrors"
      :append-icon="show ? 'visibility' : 'visibility_off'"
      required
      :type="show ? 'text' : 'password'"
      label="Password"
      counter
      @input="$v.password.$touch()"
      @blur="$v.password.$touch()"
      @click:append="show = !show"
    ></v-text-field>
    <v-btn @click.prevent="login">login</v-btn>
    <v-btn @click="clear">clear</v-btn>
  </form>
</template>

<script>
import { validationMixin } from "vuelidate";
import { required, email } from "vuelidate/lib/validators";

export default {
  mixins: [validationMixin],

  validations: {
    /* email: { required, email }, */
    username: { required },
    password: { required }
  },

  data: () => ({
    /* email: "", */
    username: "",
    password: "",
    show: false
  }),

  computed: {
    /* emailErrors() {
      const errors = [];
      if (!this.$v.email.$dirty) return errors;
      !this.$v.email.email && errors.push("Must be valid e-mail");
      !this.$v.email.required && errors.push("E-mail is required");
      return errors;
    }, */
    usernameErrors() {
      const errors = [];
      if (!this.$v.username.$dirty) return errors;
      !this.$v.username.required && errors.push("Username is required");
      return errors;
    },
    passwordErrors() {
      const errors = [];
      if (!this.$v.password.$dirty) return errors;
      !this.$v.password.required && errors.push("Password is required");
      return errors;
    }
  },

  methods: {
    clear() {
      this.$v.$reset();
      this.password = "";
      this.email = "";
    },
    login: function() {
      if (this.passwordErrors[0] != null || this.emailErrors[0] != null) {
        return;
      }
      /* eslint-disable no-console */
      console.log("login");
      let email = this.email;
      let password = this.password;
      this.$store
        .dispatch("login", { email, password })
        .then(() => this.$router.push("/account"))
        .catch(err => console.log(err));
      /* eslint-disable no-console */
    }
  }
};
</script>
