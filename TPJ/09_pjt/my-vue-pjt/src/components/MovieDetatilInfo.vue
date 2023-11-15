<template>
  <div class="card mb-3 mx-auto" style="max-width: 1240px">
    <div class="row g-0">
      <div class="col-md-4">
        <img
          :src="movieURL + movie.poster_path"
          alt="alt"
          class="img-fluid rounded-start"
        />
      </div>
      <div class="col-md-8">
        <div class="card-body">
          <h2 class="card-title">{{ movie.title }}</h2>
          <p class="card-text">인기 : {{ movie.popularity }}</p>
          <p class="card-text">상영시간 : {{ movie.runtime }} 분</p>
          <p class="card-text">{{ movie.overview }}</p>
          <p class="card-text">
            <small class="text-body-secondary"></small>관객 평점 :
            {{ movie.vote_average }}
          </p>
          <img
            src="../assets/youtubeimg.png"
            alt="유튜브썸네일"
            @click="statusModal = !statusModal"
          />
          <YoutubeTrailerModel
            v-if="statusModal"
            :movie="movie"
            @close-modal="statusModal = !statusModal"
          />
        </div>
      </div>
    </div>
  </div>
</template>
<!-- 모달 페이지 설정 -->
<script setup>
import { ref } from 'vue';
import { useRoute } from 'vue-router';
import axios from 'axios';
import YoutubeTrailerModel from '@/components/YoutubeTrailerModel.vue';

const route = useRoute();
const movie = ref([]);
console.log(movie);
const movieId = route.params.movieId;
const movieURL = `https://image.tmdb.org/t/p/w500/`;
// const movieDetail = ref([])
const statusModal = ref(false);

// 옵션-엑시오스까지 비디오 True로 바꿔서 TMDB 독스에서 다시 받아와서 바꿔주기
const options = {
  method: 'GET',
  url: `https://api.themoviedb.org/3/movie/${movieId}`,
  params: { language: 'ko-kr' },
  headers: {
    accept: 'application/json',
    Authorization:
      'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1YjEyYjM3ZDdiMDQ0YzZhN2ExNjQzOTQ2N2NmNGJhZiIsInN1YiI6IjY1NGRjYmRhNjdiNjEzMDEzYzRiNmFmOCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.cuqYitqq9vebaZFYVeGRdvuzDX5q-GyQNY7z-9o5Tus',
  },
};

axios
  .request(options)
  .then(function (response) {
    console.log(response.data);
    movie.value = response.data;
  })
  .catch(function (error) {
    console.error(error);
  });
</script>

<style scoped></style>
