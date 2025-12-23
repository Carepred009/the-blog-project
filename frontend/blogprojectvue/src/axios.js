
/*
import axios from "axios";

const api = axios.create({
  baseURL: "http://localhost:8000",
});

export default api;

*/

// Import the Axios library so we can make HTTP requests to the backend
import axios from "axios"

const api = axios.create({
     // The base URL of your Django backend
  // All requests using this instance will start with this URL
  baseURL: "http://localhost:8000",
})
    // Add a request interceptor
    // This runs BEFORE every request is sent to the backend
api.interceptors.request.use(config => {
        // Get the JWT access token from localStorage
        // This token was saved after the user logged in
  const token = localStorage.getItem("access")
          // If an access token exists (user is logged in)
  if (token) {
            // Attach the token to the Authorization header
        // "Bearer" is required by JWTAuthentication in DRF
    config.headers.Authorization = `Bearer ${token}`;
  }
        // Return the modified request configuration
    // If we don't return this, the request will fail
  return config
})
    // Export the Axios instance
    // This allows us to import and use it in other Vue files
export default api


