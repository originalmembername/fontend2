/* eslint-disable */

import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    status: '',
    token: localStorage.getItem('token') || '',
    user: localStorage.getItem('user') || '',
  },
  mutations: {
    auth_request(state) {
      state.status = 'loading'
    },
    auth_success(state, payload) {
      state.status = 'success'
      state.token = payload.token
      state.user = payload.user
    },
    auth_error(state) {
      state.status = 'error'
    },
    logout(state) {
      state.status = ''
      state.token = ''
      state.user = ''
    },

  },
  actions: {
    login({ commit }, user) {
      return new Promise((resolve, reject) => {
        commit('auth_request')
        let username = user.username
        let password = user.password
        axios
          .post("http://localhost:8000/login/", {
            username: username,
            password: password
          })
          .then(function (resp) {
            console.log(resp)
            const token = resp.data.token
            const user = username
            localStorage.setItem('token', token)
            localStorage.setItem('user', user)
            axios.defaults.headers.common['Authorization'] = token
            commit('auth_success', {
              token: token,
              user: user
            })
            resolve(resp)
          })
          .catch(err => {
            commit('auth_error')
            localStorage.removeItem('token')
            localStorage.removeItem('user')
            reject(err)
          })
      })
    },
    logout({ commit }) {
      // eslint-disable-next-line
      return new Promise((resolve, reject) => {
        commit('logout')
        localStorage.removeItem('token')
        delete axios.defaults.headers.common['Authorization']
        resolve()
      })
    },
    register({ commit }, user) {
      return new Promise((resolve, reject) => {
        commit('auth_request')
        axios({ url: 'http://localhost:3000/register', data: user, method: 'POST' })
          .then(resp => {
            const token = resp.data.token
            const user = resp.data.user
            localStorage.setItem('token', token)
            axios.defaults.headers.common['Authorization'] = token
            commit('auth_success')
            resolve(resp)
          })
          .catch(err => {
            commit('auth_error', err)
            localStorage.removeItem('token')
            reject(err)
          })
      })
    },

  },
  getters: {
    isLoggedIn: state => !!state.token,
    authStatus: state => state.status,
  }
})
