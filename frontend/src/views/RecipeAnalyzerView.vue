<template>
  <div class="recipe-analyzer">
    <!-- Header Section -->
    <v-row class="mb-6">
      <v-col cols="12" class="text-center">
        <h1 class="text-h3 font-weight-bold mb-2">🍳 Smart Recipe Analyzer</h1>
        <p class="text-h6 text-medium-emphasis">
          Enter your available ingredients and get AI-powered recipe suggestions with nutritional
          analysis
        </p>
      </v-col>
    </v-row>

    <!-- Input Form Section -->
    <v-card class="mb-6" elevation="3">
      <v-card-title class="bg-primary text-white">
        <v-icon start>mdi-food-variant</v-icon>
        What ingredients do you have?
      </v-card-title>
      <v-card-text class="pt-6">
        <v-form @submit.prevent="analyzeRecipes" ref="form">
          <v-row>
            <v-col cols="12" md="8">
              <v-textarea
                v-model="ingredients"
                label="Enter your ingredients (comma-separated)"
                placeholder="e.g., chicken breast, rice, tomatoes, garlic, olive oil"
                rows="4"
                variant="outlined"
                :rules="[rules.required]"
                :disabled="loading"
                auto-grow
                clearable
              ></v-textarea>
            </v-col>
            <v-col cols="12" md="4">
              <v-btn
                type="submit"
                color="primary"
                size="large"
                block
                :loading="loading"
                :disabled="!ingredients.trim()"
                class="mt-4"
              >
                <v-icon start>mdi-magnify</v-icon>
                {{ loading ? 'Analyzing...' : 'Find Recipes' }}
              </v-btn>
            </v-col>
          </v-row>
        </v-form>
      </v-card-text>
    </v-card>

    <!-- Loading State -->
    <v-row v-if="loading" class="mb-6">
      <v-col cols="12" class="text-center">
        <v-progress-circular indeterminate color="primary" size="64"></v-progress-circular>
        <p class="text-h6 mt-4">AI is cooking up some delicious recipes for you...</p>
      </v-col>
    </v-row>

    <!-- Error State -->
    <v-alert
      v-if="error"
      type="error"
      variant="tonal"
      class="mb-6"
      closable
      @click:close="error = ''"
    >
      <strong>Oops!</strong> {{ error }}
    </v-alert>

    <!-- Results Section -->
    <div v-if="recipes.length > 0">
      <v-row class="mb-4">
        <v-col cols="12">
          <h2 class="text-h4 font-weight-bold">🎯 Recipe Suggestions ({{ recipes.length }})</h2>
        </v-col>
      </v-row>

      <v-row>
        <v-col v-for="(recipe, index) in recipes" :key="index" cols="12" md="6" lg="4">
          <v-card class="recipe-card h-100" elevation="4">
            <v-card-title class="bg-primary text-white title-wrap">
              <v-icon start>mdi-food</v-icon>
              {{ recipe.name }}
            </v-card-title>

            <v-card-text class="pt-4">
              <!-- Rating -->
              <div class="d-flex align-center mb-3">
                <v-rating
                  v-model="ratings[getRecipeKey(recipe)]"
                  color="amber"
                  size="24"
                  density="comfortable"
                  @update:model-value="onRate(recipe, ratings[getRecipeKey(recipe)])"
                ></v-rating>
                <span class="ms-2 text-medium-emphasis"
                  >{{ ratings[getRecipeKey(recipe)] || 0 }}/5</span
                >
              </div>

              <!-- Recipe Meta Info -->
              <v-row class="mb-4">
                <v-col cols="6">
                  <v-chip color="info" variant="tonal" size="small" class="w-100 justify-center">
                    <v-icon start>mdi-clock</v-icon>
                    {{ recipe.cooking_time }}
                  </v-chip>
                </v-col>
                <v-col cols="6">
                  <v-chip
                    :color="getDifficultyColor(recipe.difficulty)"
                    variant="tonal"
                    size="small"
                    class="w-100 justify-center"
                  >
                    <v-icon start>mdi-star</v-icon>
                    {{ recipe.difficulty }}
                  </v-chip>
                </v-col>
              </v-row>

              <!-- Ingredients -->
              <div class="mb-4">
                <h6 class="text-subtitle-2 font-weight-bold mb-2">
                  <v-icon start size="small">mdi-format-list-bulleted</v-icon>
                  Ingredients
                </h6>
                <div class="d-flex flex-wrap">
                  <v-chip
                    v-for="ingredient in recipe.ingredients"
                    :key="ingredient"
                    color="secondary"
                    variant="outlined"
                    size="small"
                    class="ingredient-tag"
                  >
                    {{ ingredient }}
                  </v-chip>
                </div>
              </div>

              <!-- Instructions -->
              <div class="mb-4">
                <h6 class="text-subtitle-2 font-weight-bold mb-2">
                  <v-icon start size="small">mdi-chef-hat</v-icon>
                  Instructions
                </h6>
                <div>
                  <div
                    v-for="(instruction, stepIndex) in recipe.instructions"
                    :key="stepIndex"
                    class="instruction-step"
                  >
                    <strong>{{ stepIndex + 1 }}.</strong> {{ instruction }}
                  </div>
                </div>
              </div>

              <!-- Nutrition Info -->
              <div>
                <h6 class="text-subtitle-2 font-weight-bold mb-2">
                  <v-icon start size="small">mdi-nutrition</v-icon>
                  Nutrition (per serving)
                </h6>
                <div class="d-flex flex-wrap">
                  <v-chip color="success" variant="tonal" size="small" class="nutrition-chip">
                    {{ recipe.nutrition.calories }} cal
                  </v-chip>
                  <v-chip color="warning" variant="tonal" size="small" class="nutrition-chip">
                    P: {{ recipe.nutrition.protein }}
                  </v-chip>
                  <v-chip color="info" variant="tonal" size="small" class="nutrition-chip">
                    C: {{ recipe.nutrition.carbs }}
                  </v-chip>
                  <v-chip color="error" variant="tonal" size="small" class="nutrition-chip">
                    F: {{ recipe.nutrition.fat }}
                  </v-chip>
                  <v-chip
                    v-if="recipe.nutrition.fiber"
                    color="success"
                    variant="tonal"
                    size="small"
                    class="nutrition-chip"
                  >
                    Fiber: {{ recipe.nutrition.fiber }}
                  </v-chip>
                </div>
              </div>
            </v-card-text>

            <v-card-actions class="pt-0">
              <v-spacer></v-spacer>
              <v-btn color="primary" variant="outlined" size="small" @click="copyRecipe(recipe)">
                <v-icon start>mdi-content-copy</v-icon>
                Copy Recipe
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-col>
      </v-row>

      <!-- Try Again Button -->
      <v-row class="mt-6">
        <v-col cols="12" class="text-center">
          <v-btn color="secondary" size="large" @click="resetForm" variant="outlined">
            <v-icon start>mdi-refresh</v-icon>
            Try Different Ingredients
          </v-btn>
        </v-col>
      </v-row>
    </div>

    <!-- Empty State -->
    <v-row v-else-if="!loading && !error">
      <v-col cols="12" class="text-center">
        <v-card class="pa-8" variant="outlined">
          <v-icon size="64" color="grey" class="mb-4">mdi-food-variant</v-icon>
          <h3 class="text-h5 mb-2">Ready to cook?</h3>
          <p class="text-body-1 text-medium-emphasis">
            Enter your available ingredients above to get started with AI-powered recipe
            suggestions!
          </p>
        </v-card>
      </v-col>
    </v-row>
  </div>
</template>

<script setup>
import { ref, reactive, onMounted } from 'vue'
import axios from 'axios'

// Reactive data
const ingredients = ref('')
const recipes = ref([])
const loading = ref(false)
const error = ref('')
const form = ref(null)

// Ratings state keyed by recipe identity
const ratings = ref({})

// Form validation rules
const rules = reactive({
  required: (v) => !!v || 'Ingredients are required',
})

// API configuration
const API_BASE_URL = 'http://localhost:8000'

// Persist/load ratings
const RATINGS_STORAGE_KEY = 'recipe_ratings_v1'

const loadRatings = () => {
  try {
    const raw = localStorage.getItem(RATINGS_STORAGE_KEY)
    ratings.value = raw ? JSON.parse(raw) : {}
  } catch {
    ratings.value = {}
  }
}

const saveRatings = () => {
  try {
    localStorage.setItem(RATINGS_STORAGE_KEY, JSON.stringify(ratings.value))
  } catch {
    // ignore storage errors
  }
}

const getRecipeKey = (recipe) => {
  // Build a stable key using name + first ingredients signature
  const ingSig = Array.isArray(recipe.ingredients)
    ? recipe.ingredients.slice(0, 5).join('|').toLowerCase()
    : ''
  return `${recipe.name}`.toLowerCase() + '::' + ingSig
}

const onRate = (recipe, value) => {
  const key = getRecipeKey(recipe)
  ratings.value = { ...ratings.value, [key]: value }
  saveRatings()
}

onMounted(loadRatings)

// Methods
const analyzeRecipes = async () => {
  if (!ingredients.value.trim()) {
    error.value = 'Please enter some ingredients'
    return
  }

  loading.value = true
  error.value = ''
  recipes.value = []

  try {
    const response = await axios.post(`${API_BASE_URL}/analyze-recipes`, {
      ingredients: ingredients.value.trim(),
    })

    recipes.value = response.data.recipes
    // Pre-hydrate ratings for newly shown recipes
    for (const r of recipes.value) {
      const k = getRecipeKey(r)
      if (!(k in ratings.value)) {
        ratings.value[k] = 0
      }
    }
    saveRatings()
  } catch (err) {
    console.error('Error analyzing recipes:', err)
    if (err.response?.data?.detail) {
      error.value = err.response.data.detail
    } else if (err.message) {
      error.value = err.message
    } else {
      error.value = 'Failed to analyze recipes. Please try again.'
    }
  } finally {
    loading.value = false
  }
}

const getDifficultyColor = (difficulty) => {
  switch (difficulty.toLowerCase()) {
    case 'easy':
      return 'success'
    case 'medium':
      return 'warning'
    case 'hard':
      return 'error'
    default:
      return 'primary'
  }
}

const copyRecipe = (recipe) => {
  const recipeText = `
${recipe.name}

Ingredients:
${recipe.ingredients.map((ing) => `- ${ing}`).join('\n')}

Instructions:
${recipe.instructions.map((inst, i) => `${i + 1}. ${inst}`).join('\n')}

Cooking Time: ${recipe.cooking_time}
Difficulty: ${recipe.difficulty}
Servings: ${recipe.servings}

Nutrition (per serving):
- Calories: ${recipe.nutrition.calories}
- Protein: ${recipe.nutrition.protein}
- Carbs: ${recipe.nutrition.carbs}
- Fat: ${recipe.nutrition.fat}
${recipe.nutrition.fiber ? `- Fiber: ${recipe.nutrition.fiber}` : ''}
  `.trim()

  navigator.clipboard.writeText(recipeText).then(() => {
    // You could add a toast notification here
    console.log('Recipe copied to clipboard!')
  })
}

const resetForm = () => {
  ingredients.value = ''
  recipes.value = []
  error.value = ''
  if (form.value) {
    form.value.reset()
  }
}
</script>

<style scoped>
.recipe-analyzer {
  max-width: 1200px;
  margin: 0 auto;
}

.h-100 {
  height: 100%;
}

.ingredient-tag {
  margin: 2px;
}

.instruction-step {
  margin-bottom: 8px;
  padding-left: 16px;
  border-left: 3px solid #1976d2;
}

.nutrition-chip {
  margin: 2px;
}

/* Allow long recipe titles to wrap instead of truncating */
.title-wrap {
  white-space: normal;
  overflow: visible;
  text-overflow: clip;
  word-break: break-word;
}
</style>
