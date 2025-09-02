<script setup></script>

<template>
  <div class="home-view">
    <!-- Hero Section -->
    <v-row class="mb-8">
      <v-col cols="12" class="text-center">
        <v-icon size="120" color="primary" class="mb-4">🍳</v-icon>
        <h1 class="text-h2 font-weight-bold mb-4">Welcome to Smart Recipe Analyzer</h1>
        <p class="text-h5 text-medium-emphasis mb-6">
          Transform your available ingredients into delicious, AI-powered recipe suggestions
        </p>
        <v-btn to="/recipes" color="primary" size="x-large" class="px-8">
          <v-icon start>mdi-food-variant</v-icon>
          Start Cooking
        </v-btn>
      </v-col>
    </v-row>

    <!-- Features Section -->
    <v-row class="mb-8">
      <v-col cols="12">
        <h2 class="text-h4 font-weight-bold text-center mb-6">What You Can Do</h2>
      </v-col>

      <v-col cols="12" md="4">
        <v-card class="h-100 text-center" elevation="3">
          <v-card-text class="pa-6">
            <v-icon size="64" color="primary" class="mb-4">mdi-magnify</v-icon>
            <h3 class="text-h5 font-weight-bold mb-3">Smart Ingredient Analysis</h3>
            <p class="text-body-1">
              Simply list your available ingredients and let our AI analyze what delicious meals you
              can create.
            </p>
          </v-card-text>
        </v-card>
      </v-col>

      <v-col cols="12" md="4">
        <v-card class="h-100 text-center" elevation="3">
          <v-card-text class="pa-6">
            <v-icon size="64" color="success" class="mb-4">mdi-food</v-icon>
            <h3 class="text-h5 font-weight-bold mb-3">AI Recipe Generation</h3>
            <p class="text-body-1">
              Get multiple recipe suggestions with step-by-step instructions, cooking times, and
              difficulty levels.
            </p>
          </v-card-text>
        </v-card>
      </v-col>

      <v-col cols="12" md="4">
        <v-card class="h-100 text-center" elevation="3">
          <v-card-text class="pa-6">
            <v-icon size="64" color="info" class="mb-4">mdi-nutrition</v-icon>
            <h3 class="text-h5 font-weight-bold mb-3">Nutritional Insights</h3>
            <p class="text-body-1">
              Understand the nutritional value of each recipe with detailed breakdowns of calories,
              protein, carbs, and more.
            </p>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>

    <!-- How It Works Section -->
    <v-row class="mb-8">
      <v-col cols="12">
        <h2 class="text-h4 font-weight-bold text-center mb-6">How It Works</h2>
      </v-col>

      <v-col cols="12" md="3" class="text-center">
        <div class="step-circle mb-3">
          <span class="step-number">1</span>
        </div>
        <h4 class="text-h6 font-weight-bold mb-2">List Ingredients</h4>
        <p class="text-body-2">Enter what you have in your kitchen</p>
      </v-col>

      <v-col cols="12" md="3" class="text-center">
        <div class="step-circle mb-3">
          <span class="step-number">2</span>
        </div>
        <h4 class="text-h6 font-weight-bold mb-2">AI Analysis</h4>
        <p class="text-body-2">Our AI processes your ingredients</p>
      </v-col>

      <v-col cols="12" md="3" class="text-center">
        <div class="step-circle mb-3">
          <span class="step-number">3</span>
        </div>
        <h4 class="text-h6 font-weight-bold mb-2">Get Recipes</h4>
        <p class="text-body-2">Receive personalized suggestions</p>
      </v-col>

      <v-col cols="12" md="3" class="text-center">
        <div class="step-circle mb-3">
          <span class="step-number">4</span>
        </div>
        <h4 class="text-h6 font-weight-bold mb-2">Start Cooking</h4>
        <p class="text-body-2">Follow instructions and enjoy!</p>
      </v-col>
    </v-row>

    <!-- CTA Section -->
    <v-row>
      <v-col cols="12" class="text-center">
        <v-card class="pa-8" color="primary" dark>
          <h3 class="text-h4 font-weight-bold mb-4">Ready to transform your cooking experience?</h3>
          <p class="text-h6 mb-6">
            Join thousands of home chefs who are discovering new recipes every day!
          </p>
          <v-btn to="/recipes" color="white" size="large" variant="outlined" class="px-8">
            <v-icon start>mdi-chef-hat</v-icon>
            Get Started Now
          </v-btn>
        </v-card>
      </v-col>
    </v-row>
  </div>
</template>

<script setup>
// No additional logic needed for this view
</script>

<style scoped>
.home-view {
  max-width: 1200px;
  margin: 0 auto;
}

.step-circle {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  background: linear-gradient(135deg, #1976d2, #42a5f5);
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0 auto;
}

.step-number {
  color: white;
  font-size: 2rem;
  font-weight: bold;
}

.h-100 {
  height: 100%;
}
</style>
