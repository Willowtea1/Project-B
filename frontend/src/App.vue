<!-- frontend/src/App.vue -->

<template>
  <v-app>
    <v-container>
      <v-textarea
        label="Enter text to summarize and categorize"
        v-model="text"
        rows="6"
      ></v-textarea>
      <v-btn color="primary" @click="submitText">Analyze</v-btn>

      <div v-if="loading">Processing...</div>

      <v-card v-if="result">
        <v-card-title>Summary</v-card-title>
        <v-card-text>{{ result.summary }}</v-card-text>
        <v-card-title>Category</v-card-title>
        <v-card-text>{{ result.category }}</v-card-text>
      </v-card>
    </v-container>
  </v-app>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      text: '',
      result: null,
      loading: false,
    }
  },
  methods: {
    async submitText() {
      if (!this.text.trim()) return alert('Text cannot be empty')
      this.loading = true
      try {
        const res = await axios.post('http://127.0.0.1:8000/analyze', {
          text: this.text,
        })
        this.result = res.data
      } catch (err) {
        console.error(err)
        alert('Error processing text')
      } finally {
        this.loading = false
      }
    },
  },
}
</script>
