<template>
  <div class="userArticles">
      <h2>User Articles</h2>
      <div>
        <ul>
          <li v-for="article in userArticles" :key="article.id">{{article}}</li>
        </ul>
      </div>
  </div>
</template>

<script>
export default {
  name: 'UserArticles',
  props: {
    userArticles: Array
  }
}
</script>

<style>
div.userArticles {
	border: 1px solid blue;
}
</style>