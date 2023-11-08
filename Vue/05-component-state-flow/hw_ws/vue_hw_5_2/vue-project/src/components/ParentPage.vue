<template>
  <div>
    <h1>부모페이지입니다.</h1>
    <ChildPage 
    v-for="child in children"
    :key="child.name"
    :child="child"/>
  </div>
</template>

<script setup>
  import ChildPage from '@/components/ChildPage.vue';
  import {ref} from 'vue';  // 뷰 임포트 받아오기 
  // 각각의 요소는 속성을 가짐
  const children = ref([
    {
      name:'김하나',
      age: 30
    },
    {
      name:'김두리',
      age: 20
    },
    {
      name:'김서이',
      age: 10
    },
  ])
</script>

<style scoped>

</style>