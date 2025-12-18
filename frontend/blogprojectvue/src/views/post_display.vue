<script setup>
import PostContent from "../components/post_content.vue";
import CreatePost from "../views/Post.vue"
</script>

<template>
  <div>
    <h1> Create Post</h1>
    <CreatePost />

    <h1>Blog Post</h1>
    <PostContent />
  </div>
</template>
//If it’s a PAGE → View
//If it’s PART of a page → Component
//If two parts must appear together → Compose them