<template>
  <div>
    <h3>자식 페이지</h3>
    <p>이름 : {{ child.name }}</p>
    <p>나이 : {{ child.age }}</p>
  </div>
</template>

<script setup>
  defineProps({  // 메서드 즉 함수를 호출하고 인자를 넘김 반환값이 있다.
    child: Object
  })
  // console.log(props)
</script> 

<style scoped>

</style>