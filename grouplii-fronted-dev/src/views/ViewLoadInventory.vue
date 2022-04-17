<template>
  <div class="home" style="padding-top: 0px;padding-left: 0px;padding-right: 0px;padding-bottom: 0px;" >
    <CompLoadInventory></CompLoadInventory>
    <font-awesome-icon icon="home"/>
  </div>
</template>


<script>
import CompLoadInventory from '../components/CompLoadInventory.vue'

export default {
  name: 'Home',
  components: {    
    CompLoadInventory
  }
}
</script>