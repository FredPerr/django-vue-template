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
import axios from 'axios'
import UserEntry from '@/components/UserEntry.vue'


export default {
  name: 'HomeView',
  components: {
    UserEntry
  },
  data(){
    return {
      users: null
    }
  },
  mounted(){
    axios.get('http://localhost:8000/user')
    .then((response)=> (this.users = response.data))
    .catch((error) => console.error(error))
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
