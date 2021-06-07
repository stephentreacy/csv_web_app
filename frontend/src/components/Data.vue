<template>
    <div v-html="data">
    </div>
</template>

<script>
export default {
    name: 'Data',
    props: ['data']
}
</script>

<style scoped>
    div {
        height: 200px;
        overflow: scroll;
    }
</style>>
