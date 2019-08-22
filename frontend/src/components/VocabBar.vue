<template>
  <div id="VocabBar">
    <h1>Vocab List</h1>
    <v-layout row wrap>
      <v-btn small @click="selectAllEl()">Select all</v-btn>
      <v-btn small @click="deleteSelected()">Delete Selected</v-btn>
    </v-layout>
  </div>
</template>

<script>
/* eslint-disable */
import Vocabs from "./Vocabs";

export default {
  data() {
    return {
      vocabsObj: "Insert Vocabs Object here"
    };
  },
  methods: {
    selectAllEl() {
      console.log("select All Vocabs, VocabsBar.vocabsObj: ");
      console.log(this.vocabsObj);
    },
    deleteSelected() {
      console.log("Delete selected vocabs");
    }
  }
};
</script>