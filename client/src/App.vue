<template>
  <Menu/>
  <Panel/>
</template>

<script>
import Menu from '@/modules/components/Menu.vue'
import Panel from "@/modules/components/Panel.vue"

export default {
  name: 'App',
  components: {
    Menu,
    Panel
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  width: 100%;
  height: 100%;
}
</style>
