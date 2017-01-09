// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './components/app'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const router = new VueRouter({
  mode: 'history',
  routes: [
    { path: '/', component: App },
    { path: '/bpo/', component: App },
    { path: '/testvue/', component: App },
    { path: '/times',
      component: function (resolve) {
        require(['./components/times'], resolve)
      },
      alias: ['/bpo/times', '/testvue/times']
    },
    { path: '/model-config',
      component: function (resolve) {
        require(['./components/model-config'], resolve)
      },
      alias: ['/bpo/model-config', '/testvue/model-config']
    }
  ]
})

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router
})
