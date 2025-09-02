// Global imports
import './assets/main.css'
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

// Vuetify setup
import 'vuetify/styles'
import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'

// Import Material Design Icons
import '@mdi/font/css/materialdesignicons.css'

// Create Vuetify instance with mdi icons enabled
const vuetify = createVuetify({
  components,
  directives,
  icons: {
    defaultSet: 'mdi', // 👈 enable mdi icons
  },
})

// Create and mount app
createApp(App).use(router).use(vuetify).mount('#app')
