<template>
    <li class="user">
        {{user.id}} {{user.name}} {{user.job}}
    </li>
</template>

<script>
// import axios from 'axios'

export default {
    name: 'UserEntry',
    props: {
        user: String
    },
}
</script>

<style scoped>
.user {
    
}
</style>