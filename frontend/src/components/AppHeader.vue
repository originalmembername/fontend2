<template>
  <v-toolbar>
    <v-toolbar-side-icon></v-toolbar-side-icon>
    <v-toolbar-title>
      <v-btn
      flat
      :href='&quot;/&quot;'
      >
      Language Teaching and Translation
      </v-btn>
    </v-toolbar-title>
    <v-spacer></v-spacer>
    <v-toolbar-items class="hidden-sm-and-down">
      <v-btn flat href="/about">About</v-btn>
      <v-btn v-if="!this.$store.getters.isLoggedIn" flat href="/login">Login</v-btn>
      <v-btn flat href="/vocabs">Vocabs</v-btn>
    </v-toolbar-items>
  </v-toolbar>
</template>