<template>
  <form>
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
      :append-icon="show ? 'visibility' : 'visibility_off'"
      required
      :type="show ? 'text' : 'password'"
      label="Password"
      counter
      @click:append="show = !show"
    ></v-text-field>
    <v-btn @click.prevent="submit">submit</v-btn>
    <v-btn @click="clear">clear</v-btn>
  </form>
</template>

<script>
import { validationMixin } from "vuelidate";
import { required, email } from "vuelidate/lib/validators";

export default {
  mixins: [validationMixin],

  validations: {
    email: { required, email },
    password: { required }
  },

  data: () => ({
    name: "",
    email: "",
    show: false
  }),

  computed: {
    emailErrors() {
      const errors = [];
      if (!this.$v.email.$dirty) return errors;
      !this.$v.email.email && errors.push("Must be valid e-mail");
      !this.$v.email.required && errors.push("E-mail is required");
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
    submit() {
      this.$v.$touch();
      this.$http({
        url: "http://127.0.0.1:8000/api/v1/vocabs/",
        method: "GET"
      }).then(function(responseData) {
        /* eslint-disable no-console */
        console.log(responseData);
        /* eslint-enable no-console */
      });
    },
    clear() {
      this.$v.$reset();
      this.password = "";
      this.email = "";
    }
  }
};
</script>
