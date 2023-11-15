<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>
<template>
  <nav id="navbar-example2" class="navbar bg-body-tertiary px-3 mb-3">
      <h1 class="navbar-brand" href="#"> MovieList🎞 </h1>
      <nav class="nav nav-pills">
      <RouterLink class="nav-item" to="/">Home</RouterLink>
      <RouterLink class="nav-item" to="/movies">전체 영화 목록</RouterLink>
      <RouterLink class="nav-item" to="/review-search">검색 및 출력</RouterLink>
      <RouterLink class="nav-item" to="/recommended">날씨 기반 영화 추천</RouterLink>
      </nav>
    </nav>
  <RouterView />
</template>

<style scoped>
.nav-item {
  padding: 10px 15px; /* 상하 10px, 좌우 15px 간격 */
  background-color: darkgray; /* 배경색 */
  color: black; /* 글자색 */
  border-radius: 5px; /* 라운드 처리 */
  margin: 5px; /* 아이템 간격 */
  text-decoration: none; /* 밑줄 제거 */
  display: inline-block; /* 인라인 블록 요소로 변경하여 너비와 높이 설정 가능 */
}

.nav-item:hover {
  background-color: gray; /* 마우스 호버 시 배경색 변경 */
}


</style>
