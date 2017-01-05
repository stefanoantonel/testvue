// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
// import App from './App'
import VueRouter from 'vue-router'
import Times from './components/times'
import app from './components/app'

Vue.use(VueRouter)

const router = new VueRouter({
  mode: 'history',
  base: __dirname,
  routes: [
    { path: '/bpo/', component: app },
    { path: '/bpo/times', component: Times }
  ]
})

router.beforeEach((to, from, next) => {
  console.debug('To: ', to)
  console.debug('From: ', from)
})

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: {
    'app': app
  }
})
