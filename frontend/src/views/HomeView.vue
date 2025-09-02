<script setup></script>

<template>
  <v-container>
    <v-row justify="center">
      <v-col cols="12" md="8">
        <v-card class="pa-6">
          <v-card-title class="text-h4 text-center mb-4">
            Welcome to AI Text Analysis
          </v-card-title>

          <v-card-text class="text-body-1 text-center mb-6">
            Enter text below to get a summary and categorization, or visit our advanced
            <router-link to="/analyze" class="text-primary">Text Analysis Tool</router-link>
            for comprehensive sentiment analysis and tag extraction.
          </v-card-text>

          <v-textarea
            label="Enter text to summarize and categorize"
            v-model="text"
            rows="6"
            variant="outlined"
            placeholder="Enter your text here..."
            :disabled="loading"
          ></v-textarea>

          <v-card-actions class="pa-0 mt-4">
            <v-btn
              color="primary"
              size="large"
              @click="submitText"
              :loading="loading"
              :disabled="!text.trim()"
              block
            >
              <v-icon left>mdi-magnify</v-icon>
              Analyze Text
            </v-btn>
          </v-card-actions>
        </v-card>

        <!-- Results -->
        <v-card v-if="result" class="mt-6 pa-4">
          <v-card-title class="text-h5 mb-3">
            <v-icon left color="primary">mdi-chart-line</v-icon>
            Analysis Results
          </v-card-title>

          <v-row>
            <v-col cols="12" md="6">
              <v-card variant="outlined" class="pa-3">
                <v-card-title class="text-h6 text-primary">Summary</v-card-title>
                <v-card-text>{{ result.summary }}</v-card-text>
              </v-card>
            </v-col>
            <v-col cols="12" md="6">
              <v-card variant="outlined" class="pa-3">
                <v-card-title class="text-h6 text-primary">Category</v-card-title>
                <v-card-text>
                  <v-chip color="primary" size="large">{{ result.category }}</v-chip>
                </v-card-text>
              </v-card>
            </v-col>
          </v-row>

          <!-- Show additional results if available -->
          <v-row v-if="result.sentiment || result.tags" class="mt-4">
            <v-col cols="12" md="6" v-if="result.sentiment">
              <v-card variant="outlined" class="pa-3">
                <v-card-title class="text-h6 text-primary">Sentiment</v-card-title>
                <v-card-text>
                  <v-chip :color="getSentimentColor(result.sentiment)" size="large">
                    {{ result.sentiment }}
                  </v-chip>
                  <div v-if="result.sentiment_score" class="mt-2">
                    Score: {{ result.sentiment_score.toFixed(2) }}
                  </div>
                </v-card-text>
              </v-card>
            </v-col>
            <v-col cols="12" md="6" v-if="result.tags">
              <v-card variant="outlined" class="pa-3">
                <v-card-title class="text-h6 text-primary">Tags</v-card-title>
                <v-card-text>
                  <v-chip
                    v-for="tag in result.tags"
                    :key="tag"
                    color="secondary"
                    variant="outlined"
                    class="ma-1"
                  >
                    {{ tag }}
                  </v-chip>
                </v-card-text>
              </v-card>
            </v-col>
          </v-row>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import axios from 'axios'

export default {
  name: 'HomeView',
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
    getSentimentColor(sentiment) {
      const colors = {
        Positive: 'success',
        Negative: 'error',
        Neutral: 'info',
      }
      return colors[sentiment] || 'grey'
    },
  },
}
</script>
