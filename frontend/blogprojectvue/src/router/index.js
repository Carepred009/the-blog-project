import { createRouter, createWebHistory } from 'vue-router'


//
import Postcreate from "../views/Post.vue"

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [

    {
    path:'/post-create/', //use this url path to display the tempalte
    name: 'post_create',
    component: Postcreate,
    props:true
    }

  ],
})

export default router
