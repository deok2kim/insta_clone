<template>
  <div>
      <h1>Article LIST</h1>
      <ul>
        <li v-for="article in articles" :key="`article_${article.id}`">{{ article.id }} - {{ article.title }}</li>
      </ul>
  </div>
</template>

<script>
import axios from 'axios'
const SERVER_URL = 'http://localhost:8000'

export default {
    name: 'ArticleListView',
    data() {
      return {
        articles: []
      }
    },

    methods: {
      fetchArticles() {
        axios.get(SERVER_URL + '/articles/')
          .then((res) => {
            this.articles = [...this.articles, ...res.data]
          })
          .catch(err => console.log(err))
      }
    },

    created() {
      this.fetchArticles()
    }
}
</script>

<style>

</style>