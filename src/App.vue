<template>
  <v-app>
    <v-content>
      <AppHeader/>
      <router-view style="height: 400px"/>
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
  data () {
    return {
      //
    }
  }
}
</script>
