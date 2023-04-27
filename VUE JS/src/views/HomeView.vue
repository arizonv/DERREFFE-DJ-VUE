<template>
  <div class="home">
    <h1>Posts</h1>
    <ul>
      <li v-for="post in posts" :key="post.id">
        <h2>{{ post.title }}</h2>
        <p>{{ post.body }}</p>
      </li>
    </ul>
  </div>
</template>

<script>
import ApiService from '../service_api/ApiServices';

export default {
  name: 'Home',
  data() {
    return {
      posts: []
    };
  },
  mounted() {
    ApiService.getPosts()
      .then(response => {
        this.posts = response;
      })
      .catch(error => {
        console.log(error);
      });
  },
};
</script>
