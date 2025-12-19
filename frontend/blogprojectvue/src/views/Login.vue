<template>
  <div class="container mt-5">
    <div class="row justify-content-center">
      <div class="col-md-6 col-lg-4">
        <div class="card shadow-sm">
          <div class="card-body">
            <h1 class="card-title text-center mb-4">Log in</h1>

            <form @submit.prevent="loginUser">
              <div class="mb-3">
                <label for="usernameInput" class="form-label">Username</label>
                <input
                  type="text"
                  class="form-control"
                  id="usernameInput"
                  v-model="login.username"
                  required
                />
              </div>

              <div class="mb-4">
                <label for="passwordInput" class="form-label">Password</label>
                <input
                  type="password"
                  class="form-control"
                  id="passwordInput"
                  v-model="login.password"
                  required
                />
              </div>

              <div class="d-grid gap-2">
                <button type="submit" class="btn btn-primary">
                  Login
                </button>
              </div>
            </form>

            <p v-if="errorMessage" class="text-danger mt-3 mb-0 text-center">
              {{ errorMessage }}
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
    // Imports the configured axios instance (likely includes the base URL)
import api from "../axios.js";

export default {
        // Start of the Vue component definition
  data() {
            // Defines the reactive data properties for the component
    return {
            // Object to hold the form input values (username and password)
      login: {
        username: "",       // Initial state for the username input
        password: "",       // Initial state for the password input
      },
      errorMessage: "",     // Initial state for displaying login errors
    };
  },

  methods: {    // Defines methods (functions) available to the component

    async loginUser() {     // Async function to handle the form submission and API call

            // Start of the error-handling block for the API call
     try {
                // Makes a POST request to the /api/token/ endpoint with the login object (username/password)
                // Awaits the response, which should contain the JWT tokens
        const response = await api.post("/api/token/", this.login);

                     // clear form
        this.login.username = "";         // Clears the username input after a successful login
        this.login.password = "";       // Clears the password input after a successful login

        // save tokens
        localStorage.setItem("access", response.data.access);     // Saves the access token to the browser's local storage
        localStorage.setItem("refresh", response.data.refresh);    // Saves the refresh token to the browser's local storage

        console.log(response.data);     // Logs the API response data to the console (for debugging)

        this.$router.push("/");         // Uses Vue Router to navigate the user to the home page (/)

      } catch (error) {                 // Logs the detailed error object to the console
        console.error(error);           // Catches any error that occurred during the `try` block (e.g., bad network, 401 Unauthorized)

        this.errorMessage = "Invalid Username or Password!";  // Sets the user-friendly error message to be displayed in the template

      }
    },
  },

};
</script>
