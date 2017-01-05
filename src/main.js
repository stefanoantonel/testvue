// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
// import App from './App'
import app from './components/app'
import VueRouter from 'vue-router'
import Times from './components/times'

Vue.use(VueRouter)

const router = new VueRouter({
  mode: 'history',
  routes: [
    { path: '/bpo/times', component: Times }
  ]
})

router.beforeEach((to, from, next) => {
  console.debug('To: ', to)
  console.debug('From: ', from)
  next()
})

/* eslint-disable no-new */
new Vue({
  el: '#app',
  components: {
    'app': app
  }
})
