<template>
  <div class="textOption">
    <h2>가수 목록</h2>
    <SingerDetail />
  </div>
</template>

<script setup>
  import SingerDetail from './singer/SingerDetail.vue';
</script>

<style scoped>
  .textOption {
    text-align: center;
  }
</style>