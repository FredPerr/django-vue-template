<template>
    <li class="user">
        {{user.id}} {{user.name}} {{user.job}}
    </li>
</template>

<script>
export default {
    name: 'UserEntry',
    props: {
        user: {type: Object}
    }
}
</script>

<style scoped>
.user {
    text-align: left;
}
</style>