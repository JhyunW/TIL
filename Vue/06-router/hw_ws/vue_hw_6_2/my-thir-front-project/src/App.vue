<script setup>
import { RouterLink, RouterView } from 'vue-router'
import { ref } from 'vue'
import MainPage from './components/MainPage.vue';
</script>

<template>
   <MainPage />
  <header>
      <nav>
        <RouterLink :to="{ name: 'someview' }">someview</RouterLink> |
        <RouterLink :to="{ name: 'otherview' }">otherview</RouterLink>

      </nav>
  </header>

  <RouterView />
</template>

<style scoped>

</style>
