<template>
  <div class="">
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
import { getPost } from './api'

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
      getPost(this.$route.params.id, (err, post) => {
        this.loading = false
        if (err) {
          this.error = err.toString()
        } else {
          this.post = post
        }
      })
    }
  }
}
</script>

<style>
.loading {
  position: absolute;
  top: 10px;
  right: 10px;
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