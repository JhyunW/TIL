<template>
  <div class="textOption">
    <h1 class="textColor">가수 목록</h1>
    <div class="d-flex justify-content-between">
      <SingerDetail v-for="index in 2" :key="index"/>
    </div>
  </div>
</template>

<script setup>
  import SingerDetail from './singer/SingerDetail.vue';
</script>

<style scoped>
  .textOption {
    text-align: center;
  }
  .textColor {
    color: orangered;
  }
</style>