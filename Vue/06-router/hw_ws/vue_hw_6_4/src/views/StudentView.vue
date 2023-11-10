<template>
  <div>
    <h1>학생 목록</h1>
    <ul>
      <li v-for="student in students" :key="student.name">
        <p @click="moveDetail(student.name)"> {{ student.name }} </p>
      </li>
    </ul>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'
const students = [
  { name: '김하나' },
  { name: '김두리' },
  { name: '김서이' },
]

const router = useRouter()

const moveDetail = function (userName) {
  router.push({ name: 'StudentDetailView', params: { name: userName } })
}
</script>

<style scoped></style>