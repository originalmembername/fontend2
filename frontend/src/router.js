import Vue from 'vue'
import Router from 'vue-router'
import MainPage from './components/MainPage.vue'
import About from './components/About.vue'
import Login from './components/Login.vue'
import Vocabs from './components/vocabs/index.vue'
import Account from './components/account'
import Register from './components/Register.vue'
import ImgTest from './components/ImgTest.vue'
import store from './store.js'

Vue.use(Router)

  let router = new Router({
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
      component: Account,
      meta: {
        requiresAuth: true
      }
    },
    {
      path: '/register',
      name: 'register',
      component: Register
    },
    {
      path: '/imgtest',
      name: 'imgtest',
      component: ImgTest
    }
  ]
})

router.beforeEach((to, from, next) => {
  if(to.matched.some(record => record.meta.requiresAuth)) {
    if (store.getters.isLoggedIn) {
      next()
      return
    }
    next('/login') 
  } else {
    next() 
  }
})
export default router
