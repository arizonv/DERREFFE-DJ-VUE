<template>
  <div>
    <h1>Lista de usuarios</h1>
    <ul>
      <li v-for="user in users" :key="user.id">
        {{ user.username }} /
        {{ user.email }} /
        {{ user.is_staff }}
      </li>
    </ul>
  </div>
</template>

<script>
import ApiUsers from '@/service_api/ApiUsers';

export default {
  name: 'Home',
  data() {
    return {
      users: [],
    };
  },
  async created() {
    this.users = await ApiUsers.getUser();

  },
};
</script>
