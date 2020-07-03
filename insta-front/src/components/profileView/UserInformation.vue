<template>
  <div class="userInformation">
	<div>
		사진 자리
	</div>
	<div>
		<h2>User Information</h2>
		<h3>{{userInformation.username}}
			<button v-if="userInformation.isFollow" @click="followSignal">팔로우</button>
			<button v-if="!userInformation.isFollow" @click="followSignal">팔로우 취소</button>
		</h3>
	</div>
  </div>
</template>

<script>


export default {
	name: 'UserInformation',
	props: {
		userInformation: {
			type: Object
		}
	},
	methods: {
		followSignal() {
			this.$emit('follow')
		}
	}
}
</script>

<style scoped>
.userInformation {
 border: 1px solid red;
}
</style>