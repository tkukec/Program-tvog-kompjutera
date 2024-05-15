<template>
  <div>
    <h1>Dashboard</h1>
    <button @click="logout">Logout</button>
    <EventList @editStatus="handleEditStatus" />
    <EventForm
      v-if="isEditing"
      :event="currentEvent"
      :isEditing="isEditing"
      @formSubmitted="handleFormSubmitted"
    />
  </div>
</template>

<script>
import EventList from "../components/EventList.vue";
import EventForm from "../components/EventForm.vue";

export default {
  components: {
    EventList,
    EventForm,
  },
  data() {
    return {
      isEditing: false,
      currentEvent: null,
    };
  },
  methods: {
    handleEditStatus(editStatus) {
      this.isEditing = editStatus; // Update isEditing value received from EventList
    },
    handleFormSubmitted() {
      this.currentEvent = null;
      this.isEditing = false;
    },
    logout() {
      localStorage.removeItem("token");
      this.$router.push("/");
    },
  },
};
</script>
