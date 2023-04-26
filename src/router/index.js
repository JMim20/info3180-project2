import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import RegisterForm from '../components/RegisterForm.vue'
import LoginForm from '../components/LoginForm.vue'
import ExploreView from '../views/ExploreView.vue'
const token = localStorage.getItem("token")

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/register',
      name: 'register',
      //Accepts user information and saves it to the database
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/RegisterView.vue'),
      meta: {auth: false}
    },
    {
      path: '/login',
      name: 'login',
      //Accepts login credentials as username and password
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/LoginView.vue'),
      meta: {auth: false}
    },
    {
      path: '/explore',
      name: 'explore',
      //View/Explore all posts by all users
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/ExploreView.vue'),
      meta: {auth: true}
    },
    {
      path: '/Myprofile',
      name: 'Myprofile',
      //View/Explore all posts by all users
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/Myprofile.vue')
    },
    {
      path: '/logout',
      name: 'logout',
      //View/Explore all posts by all users
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/Logout.vue')
    },
    {
      path: '/posts/new',
      name: 'newpost',
      //View/Explore all posts by all users
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../components/NewPostForm.vue')
    }
  ]
  
})
// routing and redirecting all users according to authentication
// routing and redirecting all users according to authentication
router.beforeEach((to, from, next) => {
  if (to.meta.auth && !token) {
    next("/login")
  } else if (!to.meta.auth && token) {
    next("/explore")
  } else {
    next()
  }
})
export default router


