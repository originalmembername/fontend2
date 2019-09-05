<template>
  <v-app>
    <v-content>
      <AppHeader/>
      <router-view style="height:80%"/>
      <span v-if="isLoggedIn">
        <a @click="logout">Logout</a>
      </span>
    </v-content>
  </v-app>
</template>

<script>
import AppHeader from './components/AppHeader'

export default {
  name: 'App',
  components: {
    AppHeader,
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
    if(this.$http.interceptors.response != null) {
      this.$http.interceptors.response.use(undefined, function (err) {
      // eslint-disable-next-line
      return new Promise(function (resolve, reject) {
        if (err.status === 401 && err.config && !err.config.__isRetryRequest) {
          this.$store.dispatch('logout')
        }
        throw err;
      });
    });
    }    
  },
  data () {
    return {
      //
    }
  }
}
</script>
