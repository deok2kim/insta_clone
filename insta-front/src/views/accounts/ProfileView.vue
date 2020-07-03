<template>
  <div>
      <h1>Profile</h1>
      <p>{{ userInformation.username }}님의 프로필</p>
      <UserInformation :userInformation=userInformation @follow="follow"></UserInformation>
      <UserArticles></UserArticles>
  </div>
</template>

<script>

import UserInformation from '@/components/profileView/UserInformation.vue'
import UserArticles from '@/components/profileView/UserArticles.vue'

import axios from 'axios'
const SERVER_URL = 'http://localhost:8000'



export default {
  name: 'ProfileView',
  components: {
    UserInformation,
    UserArticles
  },

  data() {
    return {
      userInformation: null,
    }
  },
  methods: {
    fetchUserProfile() {
      axios.get(SERVER_URL + `/accounts/${this.$route.params.username}`)
        .then((res) => {
          console.log(res.data)
          
          this.userInformation = res.data
          console.log(this.userInformation.username)
        })
        .catch(()=>{
          this.$router.push({ name: 'Home'})
        })
    },
    follow() {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      axios.post(SERVER_URL + `/accounts/${this.userInformation.username}/follow/`, null, config)
        .then((res) => {
          console.log(res.data)
        })
        .catch(err => console.log(err))
    }
  },

  created() {
    this.fetchUserProfile()
  }
}
</script>

<style>

</style>