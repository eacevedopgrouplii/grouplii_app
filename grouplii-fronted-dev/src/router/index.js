import Vue from 'vue'
import VueRouter from 'vue-router'
import ViewLogin from '../views/ViewLogin.vue'
import ViewHome from '../views/ViewHome.vue'
import ViewNewInventory from '../views/ViewNewInventory.vue'
import ViewFollowInventory from '../views/ViewFollowInventory.vue'
import ViewSelectProcess from '../views/ViewSelectProcess.vue'
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
    children :[
      {
        path: '',
        component: ViewSelectProcess
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

export default router
