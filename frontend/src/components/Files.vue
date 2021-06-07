<template>
    <h1>Files</h1>
    <div :key='file.id' v-for='file in files'>
        <File :file='file' />
    </div>
</template>

<script>
import File from './File'
export default {
    name: 'Files',
    components: {
        File
    },
    data() {
        return {
            files: null
        } 
    },
    async created() {
        this.files = await this.getFiles()
    },
    methods: {
        async getFiles() {
        const res = await fetch('http://localhost:5000/files')
        const data = await res.json()

        return data
        }
    }
}
</script>