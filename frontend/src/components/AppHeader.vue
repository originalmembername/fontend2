<template>
  <v-toolbar>
    <v-menu
      class="hidden-md-and-up"
      offset-y
      content-class="dropdown-menu"
      transition="slide-y-transition"
    >
      <v-toolbar-side-icon slot="activator"></v-toolbar-side-icon>
      <v-card>
        <v-list>
          <div v-for="(item, index) in menuItems" :key="index">
            <v-list-tile v-if="showItem(item)">
              <v-list-tile-title>
                <router-link :to="item.href" tag="button">{{item.title}}</router-link>
              </v-list-tile-title>
            </v-list-tile>
          </div>
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
      <v-btn v-if="this.$store.getters.isLoggedIn" flat href="/vocabs">Vocabs</v-btn>
      <v-btn v-if="this.$store.getters.isLoggedIn" flat href="/account">Account</v-btn>
    </v-toolbar-items>
    <span v-if="this.$store.getters.isLoggedIn">
      <p>{{$store.state.user}}</p>
      <a
        @click="function(){
            this.$store.dispatch('logout')
            .then(() => {
            this.$router.push('/login')
          })}"
      >Logout</a>
    </span>
  </v-toolbar>
</template>

<script>
export default {
  data: () => ({
    menuItems: [
      { title: "About", href: "/about", loggedIn: true, loggedOut: true },
      { title: "Login", href: "/login", loggedIn: false, loggedOut: true },
      {
        title: "Vocabs",
        href: "/vocabs",
        loggedIn: true,
        loggedOut: false
      },
      {
        title: "Account",
        href: "/account",
        loggedIn: true,
        loggedOut: false
      }
    ]
  }),
  methods: {
    showItem(item) {
      return (
        (this.$store.getters.isLoggedIn && item.loggedIn) ||
        (!this.$store.getters.isLoggedIn && item.loggedOut)
      );
    }
  }
};
</script>