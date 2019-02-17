<template>
  <v-layout row wrap>
    <v-flex xs6>
      <h1>Add new Vocabulary</h1>
      <form>
        <v-text-field
          v-model="german"
          :error-messages="germanErrors"
          label="German"
          required
          @input="$v.german.$touch()"
          @blur="$v.german.$touch()"
        ></v-text-field>
        <v-text-field
          v-model="english"
          :error-messages="englishErrors"
          label="English"
          required
          @input="$v.english.$touch()"
          @blur="$v.english.$touch()"
        ></v-text-field>
        <v-btn @click.prevent="submit">submit</v-btn>
        <v-btn @click="clear">clear</v-btn>
      </form>
      <div>
        <v-alert :value="true" type="success">This is a success alert.</v-alert>
      </div>
    </v-flex>
    <v-flex xs6>
      <h1>Vocab List</h1>
      <ul id="vocabs">
        <li
          v-for="vocab in this.vocabList"
          :key="vocab.german"
        >{{ vocab.german }} : {{vocab.english}}</li>
      </ul>
    </v-flex>
  </v-layout>
</template>

<script>
import { validationMixin } from "vuelidate";
import { required } from "vuelidate/lib/validators";

export default {
  mixins: [validationMixin],

  validations: {
    german: { required },
    english: { required }
  },

  data: () => ({
    german: "",
    english: "",
    vocabList: [],
    return: {
      alert: true
    }
  }),

  computed: {
    germanErrors() {
      const errors = [];
      if (!this.$v.german.$dirty) return errors;
      !this.$v.german.required && errors.push("german is required.");
      return errors;
    },
    englishErrors() {
      const errors = [];
      if (!this.$v.english.$dirty) return errors;
      !this.$v.english.required && errors.push("English is required");
      return errors;
    }
  },

  methods: {
    loadVocab() {
      this.$http({
        url: "http://127.0.0.1:8000/api/v1/vocabs/",
        method: "GET"
      }).then(function(responseData) {
        /* eslint-disable no-console */
        console.log(responseData);
        this.vocabList = JSON.parse(responseData.bodyText);
        console.log(this.vocabList);
        /* eslint-enable no-console */
      });
    },
    submit() {
      this.$v.$touch();
      this.$http
        .post("http://127.0.0.1:8000/api/v1/vocabs/", {
          german: this.german,
          english: this.english
        })
        .then(function(responseData) {
          /* eslint-disable no-console */
          console.log(responseData);
          /* eslint-enable no-console */
          this.loadVocab();
        });
    },
    clear() {
      this.$v.$reset();
      this.german = "";
      this.english = "";
    }
  },
  beforeMount: function() {
    this.loadVocab();
  }
};
</script>
