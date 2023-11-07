<template>
  <div>
    <input type="text" ref="input">
  </div>
</template>

<script setup>
import {ref} from 'vue'

const input = ref()

console.log(input.value)

</script>

<style scoped>

</style>