<template>
  <div>
    <h2>Phishing Events</h2>
    <input type="text" v-model="searchQuery" placeholder="Search..." />
    <button @click="searchEvents">Search</button>
    <table class="styled-table">
      <thead>
        <tr>
          <th v-for="attribute in eventAttributes" :key="attribute">
            {{ attribute }}
          </th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="event in events" :key="event.id">
          <td>{{ event.name }}</td>
          <td>{{ event.description }}</td>
          <button @click="editEvent(event)">Edit</button>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import axios from "axios";
import mockAxios from "../api/mockApi";
import EventForm from "./EventForm.vue";

export default {
  components: { EventForm },
  data() {
    return {
      events: [],
      searchQuery: "",
      currentEvent: null,
      isEditing: false,
      eventAttributes: [
        "timestamp",
        "name",
        "affected brand",
        "description",
        "malicious url",
        "malicious domain registration date",
        "dns records",
        "keywords",
        "status",
      ],
    };
  },
  // async created() {
  //   await this.fetchEvents();
  // },
  async created() {
    try {
      const response = await mockAxios.get("/api/events");
      this.events = response.data;
    } catch (error) {
      console.error("Error fetching events:", error);
    }
  },
  methods: {
    async fetchEvents() {
      const token = localStorage.getItem("token");
      const config = { headers: { Authorization: `Bearer ${token}` } };
      const response = await axios.get(
        "http://your-backend-api/events",
        config
      );
      this.events = response.data;
    },
    searchEvents() {
      this.fetchEvents(); // Implement a search function on the backend
    },
    editEvent(event) {
      console.log("editEvent running");
      this.currentEvent = event;
      this.isEditing = true;
      this.$emit("editStatus", this.isEditing);
    },
    async handleFormSubmitted() {
      await this.fetchEvents();
      this.currentEvent = null;
      this.isEditing = false;
    },
  },
};
</script>

<style>
.styled-table {
  width: 100%;
  border-collapse: collapse;
}

.styled-table th,
.styled-table td {
  padding: 12px;
  border: 1px solid #ddd;
  text-align: left;
}

.styled-table th {
  background-color: #f4f4f4;
}
</style>
