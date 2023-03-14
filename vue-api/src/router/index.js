import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    /*
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    */
    
    {
      path: '/',
      name: 'cats',
      component: () => import('../views/CatsGallery.vue'),
    },
    {
      path: '/cats/page2',
      name: 'cats2',
      component: () => import('../views/CatsGallery2.vue'),
    },
    {
      path: '/cats/page3',
      name: 'cats3',
      component: () => import('../views/CatsGallery3.vue'),
    },
    
  ],
  scrollBehavior(to, from, savedPosition) {
    return { top: 0 };
  },
})

export default router
