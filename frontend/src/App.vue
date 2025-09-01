<!-- frontend/src/views/App.vue -->

<template>
  <v-app>
    <!-- App Bar / Header -->
    <v-app-bar app color="primary" dark>
      <v-toolbar-title>My App</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn text to="/home">Home</v-btn>
      <v-btn text to="/chat">Chat</v-btn>
    </v-app-bar>

    <!-- Main content area -->
    <v-main>
      <RouterView />
    </v-main>
  </v-app>
</template>

<script setup>
import { RouterView } from 'vue-router'
</script>
