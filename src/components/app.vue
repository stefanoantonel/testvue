<template>
  <div id="app2">
    <transition-group appear name="fade">
      <hello key='hello'></hello>
      <hash key='hash'></hash>
      <section class="column" key='section'>
        <router-link to="/times"><md-button class="md-raised">/times</md-button></router-link>
        <router-link to="/bpo/times"><md-button class="md-raised">/bpo/times</md-button></router-link>
        <router-link to="/"><md-button class="md-raised">/</md-button></router-link>
        <router-link to="/bpo"><md-button class="md-raised">/bpo</md-button></router-link>
        <router-link to="/model-config"><md-button class="md-raised">/model-config</md-button></router-link>
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

Vue.use(VueMaterial)
export default {
  name: 'app2',
  components: {
    Hello, Hash, VueMaterial
  }
}
</script>

<style>
#app2 {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
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
