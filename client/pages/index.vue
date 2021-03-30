<template>
  <div class="main-container">
    <p>Index page.</p>
  </div>
</template>

<script>
export default {
  layout: ctx => ctx.$device.isMobile ? 'mobile' : 'default'
}
</script>

<style>
</style>
