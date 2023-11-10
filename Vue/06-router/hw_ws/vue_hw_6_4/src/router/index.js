import { createRouter, createWebHistory } from 'vue-router'
// import HomeView from '../views/HomeView.vue'  => 예시
import SomeView from '@/views/SomeView.vue'
import OtherView from '@/views/OtherView.vue'
import StudentView from '@/views/StudentView.vue'
import StudentDetailView from '@/views/StudentDetailView.vue'
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/SomeView',
      name: 'someview',
      component: SomeView
    },
    {
      path: '/OtherView',
      name: 'otherview',
      component: OtherView
    },
    {
      path: '/StudentView',
      name: 'studentview',
      component: StudentView
    },
    {
      path: '/students/:name',  // 이름을 받아올때
      name: 'StudentDetailView',
      component: StudentDetailView
    },
    
  ]
})

export default router
