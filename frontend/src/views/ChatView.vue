<!-- frontend/src/views/Chatview.vue -->

<template>
  <v-container fluid>
    <v-row justify="center">
      <v-col cols="12" md="8">
        <v-card class="pa-6">
          <v-card-title class="text-h4 text-center mb-4"> AI Chat Interface </v-card-title>

          <v-card-text class="text-body-1 text-center mb-6">
            Chat with our AI assistant for text analysis and insights
          </v-card-text>

          <!-- Chat Messages -->
          <div class="chat-messages mb-4" ref="chatContainer">
            <div
              v-for="(message, index) in messages"
              :key="index"
              :class="['message', message.type]"
            >
              <v-card variant="outlined" class="pa-3 mb-2">
                <div class="d-flex align-center mb-2">
                  <v-icon :color="message.type === 'user' ? 'primary' : 'success'" class="mr-2">
                    {{ message.type === 'user' ? 'mdi-account' : 'mdi-robot' }}
                  </v-icon>
                  <span class="text-subtitle-2 font-weight-bold">
                    {{ message.type === 'user' ? 'You' : 'AI Assistant' }}
                  </span>
                </div>
                <div class="text-body-1">{{ message.text }}</div>
              </v-card>
            </div>
          </div>

          <!-- Input Section -->
          <v-text-field
            v-model="prompt"
            label="Ask something..."
            full-width
            variant="outlined"
            placeholder="Enter your question or text to analyze..."
            @keyup.enter="sendPrompt"
            :disabled="isLoading"
            :loading="isLoading"
          />

          <v-card-actions class="pa-0 mt-3">
            <v-btn
              color="primary"
              @click="sendPrompt"
              :disabled="!prompt.trim() || isLoading"
              block
              size="large"
            >
              <v-icon left>mdi-send</v-icon>
              Send Message
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
import { ref, nextTick } from 'vue'
import axios from 'axios'

const prompt = ref('')
const isLoading = ref(false)
const messages = ref([
  {
    type: 'assistant',
    text: "Hello! I'm your AI assistant. I can help you analyze text, answer questions, and provide insights. What would you like to know?",
  },
])

const chatContainer = ref(null)

const sendPrompt = async () => {
  if (!prompt.value.trim() || isLoading.value) return

  // Add user message
  messages.value.push({
    type: 'user',
    text: prompt.value,
  })

  const userMessage = prompt.value
  prompt.value = '' // clear input
  isLoading.value = true

  try {
    // Call Gemini backend endpoint
    const res = await axios.post('http://127.0.0.1:8000/chat', {
      text: userMessage,
    })

    const reply = res.data.reply || 'Sorry, I could not generate a response.'

    messages.value.push({
      type: 'assistant',
      text: reply,
    })
  } catch (err) {
    console.error('Chat error:', err)
    messages.value.push({
      type: 'assistant',
      text: '⚠️ Sorry, I encountered an error while processing your request.',
    })
  } finally {
    isLoading.value = false
    await nextTick()
    if (chatContainer.value) {
      chatContainer.value.scrollTop = chatContainer.value.scrollHeight
    }
  }
}
</script>

<style scoped>
.chat-messages {
  max-height: 400px;
  overflow-y: auto;
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  padding: 16px;
  background-color: #fafafa;
}

.message {
  margin-bottom: 8px;
}

.message.user {
  text-align: right;
}

.message.assistant {
  text-align: left;
}

.message.user .v-card {
  background-color: #e3f2fd;
}

.message.assistant .v-card {
  background-color: #f1f8e9;
}
</style>
