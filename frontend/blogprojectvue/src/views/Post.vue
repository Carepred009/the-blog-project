<template>

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
        },
   },

};

</script>