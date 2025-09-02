<template>
  <div class="text-analysis-container">
    <v-container fluid>
      <!-- Header -->
      <v-row class="mb-6">
        <v-col cols="12">
          <h1 class="text-h3 text-center mb-4">Text Analysis Tool</h1>
          <p class="text-body-1 text-center text-medium-emphasis">
            Analyze text for sentiment, extract tags, generate summaries, and categorize content
          </p>
        </v-col>
      </v-row>

      <!-- Input Section -->
      <v-row class="mb-6">
        <v-col cols="12">
          <v-card class="pa-4">
            <v-card-title class="text-h5 mb-3">Enter Text to Analyze</v-card-title>
            <v-textarea
              v-model="inputText"
              label="Text to analyze..."
              rows="6"
              auto-grow
              variant="outlined"
              placeholder="Enter or paste your text here for comprehensive analysis..."
              :disabled="isLoading"
            />
            <v-card-actions class="pa-0 mt-3">
              <v-btn
                color="primary"
                size="large"
                @click="analyzeText"
                :loading="isLoading"
                :disabled="!inputText.trim()"
                block
              >
                <v-icon left>mdi-magnify</v-icon>
                Analyze Text
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-col>
      </v-row>

      <!-- Results Section -->
      <v-row v-if="analysisResult">
        <v-col cols="12">
          <v-card class="pa-4">
            <v-card-title class="text-h5 mb-4">
              <v-icon left color="primary">mdi-chart-line</v-icon>
              Analysis Results
            </v-card-title>

            <!-- Summary -->
            <v-row class="mb-4">
              <v-col cols="12">
                <v-card variant="outlined" class="pa-3">
                  <v-card-title class="text-h6 text-primary">
                    <v-icon left>mdi-text-box-outline</v-icon>
                    Summary
                  </v-card-title>
                  <v-card-text class="text-body-1">
                    {{ analysisResult.summary }}
                  </v-card-text>
                </v-card>
              </v-col>
            </v-row>

            <!-- Category and Sentiment -->
            <v-row class="mb-4">
              <v-col cols="12" md="6">
                <v-card variant="outlined" class="pa-3 h-100">
                  <v-card-title class="text-h6 text-primary">
                    <v-icon left>mdi-tag</v-icon>
                    Category
                  </v-card-title>
                  <v-card-text>
                    <v-chip
                      :color="getCategoryColor(analysisResult.category)"
                      size="large"
                      class="text-h6"
                    >
                      {{ analysisResult.category }}
                    </v-chip>
                  </v-card-text>
                </v-card>
              </v-col>
              <v-col cols="12" md="6">
                <v-card variant="outlined" class="pa-3 h-100">
                  <v-card-title class="text-h6 text-primary">
                    <v-icon left>mdi-emoticon</v-icon>
                    Sentiment
                  </v-card-title>
                  <v-card-text>
                    <div class="d-flex align-center">
                      <v-chip
                        :color="getSentimentColor(analysisResult.sentiment)"
                        size="large"
                        class="text-h6 mr-3"
                      >
                        {{ analysisResult.sentiment }}
                      </v-chip>
                      <v-progress-linear
                        :model-value="getSentimentProgress(analysisResult.sentiment_score)"
                        :color="getSentimentColor(analysisResult.sentiment)"
                        height="8"
                        rounded
                        class="flex-grow-1"
                      />
                    </div>
                    <div class="text-caption mt-2">
                      Score: {{ analysisResult.sentiment_score.toFixed(2) }}
                    </div>
                  </v-card-text>
                </v-card>
              </v-col>
            </v-row>

            <!-- Tags -->
            <v-row>
              <v-col cols="12">
                <v-card variant="outlined" class="pa-3">
                  <v-card-title class="text-h6 text-primary">
                    <v-icon left>mdi-tag-multiple</v-icon>
                    Key Tags & Topics
                  </v-card-title>
                  <v-card-text>
                    <div class="d-flex flex-wrap gap-2">
                      <v-chip
                        v-for="tag in analysisResult.tags"
                        :key="tag"
                        color="secondary"
                        variant="outlined"
                        size="large"
                        class="ma-1"
                      >
                        {{ tag }}
                      </v-chip>
                    </div>
                  </v-card-text>
                </v-card>
              </v-col>
            </v-row>
          </v-card>
        </v-col>
      </v-row>

      <!-- Error Message -->
      <v-row v-if="errorMessage">
        <v-col cols="12">
          <v-alert type="error" variant="tonal" closable @click:close="errorMessage = ''">
            {{ errorMessage }}
          </v-alert>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'

const inputText = ref('')
const analysisResult = ref(null)
const isLoading = ref(false)
const errorMessage = ref('')

const analyzeText = async () => {
  if (!inputText.value.trim()) return

  isLoading.value = true
  errorMessage.value = ''

  try {
    const response = await axios.post('http://127.0.0.1:8000/analyze', {
      text: inputText.value,
    })
    analysisResult.value = response.data
  } catch (error) {
    console.error('Analysis error:', error)
    errorMessage.value = error.response?.data?.detail || 'Failed to analyze text. Please try again.'
  } finally {
    isLoading.value = false
  }
}

const getCategoryColor = (category) => {
  const colors = {
    Business: 'blue',
    Technology: 'purple',
    Health: 'green',
    Entertainment: 'orange',
    Education: 'indigo',
    Politics: 'red',
    Sports: 'teal',
    Science: 'cyan',
    Arts: 'pink',
    Others: 'grey',
  }
  return colors[category] || 'grey'
}

const getSentimentColor = (sentiment) => {
  const colors = {
    Positive: 'success',
    Negative: 'error',
    Neutral: 'info',
  }
  return colors[sentiment] || 'grey'
}

const getSentimentProgress = (score) => {
  // Convert -1 to 1 scale to 0 to 100 scale
  return ((score + 1) / 2) * 100
}
</script>

<style scoped>
.text-analysis-container {
  min-height: 100vh;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  padding: 20px 0;
}

.h-100 {
  height: 100%;
}

.gap-2 {
  gap: 8px;
}
</style>
