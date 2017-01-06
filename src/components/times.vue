<template>
  <div class="posts">
    <div class="loading" v-if="loading">Loading...</div>
    <div v-if="error" class="error">
      {{ error }}
    </div>
    <transition-group name="slide" class="container-transition">
      <!--<router-link to="/"><- Home</router-link>-->
      <!--
        giving the post container a unique key triggers transitions
        when the post id changes.
      -->
      <div v-if="posts" v-for='post in posts' class="content" :key="post.id">
        <h2>{{ post.title }}</h2>
      </div>
    </transition-group>
  </div>
</template>

<script>
import VueJsonp from 'vue-jsonp'
import Vue from 'vue'

Vue.use(VueJsonp)

export default {
  name: 'posts',
  data () {
    return {
      loading: false,
      posts: [],
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
      this.error = null
      this.posts = []
      this.loading = true
      this.$jsonp('https://jsonplaceholder.typicode.com/posts').then(json => {
        this.handlePost(json)
      }, err => {
        console.error(err)
        // Failed.
      })
    },
    handlePost (json) {
      var posts = this.posts
      // load in cascade with timeout
      var i = 0
      var howManyTimes = json.length
      function f () {
        posts.push(json[i])
        i++
        if (i < howManyTimes) {
          setTimeout(f, 50)
        }
      }
      f()
      this.loading = false
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
  width: 48%;
}
.slide-enter {
  opacity: 0;
  transform: translate(30px, 0);
}
.slide-leave-active {
  opacity: 0;
  transform: translate(-30px, 0);
}
.container-transition {
  display: flex;
  justify-content: space-between;
  flex-wrap: wrap;
}
</style>