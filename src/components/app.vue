<template>
  <div id="app2">
    <img src="../assets/logo.png">
    <hello></hello>
    <section class="column">
      <hash></hash>
<!--      <times></times>
      <router-link to="/times">/times</router-link>-->
    </section>
  </div>
</template>

<script>
import Hello from './hello'
import hash from './hash'
// import times from './times'

export default {
  name: 'app',
  components: {
    Hello, hash
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
.column {
  display: flex;
  justify-content: space-around;
  flex-wrap: wrap;
  align-items: center;
}
</style>
