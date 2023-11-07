<template>
  <div class="card">
    <h2>앨범 제목</h2>
    <p class="strColor" v-for=" index in 3" :key="index">노래 목록{{ index }}</p>
  </div>
</template>

<script setup>

</script>

<style scoped>
  .card {
    border: 2px solid lightgray;
    background-color: whitesmoke;
  }
  .strColor {
    color: orangered;
  }
</style>