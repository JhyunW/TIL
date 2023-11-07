<template>
  <div>
    <input type="text" v-model="colorClass">
    <p>{{ colorClass }}</p>
    <!-- 단방향 바인딩으로 색이 입력대로 적용되도록 -->
    <p :class = "colorClass">작성한 내용대로 글자색 변환</p>
  </div>
</template>

<script setup>
import { ref } from 'vue';
const colorClass = ref('test')
</script>

<style scoped>
  .red {
    color: red;
  }

  .blue {
    color: blue;
  }

  .orange {
    color: orange;
  }
  .purple {
    color: purple;
  }

</style>
