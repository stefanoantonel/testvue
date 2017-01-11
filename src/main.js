// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './components/app'
import VueRouter from 'vue-router'
var configroutes = require('./assets/routes.json')

Vue.use(VueRouter)

const router = new VueRouter({
  mode: 'history',
  routes: [
    { path: configroutes.home,
      component: App,
      name: configroutes.home },
    { path: configroutes.bpo.home,
      component: App,
      name: configroutes.bpo.home },
    { path: configroutes.times,
      component: function (resolve) {
        require(['./components/times'], resolve)
      },
      alias: configroutes.bpo.times,
      name: configroutes.times
    },
    { path: configroutes.modelconfig,
      component: function (resolve) {
        require(['./components/model-config'], resolve)
      },
      alias: configroutes.bpo.modelconfig,
      name: configroutes.modelconfig
    },
    { path: configroutes.traces,
      component: function (resolve) {
        require(['./components/traces'], resolve)
      },
      name: configroutes.traces
    }
  ]
})

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  data () {
    return {
    }
  }
})
