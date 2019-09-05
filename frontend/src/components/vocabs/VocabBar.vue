<template>
  <v-flex id="VocabBar">
    <h1>Vocab List</h1>
    <v-layout row wrap>
      <v-btn small @click="selectAllEl()">Select all</v-btn>
      <v-btn small @click="deleteSelected()">Delete Selected</v-btn>
    </v-layout>
  </v-flex>
</template>

<script>
/* eslint-disable */
import Vocabs from "./index";

export default {
  data() {
    return {
      vocabsObj: "Insert Vocabs Object here"
    };
  },
  methods: {
    selectAllEl() {
      return this.vocabsObj.selectAllEl();
    },
    deleteSelected() {
      return this.vocabsObj.deleteSelected();
    }
  }
};
</script>