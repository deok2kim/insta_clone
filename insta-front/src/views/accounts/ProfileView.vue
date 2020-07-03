<template>
  <div>
      <h1>Profile</h1>
      <p v-if="userInformation.user">{{ userInformation.user.username }}님의 프로필</p>
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
      userInformation: {
        user: null,
        isFollow: null,
      }
    }
  },
  methods: {
    fetchUserProfile() {
      axios.get(SERVER_URL + `/accounts/${this.$route.params.username}`)
        .then((res) => {
          this.userInformation.user = res.data
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
      axios.post(SERVER_URL + `/accounts/${this.userInformation.user.username}/follow/`, null, config)
        .then((res) => {
          this.userInformation.isFollow = res.data
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