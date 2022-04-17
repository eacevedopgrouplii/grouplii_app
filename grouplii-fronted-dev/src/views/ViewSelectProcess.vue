<template>
  <div class="home" style="padding-top: 0px;padding-left: 0px;padding-right: 0px;padding-bottom: 0px;" >
    <CompSelectProcess></CompSelectProcess>      
    <font-awesome-icon icon="home"/>
  </div>
</template>


<script>
import CompSelectProcess from '../components/CompSelectProcess.vue'

export default {
  name: 'Home',

  components: {    
    CompSelectProcess
  }

}
</script>