<template>
    <div class="model-config">
        <md-input-container>
            <label>Generations</label>
            <md-input type="number"></md-input>
        </md-input-container>
        <md-input-container>
            <label>Offsprings</label>
            <md-input type="number"></md-input>
        </md-input-container>
        <navigation-buttons prev='/' next='/times'></navigation-buttons>
    </div>
</template>
<script>
import Vue from 'vue'
import VueMaterial from 'vue-material'
import 'vue-material/dist/vue-material.css'
import NavigationButtons from './navigation-buttons'

Vue.use(VueMaterial)

export default {
  name: 'model-config',
  data () {
    return {
    }
  },
  components: {
    NavigationButtons
  }
}
</script>
<style>
.model-config {
    padding: 20px;
}
</style>