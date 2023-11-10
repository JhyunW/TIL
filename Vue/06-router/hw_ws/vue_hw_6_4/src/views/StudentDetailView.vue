<template>
  <div>
    <h2>학생 상세정보 페이지</h2>
    <p>{{ name }}</p>
  </div>
</template>

<script setup>
import {ref} from 'vue'
import { useRoute } from 'vue-router'
const route = useRoute()
const name = ref(route.params.name)
</script>

<style scoped>

</style>