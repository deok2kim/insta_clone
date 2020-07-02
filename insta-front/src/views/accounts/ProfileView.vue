<template>
  <div>
      <h1>Profile</h1>
      <p v-if="user">{{ user.username }}님의 프로필</p>
      <UserInformation user=user></UserInformation>
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
      user: null
    }
  },
  methods: {
    fetchUserProfile() {
      console.log(this.$route.params.username)
      axios.get(SERVER_URL + `/accounts/${this.$route.params.username}`)
        .then((res) => {
          this.user = res.data
        })
        .catch(()=>{
          this.$router.push({ name: 'Home'})
        })
    }
  },

  created() {
    this.fetchUserProfile()
  }
}
</script>

<style>

</style>