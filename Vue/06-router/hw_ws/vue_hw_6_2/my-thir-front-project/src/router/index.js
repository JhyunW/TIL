import { createRouter, createWebHistory } from 'vue-router'
// import HomeView from '../views/HomeView.vue'  => 예시
import SomeView from '@/views/SomeView.vue'
import OtherView from '@/views/OtherView.vue'

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
    
  ]
})

export default router
