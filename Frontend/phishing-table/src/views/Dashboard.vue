<template>
  <div>
    <h1>Dashboard</h1>
    <EventList />
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
    handleFormSubmitted() {
      this.currentEvent = null;
      this.isEditing = false;
    },
  },
};
</script>
