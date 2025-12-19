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

//import the login.vue
//this component will be use for login
import login from "../views/login.vue"

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

    {           // use this url path to display login.vue
        path: "/login/",
        name: "login",     //Vue component that will render for this route
        component: login,     //  // Allow route params to be passed as props to the component
        props: true

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




// This function runs BEFORE every route change in the app
router.beforeEach((to, from, next) => {

  // Get the access token from browser storage
  // If user is logged in, this token exists
  const token = localStorage.getItem("access");

  // Check:
  // 1. User is NOT going to the login page
  // 2. User does NOT have an access token
  if (to.path !== "/login" && !token) {

    // If both conditions are true:
    // Force the user to go to the login page
    next("/login");

  } else {

    // Otherwise:
    // Allow navigation to continue normally
    next();
  }
});
                     // Export the router so it can be used in main.js
export default router