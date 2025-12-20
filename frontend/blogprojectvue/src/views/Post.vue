<template>

    <div>
        <h1> We will put the logout in here for now! </h1>
        <button @click="logoutUser()"> LOG OUT FOR NOW </button>
    </div>
<div class="container mt-5">

    <form @submit.prevent="createPost">

    <div class="card-header bg-primary text-while text-center">
    <h1 class="h3 mb-0">Create a Post </h1>
    </div>
    <br>

    <label for="postTitle" class="form-label">Title</label><br>
    <input type="text"
    id="postTitle"
    class="form-control"
    v-model="post.title"
    required/>
<br>

    <label for="postContent" class="form-label">Content</label> <br>
    <textarea
        class="form-control"
        id="postContent"
        v-model="post.content"
        rows="4"
        required
    ></textarea>
    <br>
    <br>

    <button class="btn btn-success btn-lg" type="submit"> Submit </button>
    </form>


</div>
</template>



<script>

import api from "../axios.js";  // from axios.js file

export default{
   data(){
    return{

        //use this for less complex, this post is only for createPost()
        //make the input fields v-model use post.name like this
        post:{
            title:"",
            content:"",
        },
    };

   },

   methods:{
        async createPost(){
            try{
                const  response = await api.post(`/api/posts/`, this.post); // POST method
                this.post = {title: "", content:""}
                //this.post = response.data;
                console.log(response.data)
            }catch(error){
                console.error(error)
            }
        },  //end of function

        // This function logs out the currently authenticated user
        async logoutUser(){
                try{
                        // Send a POST request to the Django logout endpoint
                        // The Axios interceptor automatically adds the Authorization header (access token)
                    const response = await api.post(`/api/logout/`, {

                                // Send the refresh token in the request body
                                 // This allows the backend to blacklist (invalidate) the refresh token
                        refresh: localStorage.getItem("refresh"),
                    })
                                    // Remove the access token from localStorage
                                    // This immediately logs the user out on the frontend
                    localStorage.removeItem("access")

                     // Remove the refresh token from localStorage
                      // This prevents the user from getting new access tokens
                    localStorage.removeItem("refresh")

                    // Redirect the user to the login page after logout
                    this.$router.push("/login")


                    console.log(response.data)  // Log the response from the backend (for debugging)
                    alert("Successfully logout!")
                }catch(error){
                    console.error(error)    // Log any error that occurs during the logout process
                    alert("Error in log out!")
                }
        }, //end of function

   }, //end of method

};

</script>