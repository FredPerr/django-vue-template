<template>
  <div class="home">
    <h2>Registered Users</h2>
    <ul>
      <UserEntry 
      v-for="user in users" 
      :key="user.id" 
      :user="user"/>
    </ul>
  </div>
</template>

<script>
// @ is an alias to /src
import UserEntry from '@/components/UserEntry.vue'


export default {
  name: 'HomeView',
  components: {
    UserEntry
  },
  data(){
    return {
      users: [
        {id: 0, name: 'user 1', job:'job 1'},
        {id: 1, name: 'user 2', job:'job 2'},
        {id: 2, name: 'user 3', job:'job 3'},
      ]
    }
  }
}
</script>

<style scoped>
.home {
  width: 20rem;
  border: 1px solid black;
  border-radius: 3rem;
}
</style>
