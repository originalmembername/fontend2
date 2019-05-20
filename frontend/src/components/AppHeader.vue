<template>
  <v-toolbar>
    <v-menu offset-y content-class="dropdown-menu" transition="slide-y-transition">
      <v-toolbar-side-icon slot="activator"></v-toolbar-side-icon>
      <v-card>
        <v-list>
          <v-list-tile v-for="(item, index) in menuItems" :key="index">
            <v-list-tile-title>
              <router-link :to="item.href" tag="button">{{item.title}}</router-link>
            </v-list-tile-title>
          </v-list-tile>
        </v-list>
      </v-card>
    </v-menu>
    <v-toolbar-title>
      <v-btn flat :href="&quot;/&quot;">Language Teaching and Translation</v-btn>
    </v-toolbar-title>
    <v-spacer></v-spacer>
    <v-toolbar-items class="hidden-sm-and-down">
      <v-btn flat href="/about">About</v-btn>
      <v-btn v-if="!this.$store.getters.isLoggedIn" flat href="/login">Login</v-btn>
      <v-btn flat href="/vocabs">Vocabs</v-btn>
    </v-toolbar-items>
  </v-toolbar>
</template>

<script>
export default {
  data: () => ({
    menuItems: [
      { title: "About", href: "/about" },
      { title: "Login", href: "/login" },
      { title: "Vocabs", href: "/vocabs" }
    ]
  })
};
</script>
