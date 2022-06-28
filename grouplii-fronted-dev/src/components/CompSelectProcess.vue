<template>
<div class="card mb-3 ">
  <div class="card-header">Seleccione el tipo de proceso</div>
  <div class="card-body" >
    <ul class="list-group list-group-flush">
    <a class="list-group-item list-group-item-action" id="list-home-list" data-toggle="list" href="new_inventory  " role="tab" aria-controls="home">Nuevo Inventario</a>
    <a class="list-group-item list-group-item-  action" id="list-profile-list" data-toggle="list" href="follow_inventory  " role="tab" aria-controls="profile">Seguir Inventario</a>
  </ul>
  </div>    
</div>

</template>

<script>

export default {
    name: 'SelectProcess',
    data() {
      return {
        status: 'No subir imágenes'
      }
    }
}
    

</script>


<style lang="scss" scoped>

@media only screen and (max-width: 1200px) {
  
  .card {
    position: absolute;
    left: 32%;  
    top: 30%;  
    width: 40%;
    height: 25% ;
  }
}

@media only screen and (max-width: 700px) {
  
  .card {
    position: absolute;
    left: 32%;  
    top: 30%;  
    width: 40%;
    height: 60% ;
  }
}



.card-header{
    background-color: rgb(8, 40, 160) ;
    color: rgb(255, 255, 255);
}

.card-body{
    background-color: rgb(255, 255, 255) ;
    color: rgb(0, 0, 0);
}

.card-title{
    font: 12px Verdana, sans-serif;
    font-size-adjust: 0.58;
}
</style>