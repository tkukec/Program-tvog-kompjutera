<template>
  <div>
    <h2>{{ isEditing ? "Edit Event" : "Add Event" }}</h2>
    <form @submit.prevent="submitForm">
      <div>
        <label>Name:</label>
        <input type="text" v-model="event.name" required />
      </div>
      <div>
        <label>Affected Brand:</label>
        <input type="text" v-model="event.affected_brand" required />
      </div>
      <div>
        <label>Description:</label>
        <textarea v-model="event.description" maxlength="1500"></textarea>
      </div>
      <div>
        <label>Malicious URL:</label>
        <input type="url" v-model="event.malicious_url" required />
      </div>
      <div>
        <label>Malicious Domain Registration Date:</label>
        <input
          type="date"
          v-model="event.malicious_domain_registration_date"
          required
        />
      </div>
      <div>
        <label>DNS Records:</label>
        <div v-for="(record, index) in event.dns_records" :key="index">
          <input
            type="text"
            v-model="record.type"
            placeholder="Type (A, NS, MX)"
            required
          />
          <input
            type="text"
            v-model="record.value"
            placeholder="Value"
            required
          />
        </div>
        <button @click="addDNSRecord">Add DNS Record</button>
      </div>
      <div>
        <label>Keywords:</label>
        <input
          type="text"
          v-model="event.keywords"
          placeholder="Comma separated keywords"
        />
      </div>
      <div>
        <label>Status:</label>
        <select v-model="event.status" required>
          <option value="todo">To Do</option>
          <option value="in progress">In Progress</option>
          <option value="done">Done</option>
        </select>
      </div>
      <button type="submit">
        {{ isEditing ? "Save Changes" : "Add Event" }}
      </button>
    </form>
  </div>
</template>

<script>
import axios from "axios";

export default {
  props: ["event", "isEditing"],
  data() {
    return {
      event: this.event || {
        name: "",
        affected_brand: "",
        description: "",
        malicious_url: "",
        malicious_domain_registration_date: "",
        dns_records: [{ type: "", value: "" }],
        keywords: "",
        status: "todo",
      },
    };
  },
  methods: {
    addDNSRecord() {
      this.event.dns_records.push({ type: "", value: "" });
    },
    async submitForm() {
      try {
        const token = localStorage.getItem("token");
        const config = { headers: { Authorization: `Bearer ${token}` } };

        if (this.isEditing) {
          await axios.put(
            `http://your-backend-api/events/${this.event.id}`,
            this.event,
            config
          );
        } else {
          await axios.post(
            "http://your-backend-api/events",
            this.event,
            config
          );
        }
        this.$emit("formSubmitted");
      } catch (error) {
        alert("Failed to submit form");
      }
    },
  },
};
</script>
