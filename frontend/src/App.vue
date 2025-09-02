<!-- frontend/src/App.vue -->

<template>
  <v-app>
    <!-- Navigation -->
    <v-app-bar app color="primary" dark>
      <v-app-bar-title>AI Text Analysis</v-app-bar-title>
      <v-spacer></v-spacer>
      <v-btn to="/" text>Home</v-btn>
      <v-btn to="/analyze" text>Text Analysis</v-btn>
      <v-btn to="/chat" text>Chat</v-btn>
    </v-app-bar>

    <!-- Main Content with Router View -->
    <v-main>
      <router-view />
    </v-main>
  </v-app>
</template>

<script>
export default {
  name: 'App',
}
</script>

<style>
.v-main {
  background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
  min-height: 100vh;
}
</style>
