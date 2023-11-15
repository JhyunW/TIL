<template>
  <div class="modal" @click="closeModal">
    <div class="modal-content" @click.stop>
      <iframe :src="youtubeEmbedUrl" width="560" height="315" frameborder="0" allowfullscreen></iframe>
      <button @click="closeModal">닫기</button>
    </div>
  </div>
</template>

<script>
const youtubeAPIKey = import.meta.env.VITE_YOUTUBE_API_KEY

export default {
  props: {
    movie: Object,
  },
  computed: {
    youtubeEmbedUrl() {
      // 유튜브 썸네일을 클릭했을 때 해당 영화의 유튜브 링크로 변경하세요.
      // 예를 들어, 'https://www.youtube.com/watch?v=' 뒤에 해당 영화의 유튜브 비디오 ID를 추가하세요.
      return `https://www.youtube.com/embed/${this.movie.youtube_video_id}`; // TMDB 에서 비디오
    },
  },
  methods: {
    closeModal() {
      this.$emit("close-modal");
    },
  },
};
</script>

<style scoped>
.modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.7);
  display: flex;
  justify-content: center;
  align-items: center;
}

.modal-content {
  background: #fff;
  padding: 20px;
  border-radius: 5px;
}

iframe {
  width: 100%;
  height: 100%;
}
</style>
