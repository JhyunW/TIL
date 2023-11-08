<template>
  <div>
    <ParentChild 
      my-msg="message" 
      :dynamic-props="name" 
      @some-event="someCallback"
      @emit-args="getNumbers"
      @update-name="updateName"/> <!--props이름, prop값-->
      
  </div>
</template>

<script setup>
import ParentChild from '@/components/ParentChild.vue';
import { ref } from 'vue'

const name = ref('ALICE')

const someCallback = function() {
  console.log('페어런트 차일드가 발신한 에밋 이벤트를 수신했습니다.')
}
const getNumbers =function(...args) {
  console.log(args)
}
const updateName = function () {
  console.log('뿅')
  name.value = 'Bella'
}
</script>

<style scoped>

</style>