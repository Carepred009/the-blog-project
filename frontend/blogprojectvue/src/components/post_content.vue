<template>
    <div class="container mt-4 bg-warning">
          <h1 class="text-center mb-4"> This is the Post Content </h1>
           <div v-for=" content in contents" :key="content.post_id" claass="card-mb4 shadow-sm">

                <div class="car-header bg-primary text-white">
                  <h3 class="mb-0"> Title: {{content.title}} </h3>
                </div>
                <br>
                <div class="card-body">
                 <p class="card-text"> Content: {{content.post}}</p>
                </div>
                  <br>
           </div>

    </div>
</template>


<script>
import api from "../axios.js"

export default{
    data(){

        return{
                // holds the list of posts fetched from the API
            contents:[],
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

    },//end of methods

};//end for export


</script>