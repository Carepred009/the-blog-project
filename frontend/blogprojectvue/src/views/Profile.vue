<template>
  <div class="container py-4">
    <div class="row justify-content-center">
      <div class="col-lg-8 col-md-10">
        <h2 class="mb-4 text-center">{{profile?.user?.username}}</h2>

        <div class="text-center mb-4">
          <img
            v-if="profile.profile_picture"
            :src="profile.profile_picture"
            class="img-fluid rounded-circle border border-3 p-1"
            alt="Profile Picture"
            style="width: 120px; height: 120px; object-fit: cover;"
          />
          <div v-else class="placeholder-img bg-light text-secondary d-flex align-items-center justify-content-center rounded-circle mx-auto" style="width: 120px; height: 120px;">
            No Image
          </div>
        </div>

        <form @submit.prevent="updateProfile" class="p-4 border rounded shadow-sm">

          <div class="mb-3">

            <label for="profileBio" class="form-label">Bio</label>
            <hr>
              <div>
             <p>Username : {{profile?.user?.username}} </p>
          </div>
          <hr>
            <hr>
               <div>
             <p>First Name : {{profile?.user?.first_name}} </p>
          </div>
          <hr>
                 <div>
             <p>Last Name : {{profile?.user?.last_name}} </p>
          </div>
          <hr>

          <hr>
                 <div>
             <p>Email : {{profile?.user?.email}} </p>
          </div>
          <hr>

            <div>
                    <template v-if="!isEditing">
                      <p>{{ profile.bio }}</p>
                      <button @click="startEditing">Edit Bio</button>
                    </template>

                    <template v-else>
                      <textarea v-model="profile.bio" rows="4"></textarea>
                      <div>
                        <button @click="saveChanges">Save</button>
                        <button @click="cancelEditing">Cancel</button>
                      </div>
                    </template>
            </div>

            <p>{{profile.bio}} </p>
            <hr>

          </div>




          <div class="mb-4">
            <label for="profilePictureUpload" class="form-label">Update Profile Picture</label>
            <input
              type="file"
              @change="onFileChange"
              id="profilePictureUpload"
              class="form-control"
            />
          </div>

          <div class="d-grid">
            <button type="submit" class="btn btn-primary btn-lg">
              Update Profile
            </button>
          </div>
        </form>

      </div>
    </div>
  </div>
</template>


<script>
 // Import the pre-configured Axios instance for making API requests
import api from "../axios.js";

  // Export the default configuration object for the Vue component.
export default{
     /*
      The name of the Vue component.
      This is useful for debugging, Vue DevTools,
      and when referencing the component internally.
      It does NOT control routing — routing is handled in index.js.
    */
    name: "profile",

    data(){                            // The data function returns the initial reactive state of the component.
        return{

            isEditing: false,           // Controls which element is visible (p or textarea)

             originalBio: '',               // Temporarily stores the original bio in case the user cancels

            profile:{                        // Holds the user's profile data fetched from the API.
                bio:"",
                profile_picture:null,
            },
                                              // Stores the file object selected by the user, waiting for submission.
            avatarFile: null,

        };
    },

                                                    // Runs immediately after the component is mounted to fetch initial data.
    mounted(){
        this.getProfile();
    },

    methods:{

                                                    /**
                                                     * Switches to Edit Mode and saves the current bio in case of cancelation.
                                                     */
            startEditing() {
                                                    // Save the original value before editing starts
              this.originalBio = this.profile.bio;
              this.isEditing = true;
            },

                                                    /**
                                                     * Saves the changes and switches back to Display Mode.
                                                     * (In a real app, this is where you'd call an API to update the server)
                                                     */
            saveChanges() {
                                                        // The changes are already in this.profile.bio thanks to v-model.
              this.isEditing = false;
                                                            // You can add logic here to send the updated bio to a backend.
              console.log('Bio saved:', this.profile.bio);
            },

                                                        /**
                                                         * Discards the changes and switches back to Display Mode.
                                                         */
            cancelEditing() {
                                                           // Restore the bio to the value it had before editing started
              this.profile.bio = this.originalBio;
              this.isEditing = false;
            },


                                                /**
                                                 * Fetches the user's profile from the API and updates the component state.
                                                 * NOTE: Assumes the API endpoint returns a list with the profile as the first element.
                                                 */
        async getProfile(){
            try{
                                                              // Send a GET request to the profiles endpoint.
                const response = await api.get(`/api/profiles/`)
                this.profile = response.data[0];                // Stores the user's biography text.
                console.log(response.data[0])                    // Stores the URL of the current profile picture.
                                                                 // NOTE: 'profile_id' will be added here after the API call in getProfile.
            }catch(error){
                 console.error(error)
            }
        }, //end of function

                                                         // Stores the selected file object when the input changes.
        onFileChange(e){
        this.avatarFile = e.target.files[0]
        },

        async updateProfile(){
                                                      // NOTE: FormData is required for file uploads, even if only text fields are being sent.
            const formData = new FormData()
            formData.append("bio", this.profile.bio)

            if (this.avatarFile){
                formData.append("profile_picture", this.avatarFile)
            }

            await api.put(`/api/profiles/${this.profile.profile_id}/`, formData,{
                headers:{
                    "Content-Type": "multipart/form-data", // Required for file upload payloads.
                },
            })

            alert("Profile updated");
        },


    },// end of methodds

}; //end of export

</script>

<style scoped>
/* Optional: Basic styling to make it look decent */
        textarea {
          width: 100%;
          margin-bottom: 10px;
        }
        button {
          margin-right: 5px;
          padding: 5px 10px;
        }
</style>