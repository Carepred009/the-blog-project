<template>
  <div class="comments card my-4">
    <div class="card-header bg-primary text-white">
      <h3><i class="bi bi-chat-left-text-fill me-2"></i>Comments ({{ comments.length }})</h3>
    </div>

    <div class="card-body">
      <div
        v-for="comment in comments"
        :key="comment.comment_id"
        class="comment border-bottom py-2"
      >
        <p class="mb-1 text-muted small">Post ID: {{ comment.post }}</p>

        <strong class="text-dark">
          <i class="bi bi-person-circle me-1"></i>
          {{ comment.user }}
        </strong>

        <p class="mt-1 mb-1">{{ comment.comment }}</p>

        <small class="text-muted d-block text-end">
          <i class="bi bi-clock-fill me-1"></i>
          {{ comment.created_at }}
        </small>
      </div>

      <div v-if="!comments.length" class="alert alert-info mt-3" role="alert">
        No comments yet. Be the first to comment!
      </div>

      <hr class="my-4">

      <h5 class="mb-3">Add a Comment</h5>

      <div class="mb-3">
        <textarea
          v-model="newComment"
          class="form-control"
          rows="3"
          placeholder="Write your comment here..."
        ></textarea>
      </div>

      <button
        @click="postComments"
        class="btn btn-success w-100"
        :disabled="!newComment.trim()"
      >
        <i class="bi bi-send-fill me-2"></i> Post Comment
      </button>

    </div>
  </div>
</template>

<script>
import api from "../axios.js";

export default {

 props: {                 //   `props` are values passed from a parent component to this child component.
  postId: {                 // postId is the ID of the post this comment section belongs to
    type: Number,
    required: true
  }
},


  data() {
    return {
      comments: [],                 // Array to store comments that belong ONLY to this post
      newComment: "",               // Stores the text typed by the user in the textarea
    };
  },

  mounted() {
    this.getComments();             // Fetch comments as soon as the component loads
  },

  methods: {
    async getComments() {
      try {
        const response = await api.get("/api/comments/");               // Make GET request to fetch all comments

        // Filter comments so only comments belonging to this post appear
        // comment.post = post ID from backend
        // this.postId = post ID passed via props

        this.comments = response.data.filter(
          comment => comment.post === this.postId
        );
        console.log(this.comments);
      } catch (error) {
        console.error(error);
      }
    },

    async postComments(){
            try{                                                    // Send POST request to backend to create a new comment
                const response = await api.post(`/api/comments/`,{

                comment: this.newComment,            // Comment text typed by the user

                post: this.postId                    // Post ID this comment belongs to

                });

                this.newComment = "";               // Clear textarea after successful submission

                console.log(response.data)            // Log response for debugging

                this.getComments()               // Refresh comment list so the new comment appears immediately
            }catch(error){
                console.error(error)
            }
     },


  },
};
</script>
