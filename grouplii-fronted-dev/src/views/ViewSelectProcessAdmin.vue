<template>
  <div class="home" style="padding-top: 0px;padding-left: 0px;padding-right: 0px;padding-bottom: 0px;" >
    <CompSelectProcessAdmin></CompSelectProcessAdmin>      
    <font-awesome-icon icon="home"/>
  </div>
</template>


<script>
import CompSelectProcessAdmin from '../components/CompSelectProcessAdmin.vue'

export default {
  name: 'Home',

  components: {    
    CompSelectProcessAdmin
  }

}
</script>