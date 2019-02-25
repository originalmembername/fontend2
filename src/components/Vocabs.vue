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
      <v-alert :value="alert" type="error">Vocab already exists.</v-alert>
    </v-flex>
    <v-flex xs6 style="max-height:400px; overflow:scroll;">
      <h1>Vocab List</h1>
      <div>
        <v-container fluid>
          <v-checkbox 
            :label="'Select all'"
          ></v-checkbox>
          <v-checkbox
            v-for="(vocab, index) in vocabList"
            :key="vocab.german"
            :id="vocab.german"
            v-model="selected[index]"
            height="0"
            style="margin:0px"
            :label="`${index} ${vocab.german} : ${vocab.english}`"
          ></v-checkbox>
        </v-container>
      </div>
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

  data() {
    return {
    selected: [],    
    german: "",
    english: "",
    vocabList: [],
    alert: false
    }    
  },

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
        this.vocabList = JSON.parse(responseData.bodyText);
        //by default, unselect all vocab
        for (var i=0; i<this.vocabList.length; i++){
          this.selected[i]=false;
        }
      });
    },
    submit() {
      if (this.german == "" || this.english == "") {
        return;
      }
      this.$v.$touch();
      this.$http
        .post("http://127.0.0.1:8000/api/v1/vocabs/", {
          german: this.german,
          english: this.english
        })
        .then(function(responseData) {
          var inserted = JSON.parse(responseData.bodyText).inserted;
          if (inserted == "False") {
            this.alert = true;
          } else {
            this.alert = false;
          }
          this.loadVocab();
          this.clear();
        });
    },
    clear() {
      this.$v.$reset();
      this.german = "";
      this.english = "";
    },
    selectAll() {
      /* eslint-disable no-console */
      console.log("selectAll");
      /* eslint-enable no-console */
    }
  },
  beforeMount: function() {
    this.loadVocab();
  }
};
</script>
