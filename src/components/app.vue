<template>
  <div id="app2">
    <transition-group appear name="fade">
      <hello key='hello'></hello>
      <hash key='hash'></hash>
      <section class="column" key='section'>
        <router-link to="/times">/times</router-link>
        <router-link to="/bpo/times">/bpo/times</router-link>
        <router-link to="/">/</router-link>
        <router-link to="/bpo">/bpo</router-link>
      </section>
    </transition-group>
  </div>
</template>

<script>
const Hello = require('./hello')
const Hash = require('./hash')

export default {
  name: 'app',
  components: {
    Hello, Hash
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
