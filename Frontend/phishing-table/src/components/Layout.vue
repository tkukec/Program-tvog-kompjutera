<!-- Layout.vue -->
<template>
    <div>
      <Header />
  
      <main>
        <router-view></router-view>
      </main>
  
    </div>
  </template>
  
  <script>
  import Header from './Header.vue'
  
  export default {
    name: 'Layout',
    components: {
      Header,
    }
  }
  </script>
  
  <!-- <style>
  /* Add global styling for layout elements */
  header {
    /* Header styles */
  }
  
  main {
    /* Main content styles */
  }
  
  footer {
    /* Footer styles */
  }
  </style>
   -->