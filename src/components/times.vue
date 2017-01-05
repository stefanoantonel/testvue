<template>
  <div class="time">
    <div class="loading" v-if="loading">Loading...</div>
    <div v-if="error" class="error">
      {{ error }}
    </div>
    <transition name="slide">
      <!--
        giving the post container a unique key triggers transitions
        when the post id changes.
      -->
      <div v-if="info" class="content" :key="info.id">
        <h2>{{ info.time }}</h2>
        <p>{{ info.date }}</p>
      </div>
    </transition>
  </div>
</template>

<script>
import VueJsonp from 'vue-jsonp'
import Vue from 'vue'

Vue.use(VueJsonp)

export default {
  name: 'times',
  data () {
    return {
      loading: false,
      info: null,
      error: null
    }
  },
  created () {
    this.fetchData()
  },
  watch: {
    '$route': 'fetchData'
  },
  methods: {
    fetchData () {
      this.error = this.post = null
      this.loading = true
      this.$jsonp('http://date.jsontest.com/', {}).then(json => {
        this.info = json
        this.loading = false
      }).catch(err => {
        // Failed.
        console.error(err)
      })
    }
  }
}
</script>

<style>
.loading {
  position: absolute;
  font-size: 20px;
}
.error {
  color: red;
}
.content {
  transition: all .35s ease;
  position: absolute;
}
.slide-enter {
  opacity: 0;
  transform: translate(30px, 0);
}
.slide-leave-active {
  opacity: 0;
  transform: translate(-30px, 0);
}
</style>