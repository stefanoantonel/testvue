<template>
  <div class="startapp">
    <transition-group appear name="fade">
      <hello key='hello'></hello>
      <hash key='hash'></hash>
      <section class="column" key='section'>
        <router-link v-bind:to="configroutes.home"><md-button class="md-raised">/</md-button></router-link>
        <router-link v-bind:to="configroutes.times"><md-button class="md-raised">times</md-button></router-link>
        <!--<router-link v-bind:to="configroutes.bpo.times"><md-button class="md-raised">bpo/times</md-button></router-link>-->
        <!--<router-link v-bind:to="configroutes.bpo.home"><md-button class="md-raised">bpo</md-button></router-link>-->
        <router-link v-bind:to="configroutes.modelconfig"><md-button class="md-raised">model-config</md-button></router-link>
        <router-link v-bind:to="configroutes.traces"><md-button class="md-raised">traces</md-button></router-link>
      </section>
    </transition-group>
  </div>
</template>

<script>
const Hello = r => require.ensure([], () => r(require('./hello')), 'group-foo')
const Hash = r => require.ensure([], () => r(require('./hash')), 'group-foo')
import VueMaterial from 'vue-material'
import 'vue-material/dist/vue-material.css'
import Vue from 'vue'
var configroutes = require('../assets/routes.json')

Vue.use(VueMaterial)
export default {
  name: 'startapp',
  data () {
    return {
      configroutes: configroutes
    }
  },
  components: {
    Hello, Hash, VueMaterial
  }
}
</script>

<style>
.startapp {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  background-color: #effff3;
}
.column {
  display: flex;
  justify-content: space-around;
  flex-wrap: wrap;
  align-items: center;
}
.fade-enter-active, .fade-leave-active {
  transition: opacity .5s
}
.fade-enter, .fade-leave-active {
  opacity: 0
}
</style>
