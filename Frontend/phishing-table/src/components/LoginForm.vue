<template>
  <div>
    <h2>Login</h2>
    <form @submit.prevent="login">
      <div>
        <label>Email:</label>
        <input type="email" v-model="email" required />
      </div>
      <div>
        <label>Password:</label>
        <input type="password" v-model="password" required />
      </div>
      <button type="submit">Login</button>
    </form>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      email: "",
      password: "",
    };
  },
  methods: {
    async login() {
      try {
        // const response = await axios.post("http://your-backend-api/login", {
        //   email: this.email,
        //   password: this.password,
        // });
        // localStorage.setItem("token", response.data.token);
        localStorage.setItem("token", "fake-jwt-token");
        this.$router.push("/dashboard");
      } catch (error) {
        alert("Login failed");
      }
    },
  },
};
</script>
