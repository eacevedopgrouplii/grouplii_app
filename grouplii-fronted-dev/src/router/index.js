import Vue from 'vue'
import VueRouter from 'vue-router'
import ViewLogin from '../views/ViewLogin.vue'
import ViewHome from '../views/ViewHome.vue'
import ViewNewInventory from '../views/ViewNewInventory.vue'
import ViewFollowInventory from '../views/ViewFollowInventory.vue'
import ViewSelectProcess from '../views/ViewSelectProcess.vue'
import ViewSelectProcessAdmin from '../views/ViewSelectProcessAdmin.vue'  
import ViewLoadInventory from '../views/ViewLoadInventory.vue'
import ViewUnloadInventory from '../views/ViewUnloadInventory.vue'
import ViewAuth from '../views/ViewAuth.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Login',
    component: ViewLogin
  },
  {
    path: '/home',
    name: 'Home',
    component: ViewHome,
    props: true,
    meta:{requiresAuth:true},
    children :[
      {
        path: 'admin',
        component: ViewSelectProcessAdmin,
        meta:{requiresAuth:true, adminAuth: true, residentAuth: false}
      },
      {   
        path: 'operator',
        component: ViewSelectProcess,
        meta:{requiresAuth:true, adminAuth: false, residentAuth: true}
      },
      {
        path: 'new_inventory',
        component: ViewNewInventory,
        props: true
      },
      {
        path: 'follow_inventory',
        component: ViewFollowInventory
      },
      {
        path: 'load_inventory',
        component: ViewLoadInventory
      },
      {
        path: 'unload_inventory',
        component: ViewUnloadInventory
      }

    ]
  },
  {
    path: '/auth:code?',
    name: 'auth',
    component: ViewAuth
    
  }  
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

router.beforeEach((to, from, next) => {
  if(to.meta.requiresAuth) {
    const authUser = JSON.parse(localStorage.getItem("user") || '[]')
    if(!authUser  ) {
      next({name:'Login'})
    }
    else if(to.meta.adminAuth) {
    const authUser = JSON.parse(localStorage.getItem("user") || '[]')
    if(authUser.data.role === 'admin') {
      next()
    }else {
      next('home/operator')
    }
  } else if(to.meta.residentAuth) {
    const authUser = JSON.parse(localStorage.getItem("user") || '[]')
    if(authUser.data.role === 'operator') {
      next()
    }else {
      console.log('Im in admin')
      next('home/admin')
    }
  }
  }else {
  next()
  }
})



export default router
