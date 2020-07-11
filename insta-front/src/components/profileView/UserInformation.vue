<template>
  <div class="userInformation">
	<div>
		사진 자리
	</div>
	<div>
		<h2>User Information</h2>
		<h3>{{ userInformation }}</h3>
			<button v-if="!userInformation.isFollow" @click="follow">팔로우</button>
			<button v-if="userInformation.isFollow" @click="follow">팔로우 취소</button>
		
	</div>
  </div>
</template>

<script>
import axios from 'axios'
const SERVER_URL = 'http://localhost:8000'


export default {
	name: 'UserInformation',
	props: {
		userInformation: {
			type: Object
		}
	},
	methods: {
		follow() {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      axios.post(SERVER_URL + `/accounts/${this.userInformation.username}/follow/`, null, config)
        .then((res) => {
					console.log(res.data)
					this.userInformation.isFollow = !this.userInformation.isFollow
        })
        .catch(err => console.log(err))
    }
	}
}
</script>

<style scoped>
.userInformation {
 border: 1px solid red;
}
</style>