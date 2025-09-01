<!-- frontend/src/App.vue -->

<template>
  <v-container>
    <v-textarea v-model="inputText" label="Paste your text here" rows="10"></v-textarea>

    <v-btn color="primary" @click="submitText" :loading="loading"> Summarize </v-btn>

    <v-card v-if="summary" class="mt-4">
      <v-card-title>Summary</v-card-title>
      <v-card-text>
        <ul>
          <ul>
            <li v-for="(point, index) in summaryPoints" :key="index">{{ point }}</li>
          </ul>
        </ul>
      </v-card-text>
    </v-card>

    <v-alert v-if="error" type="error" class="mt-4">{{ error }}</v-alert>
  </v-container>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      inputText: '',
      summary: '',
      error: '',
      loading: false,
    }
  },
  methods: {
    async submitText() {
      this.loading = true
      this.error = ''
      this.summary = ''
      try {
        const res = await axios.post('http://localhost:8000/summarize', {
          text: this.inputText,
        })
        if (res.data.summary) this.summary = res.data.summary
        else this.error = res.data.error || 'Unknown error'
      } catch (err) {
        this.error = err.message
      } finally {
        this.loading = false
      }
    },
  },
  computed: {
    summaryPoints() {
      return this.summary
        ? this.summary
            .split('\n') // split by lines
            .map((line) => line.replace(/^\*\s*/, '').trim()) // remove leading "* "
            .filter((line) => line !== '') // remove empty lines
        : []
    },
  },
}
</script>
