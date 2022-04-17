<template>
  <div class="home" style="padding-top: 0px;padding-left: 0px;padding-right: 0px;padding-bottom: 0px;" >
    <CompStepInventory></CompStepInventory>
    <font-awesome-icon icon="home"/>
  </div>
</template>

<script>
import CompStepInventory from '../components/CompStepInventory.vue'

export default {
  name: 'Home',
  components: {    
    CompStepInventory
  }
}
</script>