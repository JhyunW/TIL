import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useCounterStore = defineStore('counter', () => {
  const articles = ref([])
  const API_URL = 'http://127.0.0.1:8000'
  const token = ref(null)
  const isLogin = computed(() => {
    if (token.value === null) {
      return false
    } else {
      return true
    }
  })

  // DRF에 article 조회 요청을 보내는 action
  const getArticles = function () {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/articles/`,
      headers: {
        'Authorization': `Token ${token.value}`  // 전체 게시글을 보기위한 토큰
      }
    })
      .then((res) =>{
        // console.log(res)
        articles.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const signUp = function (payload) {
    const { username, password1, password2 } = payload

    axios({
      method: 'post',
      url: `${API_URL}/accounts/signup/`,
      data: {
        username, password1, password2
        // 줄여쓰기 전
        // username: username,
        // password1: password1,
        // password2: password2
      }
    })
    .then((res) => {
        console.log('회원가입완료')
      })
      .catch((err) => {
        console.log('실패')
      })
  }

  const logIn = function (payload) {
    const { username, password } = payload
    axios({
      method: 'post',
      url: `${API_URL}/accounts/login/`,
      data: {
        username, password
        // 줄여쓰기 전
        // username: username,
        // password1: password
      }
    })
    .then((res) => {
        console.log('로그인완료')
        // 키는 res.data에 존재
        token.value = res.data.key  // 로그인 후 토큰 저장
      })
      .catch((err) => {
        console.log('실패')
      })
  }
  return { articles, API_URL, getArticles, signUp, logIn, token, isLogin}
}, { persist: true })
