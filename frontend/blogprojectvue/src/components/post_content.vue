<template>
    <div class="container mt-4 bg-warning">
          <h1 class="text-center mb-4"> This is the Post Content </h1>
           <div v-for=" content in contents" :key="content.post_id" class="card-mb4 shadow-sm">

                <div class="card-header bg-primary text-white">
                  <h3 class="mb-0"> Title: {{content.title}} </h3>
                </div>
                <br>

                <div class="card-body">
                    <p class="card-text"> Content: {{content.post_id}}</p>
                 <p class="card-text"> Content: {{content.post}}</p>
                  <p class="card-text"> Date: {{content.created_at}}</p>
                  <p class="card-text"> User: {{content.author}}</p>

                     <!--
                        When the button is clicked, getPostId(content.post_id) is called.
                        This sends a GET request to the API endpoint with the post ID
                        and loads the response data into the modal.
                    -->
                 <button @click="getPostId(content.post_id)" type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#myModal">
                        Update Post
                  </button>
                </div>
                  <br>
           </div>
    </div>



                <!-- The Modal -->
                <div class="modal" id="myModal">
                  <div class="modal-dialog">
                    <div class="modal-content">

                      <!-- Modal Header -->
                      <div class="modal-header">
                        <h4 class="modal-title">Modal Heading</h4>
                        <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
                      </div>

                      <!-- Modal body -->
                      <div class="modal-body">
                            <!-- update the specific post
                            selectedPost data will be displayed here based on the selected ID
                             -->
                                        <!-- do not put parameters-->
                            <form @submit.prevent="postUpdate">
                                <h1>Update the Post </h1>
                                <label>Title </label>
                                        <!--Can update with or without this   -->
                                <p>ID : {{selectedPost.post_id}} </p>
                                <label>Title </label>

                                <input type="text" v-model="selectedPost.title">
                                <br>
                                <label>Post </label>
                                <input type="text" v-model="selectedPost.post">
                                 <br>
                                <button type="submit">Update the Post </button>
                            </form>
                      </div>

                      <!-- Modal footer
                      <div class="modal-footer">
                        <button type="button" class="btn btn-danger" data-bs-dismiss="modal">Close</button>
                      </div>
                      -->

                    </div>
                  </div>
                </div> //end of modal



</template>


<script>
import api from "../axios.js"

export default{
    data(){

        return{
                    // holds the list of posts fetched from the API
                    //list
            contents:[],

                   // single post used for updating
                   // bound to the modal inputs via v-model
            selectedPost: {
                post_id: "",
                title: "",
                post:"",
            }

        };
     },
                // The 'mounted' lifecycle hook runs after the component is added to the DOM
      mounted(){
        this.getContent();
    },

    methods:{
        async getContent(){
            try{
                  // calls API end point to fetch the list posts
                const response = await api.get(`/api/posts/`);
                    // The raw data returned by the API will display in the console for debugging
                console.log(response.data);
                    // Passes the fetched post data (the array of posts) to the 'contents' data property
                    //use this.contents = response.data.result; when using pagination
                this.contents = response.data;
            }catch(error){
                // Logs any errors encountered during the API call
                console.error(error) //will display error at console.log()
            } //end try/catch

        }, //end function


            //Start of update function
            //retrieve the data of the specific ID
         async getPostId(postId){
                try{
                            //Calls the API end point GET request with the ID
                    const response = await api.get(`/api/posts/${postId}`);
                    console.log(response.data);
                            //returns the data the selectedPost
                            //Passes the fetched post data with single object to  the 'selectedPost'
                    this.selectedPost = response.data;
                }catch(error){
                    console.error(error)
                }        //end of try/catch

         }, //End of update Function

         //Start function to update
        async postUpdate(postId){
                try{
                                //Calls the API end point with PUT request with  the ID
                    const response = await api.put(`/api/posts/${this.selectedPost.post_id}/`,this.selectedPost);
                            //Passes the updated post data with single object to  the 'selectedPost'
                    this.selectedPost = response.data;
                    console.log("Updated!", response.data)
                }catch(error){
                            //log the error
                    console.error(error)
                }//end of try/catch
            }
         //end of function

    },//end of methods


};//end for export


</script>