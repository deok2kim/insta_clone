<template>
  <div>
    <h1>SIGNUP</h1>
    <div>
      <label for="username">username: </label>
      <input v-model="SignupData.username" type="text" id="username">
    </div>
    <div>
      <label for="password1">password1: </label>
      <input v-model="SignupData.password1" type="password" id="password1">
    </div>
    <div>
      <label for="password2">password2: </label>
      <input v-model="SignupData.password2" type="password" id="password2">
    </div>
    <div>
      <button @click="signup">Signup</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'SignupView',
  data() {
    return {
      SignupData: {
        username: null,
        password1: null,
        password2: null,
      }
    }
  },

  methods: {
    signup() {
      this.$emit('submit-signup-data', this.SignupData)
    },
  },
}
</script>

<style>

</style>