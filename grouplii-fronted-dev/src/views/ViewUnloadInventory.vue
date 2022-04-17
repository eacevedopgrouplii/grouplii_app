<template>
  <div class="home" style="padding-top: 0px;padding-left: 0px;padding-right: 0px;padding-bottom: 0px;" >
    <CompUnLoadInventory></CompUnLoadInventory>
    <font-awesome-icon icon="home"/>
  </div>
</template>


<script>
import CompUnLoadInventory from '../components/CompUnLoadInventory.vue'

export default {
  name: 'Home',
  components: {    
    CompUnLoadInventory
  }
}
</script>