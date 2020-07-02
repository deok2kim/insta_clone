<template>
  <div>
    <h1>Article Create</h1>
    <div>
      <label for="title">title:</label>
      <input v-model="createData.title" type="text" id="title" />
    </div>
    <div>
      <label for="content">content:</label>
      <textarea v-model="createData.content" id="content"></textarea>
    </div>
    <div>
      <button @click="createArticle">Create</button>
    </div>
  </div>
</template>

<script>
import axios from "axios";
const SERVER_URL = "http://localhost:8000";

export default {
  name: "ArticleCreateView",
  data() {
    return {
      createData: {
        title: null,
        content: null
      }
    }
  },
  methods: {
    createArticle() {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get("auth-token")}`
        }
      }
      axios
        .post(SERVER_URL + "/articles/create/", this.createData, config)
        .then(res => {
          console.log(res)
          this.$router.push({ name: "ArticleList" })
        })
        .catch(err => console.log(err))
    },
  },
}
</script>

<style>
</style>