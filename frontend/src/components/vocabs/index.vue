<template>
  <div id="vocabsPage">
    <v-layout row>
      <v-flex xs6 id="vocabEdit" theme--light teal lighten-5>
        <v-layout column>
          <h1 v-if="editMode">Edit vocabulary</h1>
          <h1 v-else>Add new vocabulary</h1>
          <v-form v-model="valid">
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
          </v-form>
          <v-alert :value="duplicateAlert" type="error">Vocab already exists.</v-alert>
          <v-container fluid grid-list-md>
            <v-layout row wrap>
              <v-flex d-flex sm7 xs12>
                <v-img v-if="mainImg!=null" height="150px" width="150px" :src="mainImg"></v-img>
              </v-flex>
              <v-flex v-if="images.length>0" d-flex sm5 xs12>
                <v-layout row wrap>
                  <v-img
                    v-for="img in images"
                    :key="img"
                    height="75px"
                    width="65px"
                    class="thumbnail"
                    :src="img"
                    @click="selectImg(img)"
                  ></v-img>
                </v-layout>
              </v-flex>
            </v-layout>
          </v-container>
        </v-layout>
      </v-flex>
      <v-flex xs6>
        <!-- VocabBar.vue -->
        <div id="vocab-bar"></div>
        <!-- VocabList.vue  -->
        <div id="vocab-list"></div>
      </v-flex>
    </v-layout>
  </div>
</template>

<script>
/* eslint-disable */
import Vue from "vue";
import { validationMixin } from "vuelidate";
import { required } from "vuelidate/lib/validators";
import axios from "axios";
import VocabBar from "./VocabBar";
import VocabList from "./VocabList";
import _ from "lodash";

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
      valid: false,
      images: [],
      mainImg: null
    };
  },

  watch: {
    english: _.debounce(function() {
      if(this.valid && this.english!=""){
        this.searchVocab();
      }      
    }, 600)
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
    searchVocab() {
      if (this.valid) {
        this.$http
          .get("https://pixabay.com/api/", {
            params: {
              key: "13199466-27d2c444fb6b20f46562bd57c",
              image_type: "photo",
              per_page: "3",
              q: `${this.english}`
            }
          })
          .then(response => {
            let data = response.data.hits;
            this.setImageOptions(data);
          });
      }
    },
    setImageOptions(data) {
      this.images = [];
      for (var i = 0; i < data.length; i++) {
        this.images[i] = data[i].largeImageURL;
      }
      if(this.mainImg == null){
        this.mainImg = this.images[0];
      }      
    },
    selectImg(img) {
      this.mainImg = img;
    },
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
          english: this.english,
          imgUrl: this.mainImg
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
          english: this.english,
          imgUrl: this.mainImg
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
      this.mainImg = null;
      this.images = [];
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
    edit(vocab) {      
      this.editMode = true;
      this.german = vocab.german;
      this.english = vocab.english;
      this.editedVocab = vocab.german;
      console.log("Edit vocab: " + vocab.german + ", " + vocab.english + ", " + vocab.pictureUrl);
      this.selectImg(vocab.pictureUrl);
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
    let vocabBarComponent = new VocabBarClass();
    vocabBarComponent._data.vocabsObj = this;
    vocabBarComponent.$mount("#vocab-bar");
    var VocabListClass = Vue.extend(VocabList);
    let vocabListComponent = new VocabListClass();
    vocabListComponent._data.vocabsObj = this;
    vocabListComponent.$mount("#vocab-list");
  }
};
</script>

<style>
.thumbnail:hover {
  opacity: 0.5;
  cursor: pointer;
}
</style>
