<!-- frontend/src/App.vue -->

<template>
  <v-app>
    <v-app-bar color="primary" dark>
      <v-app-bar-title> 🍳 Smart Recipe Analyzer </v-app-bar-title>
      <v-spacer></v-spacer>
      <v-btn icon @click="toggleTheme">
        <v-icon>{{ themeIcon }}</v-icon>
      </v-btn>
    </v-app-bar>

    <v-main>
      <v-container fluid class="pa-6">
        <router-view />
      </v-container>
    </v-main>

    <v-footer app color="primary" dark class="text-center">
      <v-container>
        <span>&copy; 2024 Smart Recipe Analyzer. Powered by Google Gemini AI</span>
      </v-container>
    </v-footer>
  </v-app>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useTheme } from 'vuetify'

const theme = useTheme()
const isDark = ref(false)

const themeIcon = computed(() => (isDark.value ? 'mdi-weather-sunny' : 'mdi-weather-night'))

const toggleTheme = () => {
  isDark.value = !isDark.value
  theme.global.name.value = isDark.value ? 'dark' : 'light'
}
</script>

<style>
.v-application {
  font-family: 'Roboto', sans-serif;
}

.recipe-card {
  transition: transform 0.2s ease-in-out;
}

.recipe-card:hover {
  transform: translateY(-4px);
}

.nutrition-chip {
  margin: 2px;
}

.ingredient-tag {
  margin: 4px;
}

.instruction-step {
  margin-bottom: 8px;
  padding-left: 16px;
  border-left: 3px solid #1976d2;
}
</style>
