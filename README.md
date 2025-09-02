# AI Text Analysis Application

A comprehensive web application that provides advanced text analysis capabilities including sentiment analysis, tag extraction, summarization, and categorization using Google's Gemini AI.

## Features

### 🎯 Core Analysis Capabilities

- **Text Summarization**: Generate concise 2-3 sentence summaries
- **Content Categorization**: Classify text into 10 categories (Business, Technology, Health, Entertainment, Education, Politics, Sports, Science, Arts, Others)
- **Sentiment Analysis**: Determine text sentiment (Positive, Negative, Neutral) with confidence scores
- **Tag Extraction**: Extract 5-8 relevant keywords and topics from text

### 🎨 User Interface

- **Modern Web Interface**: Built with Vue.js 3 and Vuetify
- **Responsive Design**: Works seamlessly on desktop and mobile devices
- **Real-time Analysis**: Instant results with loading indicators
- **Visual Feedback**: Color-coded sentiment and category indicators
- **Navigation**: Easy switching between different analysis views

## Project Structure

```
Project-B/
├── backend/
│   ├── main.py              # FastAPI backend with analysis endpoints
│   └── requirements.txt     # Python dependencies
└── frontend/
    ├── src/
    │   ├── App.vue          # Main application with navigation
    │   ├── views/
    │   │   ├── HomeView.vue
    │   │   ├── ChatView.vue
    │   │   └── TextAnalysisView.vue  # Advanced analysis interface
    │   └── router/
    │       └── index.js     # Vue Router configuration
    └── package.json         # Node.js dependencies
```

## Setup Instructions

### Backend Setup

1. **Navigate to backend directory**:

   ```bash
   cd backend
   ```

2. **Create virtual environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   Create a `.env` file in the backend directory:

   ```
   GOOGLE_API_KEY=your_google_gemini_api_key_here
   ```

5. **Run the backend server**:
   ```bash
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```

### Frontend Setup

1. **Navigate to frontend directory**:

   ```bash
   cd frontend
   ```

2. **Install dependencies**:

   ```bash
   npm install
   ```

3. **Run the development server**:

   ```bash
   npm run dev
   ```

4. **Access the application**:
   Open your browser and go to `http://localhost:5173`

## API Endpoints

### POST /analyze

Analyzes text and returns comprehensive results.

**Request Body**:

```json
{
  "text": "Your text to analyze here"
}
```

**Response**:

```json
{
  "summary": "A concise summary of the text",
  "category": "Technology",
  "sentiment": "Positive",
  "sentiment_score": 0.8,
  "tags": [
    "artificial intelligence",
    "machine learning",
    "technology",
    "innovation",
    "future"
  ]
}
```

### GET /health

Health check endpoint to verify service status.

## Usage

### Basic Analysis (Home Page)

1. Navigate to the home page (`/`)
2. Enter your text in the textarea
3. Click "Analyze Text" to get summary and category

### Advanced Analysis (Text Analysis Tool)

1. Navigate to the Text Analysis page (`/analyze`)
2. Enter your text in the larger textarea
3. Click "Analyze Text" to get comprehensive results including:
   - Summary
   - Category with color coding
   - Sentiment analysis with progress bar
   - Extracted tags as chips

## Technologies Used

### Backend

- **FastAPI**: Modern Python web framework
- **Google Gemini AI**: Advanced language model for text analysis
- **Pydantic**: Data validation and serialization
- **Uvicorn**: ASGI server

### Frontend

- **Vue.js 3**: Progressive JavaScript framework
- **Vuetify**: Material Design component library
- **Vue Router**: Client-side routing
- **Axios**: HTTP client for API communication

## Features in Detail

### Sentiment Analysis

- **Three Categories**: Positive, Negative, Neutral
- **Confidence Scoring**: -1.0 to 1.0 scale
- **Visual Indicators**: Color-coded chips and progress bars

### Content Categorization

- **10 Categories**: Comprehensive classification system
- **Color Coding**: Each category has a distinct color
- **Smart Classification**: AI-powered category selection

### Tag Extraction

- **Keyword Identification**: Extracts 5-8 relevant tags
- **Topic Discovery**: Identifies main themes and subjects
- **Visual Display**: Tags displayed as interactive chips

### Text Summarization

- **Concise Output**: 2-3 sentence summaries
- **Key Point Extraction**: Captures main ideas
- **Clear Language**: Easy-to-understand summaries

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is licensed under the MIT License.

## Support

For support or questions, please open an issue in the repository.
