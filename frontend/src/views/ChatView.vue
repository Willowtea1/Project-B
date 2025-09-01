<!-- frontend/src/views/Chatview.vue -->

<template>
  <v-container fluid>
    <v-row align="center" justify="center" class="mb-4">
      <v-col cols="12">
        <v-text-field
          v-model="prompt"
          label="Ask something..."
          full-width
          @keyup.enter="sendPrompt"
        />
      </v-col>
    </v-row>

    <v-row align="center" justify="center" class="mb-4">
      <v-col cols="12">
        <v-btn color="primary" @click="sendPrompt" block>Send</v-btn>
      </v-col>
    </v-row>

    <v-row justify="center">
      <v-col cols="12">
        <v-card v-if="reply">
          <v-card-text>{{ reply }}</v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'

const prompt = ref('')
const reply = ref('')

// Gemini //
const sendPrompt = async () => {
  if (!prompt.value) return
  try {
    const res = await axios.post('http://127.0.0.1:8000/api/ask/gemini', { text: prompt.value })
    reply.value = res.data.reply
    prompt.value = '' // clear input after sending
  } catch (err) {
    reply.value = 'Error: ' + err.message
  }
}

/* 
//  OpenRouter //
const sendPrompt = async () => {
  if (!prompt.value) return
  try {
    const res = await axios.post('/api/ask/openrouter', { text: prompt.value })
    reply.value = res.data.reply
    prompt.value = ''
  } catch (err) {
    reply.value = 'Error: ' + err.message
  }
}
*/
</script>
