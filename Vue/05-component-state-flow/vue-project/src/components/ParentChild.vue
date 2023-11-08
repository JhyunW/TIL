<template>
  <div>
    <p>{{ myMsg }}</p>
    <p>{{ dynamicProps }}</p>
    <ParentGrandChild  
    :my-msg="myMsg"
    @update-name="updateName"/>  <!--동적 바인딩 해야함.-->

    <button @click="$emit('someEvent')">클릭</button>  <!--눌러서 소리침-->
    <button @click="buttonClick">클릭선언식</button>
    <button @click="emitArgs">추가 인자 전달</button>
  </div>
</template>

<script setup>
import ParentGrandChild from '@/components/ParentGrandChild.vue';
  // 문자열을 이용한 선언
  // defineProps(['myMsg'])

  // 객체를 사용한 선언
  // defineProps({
  //   myMsg: String,  // 유효성 검증
  // })

  // Props 데이터를 script에서 사용하려면
  const props = defineProps({
    myMsg: String,
    dynamicProps: String,
  })

  console.log(props)
  console.log(props.myMsg)

  // emit 선언 방식
  const emit = defineEmits(['someEvent', 'emitArgs', 'updateName'])

  const buttonClick = function() {
    emit('someEvent')
  }

  const emitArgs = function () {
    emit('emitArgs', 1, 2, 3)
  }

  const updateName = function () {
    emit('updateName')
  }
</script>

<style scoped>

</style>