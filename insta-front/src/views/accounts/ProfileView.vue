<template>
  <div>
      <h1>Profile</h1>
      <p>{{ userInformation.username }}님의 프로필</p>
      <UserInformation :userInformation=userInformation />
      <UserArticles :userArticles=userArticles />
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
        id: 0,
        username: null,
        isFollow: null,
        articleCount: 0,
      },
      userArticles: null,
    }
  },
  methods: {
    fetchUserProfile() {
      axios.get(SERVER_URL + `/accounts/${this.$route.params.username}`)
        .then((res) => {
          console.log(res.data)
          
          this.userInformation.isFollow = res.data.isFollow
          this.userInformation.id = res.data.id
          this.userInformation.username = res.data.username
        })
        .catch(()=>{
          this.$router.push({ name: 'Home'})
        })
    },
    fetchUserArticles() {
      axios.get(SERVER_URL + `/accounts/${this.$route.params.username}/articles/`)
        .then((res)=>{
          console.log(res.data)
          this.userArticles = res.data
          this.userInformation.articleCount = this.userArticles.length
          console.log(this.userInformation)
        })
        .catch(err => console.log(err))
    }
  },

  created() {
    this.fetchUserProfile()
    this.fetchUserArticles()
  }
}
</script>

<style>

</style>