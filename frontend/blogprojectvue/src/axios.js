
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

/* ---------------- RESPONSE INTERCEPTOR ---------------- */
/*
  This interceptor runs AFTER every API response.

  Its job:
  - Detect expired access tokens (401 errors)
  - Automatically refresh the token
  - Retry the original request
  - Log the user out ONLY if refresh fails
*/
api.interceptors.response.use(
  response => response,                 // If response is OK, do nothing
  async error => {
    const originalRequest = error.config

    if (error.response?.status !== 401 || originalRequest._retry) {
      return Promise.reject(error)
    }

      // Mark this request so we don't retry it again
      // (prevents infinite refresh loops)
    originalRequest._retry = true

     // Get the refresh token from localStorage
    const refresh = localStorage.getItem("refresh")

    // If there is no refresh token, the user is truly logged out
    if (!refresh) {
      logout()
      return Promise.reject(error)
    }

    try {
      const res = await axios.post(
        "http://127.0.0.1:8000/api/token/refresh/",
        { refresh }
      )


        // ✅ SAVE NEW ACCESS TOKEN
       // Save the new short-lived access token
      localStorage.setItem("access", res.data.access)


      // 🔥 THIS IS THE MISSING PART
         /*
        IMPORTANT:
        If refresh token rotation is enabled,
        the backend sends a NEW refresh token.
        We MUST save it or future refreshes will fail.
      */
      if (res.data.refresh) {
        localStorage.setItem("refresh", res.data.refresh)
      }

        // Attach the new access token to the original request
      originalRequest.headers.Authorization =
        `Bearer ${res.data.access}`

         // Retry the original request with the new token
      return api(originalRequest)

    } catch {
            /*
        If refreshing fails:
        - Refresh token expired
        - Refresh token blacklisted
        - Token was tampered with

        The only valid action is to log out.
      */
      logout()
      return Promise.reject(error)
    }
  }
)

/* ---------------- LOGOUT HELPER ---------------- */
/*
  Clears all authentication data
  and forces the user to log in again.
*/
function logout() {
  localStorage.clear()
  window.location.href = "/login"
}

    // Export the Axios instance
    // This allows us to import and use it in other Vue files
export default api


