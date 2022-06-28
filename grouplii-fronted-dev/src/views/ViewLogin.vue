<template>
  <div class="home">
  <section class="gradient-custom">
  <div class="container py-5 h-100">
    <form v-on:submit.prevent = "login">
    <div class="row d-flex justify-content-center align-items-center h-100">
      <div class="col-12 col-md-8 col-lg-6 col-xl-5">
        <div class="card bg-white text-black" style="border-radius: 1rem;">
          <div class="card-body p-5 text-center">            
            <div class="mb-md-5 mt-md-4 pb-5">
              <img src="@/assets/Logo_grouplii.jpg" > 
              <p class="text-black-50 mb-5">Por favor ingrese usuario y contraseña</p>

              <div class="form-outline form-white mb-4">
                <input class="form-control form-control-lg" v-model="user"/>
                <label class="form-label" for="typeEmailX">Usuario</label>
              </div>

              <div class="form-outline form-white mb-4">
                <input type="password" id="typePasswordX" class="form-control form-control-lg" v-model="password"/>
                <label class="form-label" for="typePasswordX">Contraseña</label>
              </div>             

              <button class="btn btn-login-class btn-lg px-5" type="submit" >Ingresar</button>      

              <div class="alert alert-warning" role="alert" v-if="error">
              {{error_msg}}
            </div>      
            </div>

          </div>
        </div>
      </div>
    </div>
    </form>
  </div>
  </section>
  </div>
</template>

<script>
// @ is an alias to /src
import axios from 'axios'
export default {
  name: 'Home',
  components: {
  },

  data: function(){
    return {
      user: "",
      password: "",
      error: false,
      error_msg: ""
    }
  },
  methods:{
    login(){
      let json = {
        "username" : this.user,
        "password": this.password
      };
      axios.post('https://container-grouplii-backend-uymd3d36pa-uc.a.run.app/login', json )
      .then(data =>{        
        if(data.status == 200){
            localStorage.setItem('user',JSON.stringify(data));
          if(data.data.role == "admin"){
            this.$router.push({ path: '/home/admin' }).catch(()=>{});
          }
          else {
            this.$router.push('home/operator').catch(()=>{});
          }
        } 
      } ) 
    
    }
  }
}
</script>

<style scoped>

.gradient-custom {

  /* Chrome 10-25, Safari 5.1-6 */
  background: -webkit-linear-gradient(to right, rgb(8, 40, 160), rgb(37,73,166));

  /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */
  background: linear-gradient(to right, rgb(8, 40, 160), rgb(37,73,166));

  height: 100vh;
}

.btn-login-class{

  background: rgb(8, 40, 160);
  color: white;
}



body {
    height: 100vh;
}


</style>
