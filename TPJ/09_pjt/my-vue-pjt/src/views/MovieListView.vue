<template>
  <h2>평점 내림차순</h2>
  <div class="row row-cols-1 row-cols-md-3 g-4">
    <div v-for="movie in movies" :key="movie.id" class="col" @click="goDetail(movie)">
      <div class="card h-100">
        <img :src="movieURL + movie.poster_path" alt="" class="card-img-top">
        <div class="card-body">
          <h5 class="card-title">{{ movie.title }}</h5>
          <!-- <p class="card-text">{{ movie.release_date }}</p> -->
          <p class="card-text">{{ movie.overview }}</p>
          <!-- <p class="card-text">{{ movie.vote_count }}</p> -->
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import axios from 'axios'


const router = useRouter()
const movies = ref([])
const movieURL = 'https://image.tmdb.org/t/p/w500'  // 이미지의 주소
const options = { // docs에서 가져온 URL
  method: 'GET',
  url: 'https://api.themoviedb.org/3/movie/top_rated',
  params: { language: 'ko-kr', page: '1' },
  headers: {
    accept: 'application/json',
    Authorization: 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1YjEyYjM3ZDdiMDQ0YzZhN2ExNjQzOTQ2N2NmNGJhZiIsInN1YiI6IjY1NGRjYmRhNjdiNjEzMDEzYzRiNmFmOCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.cuqYitqq9vebaZFYVeGRdvuzDX5q-GyQNY7z-9o5Tus'
  }
};
const goDetail = (movie) => {
  router.push(`/${movie.id}`)
}

axios
  .request(options)
  .then(function (response) {
    console.log(response.data.results)
    movies.value = response.data.results
  })
  .catch(function (error) {
    console.error(error)
  })
</script>

<style scoped></style>