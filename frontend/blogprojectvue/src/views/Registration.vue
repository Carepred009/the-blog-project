<template>
             <!-- Main container with padding -->
  <div class="container py-4">
                    <!-- Center the form horizontally -->
    <div class="row justify-content-center">
                 <!-- Control form width on medium & large screens -->
      <div class="col-md-6 col-lg-5">
                    <!-- Page title -->
        <h1 class="text-center mb-4">User Registration</h1>

                   <!--
                      Registration form
                      - @submit.prevent stops page reload
                      - Calls userRegistration() method
                    -->
        <form @submit.prevent="userRegistration" class="card p-4 shadow">

                <!-- Username input field -->
          <div class="mb-3">
            <label for="username" class="form-label">Username</label>
            <input
              type="text"
              class="form-control"
              id="username"
              v-model="register.username"
              required
            />
                        <!-- browser-level validation -->
                        <!-- bind input to register.username -->
          </div>
                        <!-- Email input field -->
          <div class="mb-3">
            <label for="email" class="form-label">Email</label>
            <input
              type="email"
              class="form-control"
              id="email"
              v-model="register.email"
              required
            />    <!-- Main container with padding -->
          </div>
                        <!-- Password input field -->
          <div class="mb-3">
            <label for="password" class="form-label">Password</label>
            <input
              type="password"
              class="form-control"
              id="password"
              v-model="register.password1"
              required
            />               <!-- DRF expects password1 -->

          </div>
                        <!-- Confirm password input field -->
          <div class="mb-3">
            <label for="confirmPassword" class="form-label"
              >Confirm Password</label
            >
            <input
              type="password"
              class="form-control"
              id="confirmPassword"
              v-model="register.password2"
              required
            />          <!-- DRF expects password2 -->
          </div>
                 <!-- Submit button -->
          <button type="submit" class="btn btn-primary w-100 mt-3">
            Register
          </button>
        </form>
                       <!-- Success message (shown only if message is not empty) -->
        <p v-if="message" class="alert alert-success mt-3 text-center">
          {{ message }}
        </p>
                <!-- Error message (shown only if error is not empty) -->
        <p v-if="error" class="alert alert-danger mt-3 text-center">
          {{ error }}
        </p>
      </div>
    </div>
  </div>
</template>

<script>
            // Import axios instance configured with base URL & headers
import api from "../axios.js"; // axios instance

export default {
            // Reactive state for the component
  data() {
    return {
            //Object holding only form data(sent to backend)
      register: {
            username: "",       // bound to username input
            email: "",          // bound to email input
            password1: "",      // required by dj-rest-auth
            password2: "",      // required by dj-rest-auth
      },

                                                 //UI feedback message (Not sent to backend)
        message: "",        // success message
        error: "",           // error message
    };
  },

  methods: {

    async userRegistration() {                   // Called when the registration form is submitted
      try {

        const response = await api.post(            // Send POST request to backend registration endpoint
          `/api/auth/registration/`,
          this.register                             // send only form data
        );

                    // Clear input fields after successful registration
        this.register.username = "";
        this.register.email = "";
        this.register.password1 = "";
        this.register.password2 = "";


        this.message = "Registration successful!";       // Show success message to the user

        alert('Successfully registered!')                // Optional alert popup

        console.log(response.data)                        // Log backend response (useful for debugging)
      } catch (error) {

        console.error(error.response.data)              // Log backend validation error to browser console

        this.error = error.response.data;               // Display backend error message to user


        alert('Error')                           // Optional alert popup
      }
    },

  },
};
</script>
