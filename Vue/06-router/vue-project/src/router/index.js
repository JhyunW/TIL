import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import UserView from '@/views/UserView.vue'
import LoginView from '@/views/LoginView.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue')
    },
    {
      path: '/user/:id',
      name: 'user',
      component: UserView,
      // 해당 경로로 이동할때만 실행
      beforeEnter: (to, from) => {
        console.log(to)
        console.log(from)
      }
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView,
      // 로그인이 되어 있을때 돌아오는 함수
      beforeEnter: (to, from) => {
        const isAuthenticated = true
        if (isAuthenticated === true) {
          console.log('로그인 되어있습니다.')
          return {name: 'home'}
        }
      }
    }
  ]
})

// router.beforeEach((to, from) => {
//   console.log(to)
//   console.log(from)
// })


// router.beforeEach((to, from) => {
//     const isAuthenticated = false  // 비로그인자로 가정
//     // ! 를 붙여서 비로그인자라면! 이라고 가정
//     if (!isAuthenticated && to.name !== 'login') {
//       console.log('로그인이 필요합니다')
//       return { name: 'login'}
//     }
//   })
export default router

