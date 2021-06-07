<template>
    <!-- Double click to get file contents. -->
    <div @dblclick='expand(file.filename)' class='file'>
        <!-- Link to download file. -->
        <h3><a :href="'http://localhost:5000'+ file.link">{{file.filename}}</a></h3>
        <button v-on:click='getStats(file.filename)'>Statistics</button>
        <!-- Hidden until content or statistics are requested. -->
        <Data :class="dataClass" :data='data' />
    </div>
    
</template>

<script>
import Data from './Data'

export default {
    name: 'File',
    props: ['file'],
    components: {
        Data
    },
    data() {
        return {
            dataClass: 'hide',
            data: ''
        }
    },
    methods: {
        async expand(name) {
            const res = await fetch('http://localhost:5000/contents/'+name)
            const data = await res.json()
            this.dataClass = ''
            this.data = data
        },
        async getStats(name) {
            const res = await fetch('http://localhost:5000/stats/'+name)
            const data = await res.json()
            this.dataClass = ''
            this.data = data
        }
    }
}
</script>

<style>
    .file {
        background: lightblue;
        margin: 15px;
        padding: 10px 10px;
    }

    a {
        padding: 5px;
    }

    .hide {
        display: none;
    }
</style>