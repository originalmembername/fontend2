<template>
  <v-layout row wrap>
    <v-flex xs4 id="vocabEdit">
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
    <v-flex xs8 style="max-height:400px; overflow:scroll;" id="vocabList">
      <div id="vocab-bar"></div>
      <div id="vocab-list"></div>
    </v-flex>
  </v-layout>
</template>

<script>
/* eslint-disable */
import Vue from "vue";
import { validationMixin } from "vuelidate";
import { required } from "vuelidate/lib/validators";
import axios from "axios";
import VocabBar from "./VocabBar";
import VocabList from "./VocabList";

export default {
  name: "Vocabs",

  components: {
    VocabBar,
    VocabList
  },

  name: "VocabsVue",

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
      editedVocab: "",
      vocabBarComponent: null
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
    setEditedVocab(vocab) {
      this.editedVocab = vocab;
    },
    setDuplicateAlert(value) {
      this.duplicateAlert = value;
    },
    setVocabList(data) {
      this.vocabList = data;
    },
    setEditMode(value) {
      this.editMode = value;
    },
    setSelected(selected) {
      this.selected = selected;
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
      let setDuplicateAlert = this.setDuplicateAlert;
      let loadVocab = this.loadVocab;
      let clear = this.clear;
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
        .then(function(response) {
          var edited = response.data.edited;
          if (edited == "False") {
            setDuplicateAlert(true);
          } else {
            setDuplicateAlert(false);
          }
          loadVocab();
          clear();
        });
    },
    submitEdit() {
      if (this.german == "" || this.english == "") {
        return;
      }
      console.log("Submit edit");
      let setDuplicateAlert = this.setDuplicateAlert;
      let setEditedVocab = this.setEditedVocab;
      let setEditMode = this.setEditMode;
      let loadVocab = this.loadVocab;
      let clear = this.clear;
      this.$v.$touch();
      axios
        .put("http://127.0.0.1:8000/api/v1/vocabs/personal/", {
          germanOld: this.editedVocab,
          german: this.german,
          english: this.english
        })
        .then(function(response) {
          var edited = response.data.edited;
          if (edited == "False") {
            setDuplicateAlert(true);
          } else {
            setDuplicateAlert(false);
          }
          loadVocab();
          clear();
          setEditedVocab("");
          setEditMode(false);
        });

      setEditMode(false);
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
    selectAllEl() {
      this.selected = [];
      if (!this.selectAll) {
        for (let i in this.vocabList) {
          this.selected.push(this.vocabList[i].german);
        }
      }
      this.selectAll = !this.selectAll;
    },
    deleteSelected() {
      let clear = this.clear;
      let setSelected = this.setSelected;
      let setVocabList = this.setVocabList;
      console.log("delete selected vocabs: " + JSON.stringify(this.selected));
      axios
        .delete("http://127.0.0.1:8000/api/v1/vocabs/personal/", {
          data: { items: this.selected }
        })
        .then(function(response) {
          setVocabList(response.data.vocabs);
          setSelected([]);
          clear();
        });
    },
    edit(german, english) {
      console.log("Edit vocab: " + german + ", " + english);
      this.editMode = true;
      this.german = german;
      this.english = english;
      this.editedVocab = german;
    },
    getImage(vocab) {
      if (vocab.pictureUrl != null) {
        return vocab.pictureUrl;
      } else {
        return require("../../assets/no-image.jpg");
      }
    }
  },
  beforeMount: function() {
    //Add "Token " if it's not already there
    let token_header = axios.defaults.headers.common["Authorization"];
    if (!/^Token\s\w+/.test(token_header)) {
      axios.defaults.headers.common["Authorization"] = "Token " + token_header;
    }
    console.log(
      "Loading vocab with token: " +
        axios.defaults.headers.common["Authorization"]
    );
    this.loadVocab();
  },
  mounted: function() {
    //Create HTML sub-components
    var VocabBarClass = Vue.extend(VocabBar);
    this.vocabBarComponent = new VocabBarClass();
    this.vocabBarComponent._data.vocabsObj = this;
    this.vocabBarComponent.$mount("#vocab-bar");
    var VocabListClass = Vue.extend(VocabList);
    this.vocabListComponent = new VocabListClass();
    this.vocabListComponent._data.vocabsObj = this;
    this.vocabListComponent.$mount("#vocab-list");
  }
};
</script>

<style>
.thumbnail:hover {
  opacity: 0.5;
  cursor: pointer;
}
</style>
