<template>
  <v-layout row wrap>
    <v-flex xs6>
      <h1 v-if="editMode">Edit vocabulary</h1>
      <h1 v-else>Add new vocabulary</h1>
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
        <v-btn v-if="editMode" @click.prevent="submitEdit">submit</v-btn>
        <v-btn v-else @click.prevent="submitAdd">submit</v-btn>
        <v-btn v-if="editMode" @click="cancelEdit">cancel</v-btn>
        <v-btn v-else @click="clear">clear</v-btn>
      </form>
      <v-alert :value="duplicateAlert" type="error">Vocab already exists.</v-alert>
    </v-flex>
    <v-flex xs6 style="max-height:400px; overflow:scroll;">
      <h1>Vocab List</h1>
      <div>
        <v-btn small @click="deleteSelected()">Delete Selected</v-btn>
        <table class="table table-striped table-hover">
          <thead>
            <tr>
              <th>
                <label class="form-checkbox">
                  <input type="checkbox" v-model="selectAll" @click="select">
                  <i class="form-icon"></i>
                </label>
              </th>
              <th style="padding:10px">German</th>
              <th>English</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="vocab in vocabList" :key="vocab.german">
              <td>
                <label class="form-checkbox">
                  <input type="checkbox" :value="vocab.german" v-model="selected">
                  <i class="form-icon"></i>
                </label>
              </td>
              <td style="padding-left:10px">{{vocab.german}}</td>
              <td>{{vocab.english}}</td>
              <td>
                <v-btn small @click="edit(vocab.german, vocab.english)">Edit</v-btn>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </v-flex>
  </v-layout>
</template>

<script>
/* eslint-disable */
import { validationMixin } from "vuelidate";
import { required } from "vuelidate/lib/validators";
import axios from "axios";

export default {
  mixins: [validationMixin],

  validations: {
    german: { required },
    english: { required }
  },

  data() {
    return {
      selected: [],
      selectAll: false,
      german: "",
      english: "",
      vocabList: [],
      duplicateAlert: false,
      editMode: false,
      editedVocab: ""
    };
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
    setVocabList(data) {
      this.vocabList = data;
      debugger
    },

    loadVocab() {
      let setVocabList = this.setVocabList;
      axios
        .get("http://127.0.0.1:8000/api/v1/vocabs/personal/")
        .then(function(response) {
          setVocabList(response.data);
        });
    },
    submitAdd() {
      if (this.german == "" || this.english == "") {
        return;
      }
      console.log("Submit add");
      this.$v.$touch();
      axios
        .post("http://127.0.0.1:8000/api/v1/vocabs/personal/", {
          german: this.german,
          english: this.english
        })
        .then(function(responseData) {
          var edited = JSON.parse(responseData.bodyText).edited;
          if (edited == "False") {
            this.duplicateAlert = true;
          } else {
            this.duplicateAlert = false;
          }
          this.loadVocab();
          this.clear();
        });
    },
    submitEdit() {
      if (this.german == "" || this.english == "") {
        return;
      }
      console.log("Submit edit");
      this.$v.$touch();
      axios
        .put("http://127.0.0.1:8000/api/v1/vocabs/personal/", {
          germanOld: this.editedVocab,
          german: this.german,
          english: this.english
        })
        .then(function(responseData) {
          var edited = JSON.parse(responseData.bodyText).edited;
          if (edited == "False") {
            this.duplicateAlert = true;
          } else {
            this.duplicateAlert = false;
          }
          this.loadVocab();
          this.clear();
          this.editedVocab = "";
          this.editMode = false;
        });

      this.editMode = false;
    },
    clear() {
      this.$v.$reset();
      this.german = "";
      this.english = "";
    },
    cancelEdit() {
      this.clear();
      this.editMode = false;
    },
    select() {
      this.selected = [];
      if (!this.selectAll) {
        for (let i in this.vocabList) {
          this.selected.push(this.vocabList[i].german);
        }
      }
    },
    deleteSelected() {
      console.log("delete selected vocabs: " + JSON.stringify(this.selected));
      axios
        .delete("http://127.0.0.1:8000/api/v1/vocabs/personal/", {
          body: { items: this.selected }
        })
        .then(function() {
          this.selected = [];
          this.loadVocab();
          this.clear();
        });
    },
    edit(german, english) {
      console.log("Edit vocab: " + german + ", " + english);
      this.editMode = true;
      this.german = german;
      this.english = english;
      this.editedVocab = german;
    }
  },
  beforeMount: function() {
    console.log(
      "Loading vocab with token: " +
        axios.defaults.headers.common["Authorization"]
    );
    this.loadVocab();
  }
};
</script>
