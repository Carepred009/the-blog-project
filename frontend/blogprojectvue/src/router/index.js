import { createRouter, createWebHistory } from 'vue-router'


//
import Postcreate from "../views/Post.vue"

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [

    {
    path:'/post-create/',
    name: 'post_create',
    component: Postcreate,
    props:true

    }

  ],
})

export default router
