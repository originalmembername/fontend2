<template>
  <v-form v-model="valid">
    <v-container>
      <v-layout column>
        <v-layout row wrap>
          <v-flex xs12 md4>
            <v-text-field
              v-model="username"
              :rules="nameRules"
              :counter="10"
              label="Username"
              required
            ></v-text-field>
          </v-flex>

          <v-flex xs12 md4>
            <v-text-field
              v-model="password"
              :rules="passwordRules"
              :counter="10"
              type="password"
              label="Password"
              required
            ></v-text-field>
          </v-flex>
          <v-flex xs12 md4>
            <v-text-field
              v-model="confirmPassword"
              :rules="passwordRules"
              :counter="10"
              type="password"
              label="Confirm Password"
              required
            ></v-text-field>
          </v-flex>
        </v-layout>
        <v-layout row>
          <v-btn @click="submit">submit</v-btn>
          <v-btn @click="clear">clear</v-btn>
          <v-alert :value="pwdDifferentAlert" type="error">Passwords don't match!</v-alert>
        </v-layout>
      </v-layout>
    </v-container>
  </v-form>
</template>

<script>
export default {
  data: () => ({
    valid: false,
    username: "",
    password: "",
    confirmPassword: "",
    pwdDifferentAlert: false,
    nameRules: [
      v => !!v || "Name is required",
      v => v.length <= 10 || "Name must be less than 10 characters"
    ],
    passwordRules: [
      v => !!v || "Password is required",
      v => v.length <= 10 || "Password must be less than 10 characters"
    ]
  }),
  methods: {
    submit() {
      if (this.password != this.confirmPassword) {
        this.pwdDifferentAlert = true;
        return;
      }
    },
    clear() {
      this.valid = false;
      this.username = "";
      this.password = "";
      this.confirmPassword = "";
      this.pwdDifferentAlert = false;
    }
  }
};
</script>