<template>
  <div>
    <h2>Phishing Events</h2>
    <input type="text" v-model="searchQuery" placeholder="Search..." />
    <button @click="searchEvents">Search</button>
    <ul>
      <li v-for="event in events" :key="event.id">
        <h3>{{ event.name }}</h3>
        <p>{{ event.description }}</p>
        <button @click="editEvent(event)">Edit</button>
      </li>
    </ul>
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
    };
  },
  // async created() {
  //   await this.fetchEvents();
  // },
  async created() {
    try {
      const response = await mockAxios.get('/api/events');
      this.events = response.data;
    } catch (error) {
      console.error('Error fetching events:', error);
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
      this.currentEvent = event;
      this.isEditing = true;
    },
    async handleFormSubmitted() {
      await this.fetchEvents();
      this.currentEvent = null;
      this.isEditing = false;
    },
  },
};
</script>
