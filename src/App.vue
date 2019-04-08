<template>
  <v-app>
    <v-content>
      <AppHeader/>
      <router-view style="height: 400px"/>
      <span v-if="isLoggedIn">
        |
        <a @click="logout">Logout</a>
      </span>
      <AppFooter/>
    </v-content>
  </v-app>
</template>

<script>
import AppHeader from './components/AppHeader'
import AppFooter from './components/AppFooter'

export default {
  name: 'App',
  components: {
    AppHeader,
    AppFooter
  },
  computed : {
      isLoggedIn : function(){ return this.$store.getters.isLoggedIn}
  },
  methods: {
      logout: function () {
        this.$store.dispatch('logout')
        .then(() => {
          this.$router.push('/login')
        })
      }
  },
  created: function () {
    this.$http.interceptors.response.use(undefined, function (err) {
      // eslint-disable-next-line
      return new Promise(function (resolve, reject) {
        if (err.status === 401 && err.config && !err.config.__isRetryRequest) {
          this.$store.dispatch('logout')
        }
        throw err;
      });
    });
  },
  data () {
    return {
      //
    }
  }
}
</script>
