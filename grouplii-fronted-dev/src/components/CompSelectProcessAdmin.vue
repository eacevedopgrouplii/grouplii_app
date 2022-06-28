<template>
<div class="card mb-3 ">
  <div class="card-header">Seleccione el tipo de proceso</div>
  <div class="card-body" >
    <ul class="list-group list-group-flush">
    <a class="list-group-item list-group-item-action" id="list-home-list" data-toggle="list" href="new_inventory  " role="tab" aria-controls="home">Nuevo Inventario</a>
    <a class="list-group-item list-group-item-action" id="list-profile-list" data-toggle="list" href="follow_inventory  " role="tab" aria-controls="profile">Seguir Inventario</a>
    <b-button v-b-modal.modal-1 class="list-group-item list-group-item-action" role="tab" aria-controls="messages" >Crear Usuario</b-button>
  </ul>
  </div>
  <b-modal id="modal-1" title="Crear Usuario">
      <form @submit="onSubmit" >
    <p class="h4 text-center mb-4">Sign up</p>
    <div class="grey-text">

      <b-form-input label="Your name" icon="user" type="text" v-model="form.username" placeholder="Ingresar UserName" />
      <b-form-input label="Your email" icon="envelope" type="email" v-model="form.email" placeholder="Ingresar Correo" />
      <b-form-input label="Your password" icon="lock" type="password" v-model="form.password" placeholder="Ingresar Contraseña" />
      <b-form-input label="Your role" icon="user" type="text" v-model="form.role" placeholder="Ingresar Role Usuario" />
    </div>
    <div class="text-center">
      <b-button type="submit" color="primary">Registrar Usuario</b-button>
    </div>
  </form>   
  </b-modal>    
</div>



</template>

<script>
import axios from 'axios'
export default {
    name: 'SelectProcess',
    data() {
      return {
        status: 'No subir imágenes',
        form: {
          username: '',
          email: '',
          password: '',
          role: ''
        }
      }
    },
    methods : {
        onSubmit(event) {
        event.preventDefault()
        axios.post('https://container-grouplii-backend-uymd3d36pa-uc.a.run.app/register', this.form )
        .then(data =>{
            console.log(data);
        } )
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