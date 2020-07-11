import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import LoginView from '../views/accounts/LoginView.vue'
import SignupView from '../views/accounts/SignupView.vue'
import ArticleListView from '../views/articles/ArticleListView.vue'
import ArticleCreateView from '../views/articles/ArticleCreateView.vue'
import ProfileView from '../views/accounts/ProfileView.vue'

Vue.use(VueRouter)

  const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/accounts/login',
    name: 'Login',
    component: LoginView
  },
  {
    path: '/accounts/signup',
    name: 'Signup',
    component: SignupView
  },
  {
    path: '/articles',
    name: 'ArticleList',
    component: ArticleListView
  },
  {
    path: '/articles/create',
    name: 'ArticleCreate',
    component: ArticleCreateView,
    beforeEnter(from, to, next) {
      if (Vue.$cookies.isKey('auth-token')) {
        next()
      } else {
        next('/accounts/login')
      }
    }
  },
  {
    path: '/:username',
    name: 'Profile',
    component: ProfileView,
  }
  
]









const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router