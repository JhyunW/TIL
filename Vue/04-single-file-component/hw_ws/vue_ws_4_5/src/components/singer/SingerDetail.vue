<template>
  <div class="card">
  <div class="bordered">
    <h2>가수 이름</h2>
    <img src="@/assets/singer.jpg" alt="singer" class="imgStyle">
    <p>가수 소개글</p>
    <SingerAlbum v-for="index in 2" :key="index"/>
  </div>
  </div>
</template>

<script setup>
  import SingerAlbum from './SingerAlbum.vue';
</script>

<style scoped>
  .imgStyle{
    width: 200px;
    border-radius: 50%;
  }

  .bordered{
    border: 2px solid black;
  }
  .card{
    display: inline-block;
    width: 40%;
    margin: 20px;
  }
  
</style>