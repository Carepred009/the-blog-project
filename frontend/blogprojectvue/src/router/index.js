// Import the function to create a router instance
// and the history mode that uses browser history (clean URLs)
import { createRouter, createWebHistory } from 'vue-router'


//
//import Postcreate from "../views/Post.vue"

// Import the Registration page component
// This component will be rendered when the /registration/ route is visited
import registration from "../views/Registration.vue"

// Import the Post Display page component
// This component will be used as the home page
import post_display from "../views/post_display.vue"

const router = createRouter({
          // Configure router to use HTML5 history mode
            // This removes the # from URLs
  history: createWebHistory(import.meta.env.BASE_URL),
                 // Define all application routes
  routes: [
    {       //this template will be our default  home page
        path: "/",
        name: 'home',                 // Unique name for this route
        component: post_display,        // Vue component that will render for this route
        props: true                       // Allow route params to be passed as props to the component
    },

    //{
   // path:'/post-create/', //use this url path to display the tempalte
    //name: 'post_create',
    //component: Postcreate,
    //props:true
    //},

    {                                     // URL path for the registration page
        path: '/registration/',         //use this url to display the registration template
        name: 'registration',           // Unique name for the registration route
        component: registration,            // Vue component that will render the registration form
        props : true                        // Allow route params to be passed as props
    },



  ],
})
               // Export the router so it can be used in main.js
export default router
