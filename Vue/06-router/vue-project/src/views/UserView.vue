<template>
  <div>
    <h1>UserView</h1>
    <h2>{{ $route.params.id }}번 USER 페이지</h2>
    <h2>{{ userId }}번 스트립트 이용</h2> <!--밑에 스크립트에서 임포트 받아와서 하기 -->
    <button @click="goHome">홈으로!</button>
    <button @click="goAnotherUser">100번 유저 페이지로!</button>
  </div>
</template>

<script setup>
import {ref} from 'vue'
import { useRoute, useRouter, onBeforeRouteLeave, onBeforeRouteUpdate } from 'vue-router'

const route = useRoute()
const userId = ref(route.params.id)

// 플로그래밍 방식 네비게이션
const router = useRouter()

const goHome = function() {
  // router.push({ name: 'home'})
  router.replace({ name:'home'})
}

  // In-component Guard 온 비포라우트 리브 임포트 넣기
  // 1.
  onBeforeRouteLeave((to, from) => {
    const answer = window.confirm('정말 떠나?')  // 확인, 취소로 값을 받음
    if (answer === false) {
      return false
    }
  })

  // 2. onBeforeRouteUpdate => 마찬가지로 임포트 받아오기
  const goAnotherUser = function () {
    router.push({name: 'user', params: {id: 100} })
  }
  // 그냥 저렇게 바꾸면 자바스크립트쪽의 변수는 못따라감
  onBeforeRouteUpdate((to, from) => {
    userId.value = to.params.id
  })
  
</script>

<style scoped>

</style>