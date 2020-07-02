<template>
  <div class="userInformation">
      <h2>User Information</h2>
			<h3>{{user}}</h3>
  </div>
</template>

<script>


export default {
	name: 'UserInformation',
	props: {
		user: {
			type: Object
		}
	}
}
</script>

<style>
div.userInformation {
 border: 1px solid red;
}
</style>