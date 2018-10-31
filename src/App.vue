<template>
  <v-app>
    <AppHeader></AppHeader>
    <v-content>
      <MainPage></MainPage>
      <AppFooter></AppFooter>
    </v-content>    
  </v-app>
</template>

<script>
import MainPage from './components/MainPage'
import AppHeader from './components/AppHeader'
import AppFooter from './components/AppFooter'

export default {
  name: 'App',
  components: {
    MainPage,
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
