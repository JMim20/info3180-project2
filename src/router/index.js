import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import RegisterForm from '../components/RegisterForm.vue'
import LoginForm from '../components/LoginForm.vue'
import ExploreView from '../views/ExploreView.vue'
import Profile from '../components/Profile.vue'
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
     component: () => import('../views/RegisterView.vue'),
     meta: {auth: false}
    },
    {
      path: '/login',
      name: 'login',
      component: () => import('../views/LoginView.vue'),
      meta: {auth: false}
    },
    {
      path: '/explore',
      name: 'explore',
      component: ExploreView.vue,
      meta: {auth: true}
    },
    {
      path: '/users/{user_id}',
      name: 'profile',
      component: Profile.vue
    },
    {
      path: '/logout',
      name: 'logout',
      component: () => import('../views/Logout.vue')
    },
    {
      path: '/posts/new',
      name: 'newpost',
      component: () => import('../components/NewPostForm.vue')
    }
  ]
  
})
// routing and redirecting all users according to authentication
// routing and redirecting all users according to authentication
/**router.beforeEach((to, from, next) => {
  if (to.meta.auth && !token) {
    next("/login")
  } else if (!to.meta.auth && token) {
    next("/explore")
  } else {
    next()
  }
})**/
export default router
