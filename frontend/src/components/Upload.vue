<template>
    <div id='upload'>
        <h1>Upload a CSV File</h1>
        <input type="file" id="file" ref="file" v-on:change="setFile()"/>
        <button v-on:click="fileUpload()">Upload</button>
    </div>
</template>

<script>
import axios from "axios";

export default {
    name: 'Upload',
    emits: ['upload'],
    data() {
        return {
            file: null
        };
    },
    methods: {
        setFile() {
            this.file = this.$refs.file.files[0]
        },

        async fileUpload() {
            let formData = new FormData()
            formData.append('file', this.file)
            await axios.post('http://localhost:5000/upload', formData, {headers:{'Content-Type': 'multipart/form-data'}})
            //Sends event to parent to cause Files rerender
            this.$emit('upload')
        }
    }

}
</script>

<style scoped>
#upload {
    border-style: groove;
    margin: 15px;
    padding: 10px 10px;
}
</style>
