import Vue from 'vue'
import Router from 'vue-router'
import MainPage from './components/MainPage.vue'
import About from './components/About.vue'
import Login from './components/Login.vue'
import Vocabs from './components/Vocabs.vue'
import HelloWorld from './components/HelloWorld.vue'
import Account from './components/account'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'mainPage',
      component: MainPage
    },
    {
      path: '/about',
      name: 'about',
      component: About
    },
    {
      path: '/login',
      name: 'login',
      component: Login
    },
    {
      path: '/vocabs',
      name: 'vocabs',
      component: Vocabs
    },
    {
      path: '/account',
      name: 'account',
      component: Account
    },
    {
      path: '/helloworld',
      name: 'helloWorld',
      component: HelloWorld
    }
  ]
})
