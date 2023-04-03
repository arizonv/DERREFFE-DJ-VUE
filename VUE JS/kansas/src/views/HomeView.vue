<template>
  <div>
    <HelloWorld msg="Welcome to Your Vue.js App"/>
    <div class="container">
      <table class="table">
        <thead>
          <tr>
            <th scope="col">#</th>
            <th scope="col">Title</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="post in posts" :key="post.id">
            <td>{{ post.id }}</td>
            <td>{{ post.title }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import ApiService from '../service_api/ApiServices';
import HelloWorld from '@/components/HelloWorld.vue'

export default {
  components: {
    HelloWorld
  },
  data() {
    return {
      posts: []
    };
  },
  mounted() {
    this.fetchPosts();
  },
  methods: {
    async fetchPosts() {
      this.posts = await ApiService.getPosts();
    }
  }
};
</script>
