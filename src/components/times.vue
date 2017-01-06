<template>
  
  <div class="posts">
    
    <div class="main-content">
      <div class="loading" v-if="loading">Loading...</div>
      <div v-if="error" class="error">
        {{ error }}
      </div>
      <transition-group name="slide" class="container-transition">
        <div v-if="posts" v-for='post in posts' class="content" :key="post.id">
          <h2>{{ post.title }}</h2>
        </div>
      </transition-group>
    </div>
    <navigation-buttons prev='/model-config' next='/bpo'></navigation-buttons>
  </div>
</template>

<script>
import VueJsonp from 'vue-jsonp'
import Vue from 'vue'
import VueMaterial from 'vue-material'
import 'vue-material/dist/vue-material.css'
import NavigationButtons from './navigation-buttons'

Vue.use(VueJsonp)
Vue.use(VueMaterial)

export default {
  name: 'posts',
  data () {
    return {
      loading: false,
      posts: [],
      error: null
    }
  },
  components: {
    NavigationButtons
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
  padding: 12px;
  font-size: 30px;
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
.main-content {
  padding: 16px;
  height: 90vh;
  overflow: scroll;
}
@media(max-width: 400px) {
  .content > h2 {
    font-size: 5vw;
  }
}
</style>