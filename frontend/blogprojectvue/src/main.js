import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
    //importing Bootstrap CSS styles
import 'bootstrap/dist/css/bootstrap.min.css'
    // Importing Bootstrap JavaScript bundle (for features like dropdowns and modals)
import 'bootstrap/dist/js/bootstrap.bundle.min.js'

    //Importing the Vue component that displays the posts
//import  getContent from './components/post_content.vue'




    //Create the Vue application instance
const app = createApp(App)

    //Registering the component globally with the tag name 'post-content'
    //This allows <post-content></post-content> to be used anywhere in the app.
//app.component('post-content', getContent)
    // Integrates the Vue Router plugin into the application
app.use(router)
    // Mounts the entire application to the HTML element with the ID 'app'
app.mount('#app')
