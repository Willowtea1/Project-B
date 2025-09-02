import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue' // Home page with text analysis
import ChatView from '../views/ChatView.vue' // Chat interface
import TextAnalysisView from '../views/TextAnalysisView.vue' // Advanced text analysis view

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView, // Home page as default
  },
  {
    path: '/chat',
    name: 'chat',
    component: ChatView, // Chat interface
  },
  {
    path: '/analyze',
    name: 'analyze',
    component: TextAnalysisView, // Advanced text analysis view
  },
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
})

export default router
