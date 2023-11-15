# 09_pjt 
  - 주의 : 유튜브 API는 하루 요청 횟수가 제한적임
  - 부트스트랩 사용을 위해 index.html에 등록

1. 받아온 API를 env에 넣기
2. views폴더와 components 필요한 vue 파일들 생성
3. router관련 컴포넌트를 index.js에 등록 + import등록 잊지말기 @는 절대주소 src/부터
4. MovieList 뷰 파일 작성
  - 스크립트 부분 import, 변수들 작성(router, 데이터저장장소, 이미지주소 등), 영화 정보를 받아오는경우 docs에 있는 방법 활용
  - @click 이벤트를 활용하여 이동하는 함수 설정 
   @click="goDetail(데이터)
  const goDetail = (데이터) => {
  해당 페이지로 이동
  router.push(`/${movie.id}`)
}

5. 디테일 페이지 설정
  - 마찬가지로 import와 변수들을 설정해주는데, 이번 경우엔 받아 오는것이므로 router가 아닌 route 사용, ex)const movieId = route.params.movieId 파람스로 받아온것을 넣어줌
