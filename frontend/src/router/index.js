import { createRouter, createWebHistory } from 'vue-router'
import AppView from '../App.vue' // your current summary page
import HomeView from '../views/HomeView.vue' // placeholder
import ChatView from '../views/ChatView.vue' // placeholder

const routes = [
  {
    path: '/',
    name: 'summary',
    component: AppView, // App.vue stays here
  },
  {
    path: '/home',
    name: 'home',
    component: HomeView, // ready for future
  },
  {
    path: '/chat',
    name: 'chat',
    component: ChatView, // ready for future
  },
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
})

export default router
