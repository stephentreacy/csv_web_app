<template>
  <Upload v-on:upload='renderFiles()'/>
  <Files :key='filesKey' />
</template>

<script>
  import Upload from './components/Upload';
  import Files from './components/Files';

export default {
  name: 'App',
  components: {
    Upload,
    Files
  },
  data() {
    return {
      filesKey: 0
    }
  },
  methods: {
    //Increases the key for Files comonent when a file is uploaded to rerended Files.
    renderFiles() {
      this.filesKey += 1;
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
