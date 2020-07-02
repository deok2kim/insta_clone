<template>
  <div id="app">
    <div id="nav">
      <router-link to="/">Home</router-link> | 
      <router-link v-if="!isLoggedIn" :to="{ name:'Login' }">Login | </router-link>
      <router-link v-if="!isLoggedIn" :to="{ name:'Signup' }">Signup | </router-link>

      <router-link v-if="isLoggedIn" @click.native="logout" to="/accounts/logout">Logout | </router-link>

      <!-- Article -->
      <router-link :to="{ name:'ArticleList' }">Article | </router-link>
      <router-link v-if="isLoggedIn" :to="{ name:'ArticleCreate' }" >Create | </router-link>
    </div>
    <router-view @submit-login-data="login" 
                 @submit-signup-data="signup" />
  </div>
</template>

<script>
import axios from 'axios'
const SERVER_URL = 'http://localhost:8000'


export default {
  name: 'App',
  data() {
    return {
      isLoggedIn: false,
    }
  },

  methods: {
    setCookie(token) {
      this.$cookies.set('auth-token', token)
    },

    signup(signupData) {
      axios.post(SERVER_URL + '/rest-auth/signup/', signupData)
        .then((res)=>{
          console.log('회원가입 성공')
          this.setCookie(res.data.key)
          this.isLoggedIn = true
          this.$router.push({ name: 'Home' })
        })
    },

    login(loginData) {
      axios.post(SERVER_URL + '/rest-auth/login/', loginData)
        .then((res)=>{
          console.log('로그인 성공')
          this.setCookie(res.data.key)
          this.isLoggedIn = true
          this.$router.push({ name: 'Home' })

        })
        .catch((err)=>{
          console.log(err.response)
        })

    },

    logout() {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      axios.post(SERVER_URL + '/rest-auth/logout/', null, config)
        .then(()=>{
          console.log('로그아웃 성공')
          this.$cookies.remove('auth-token')
          this.isLoggedIn = false
          this.$router.push({ name:'Home' })
        })
        .catch(err => console.log(err))
    }

  },

  mounted() {
    this.isLoggedIn = this.$cookies.isKey('auth-token')
  }
}
</script>


<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
