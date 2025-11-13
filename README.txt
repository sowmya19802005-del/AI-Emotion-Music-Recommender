AI Emotion Detection and Music Recommendation System
Project Overview

This project develops an AI system that identifies emotions from user text and provides suitable music recommendations from YouTube. It uses machine learning techniques for emotion classification and integrates the YouTube Data API for real-time song suggestions.

Features

Detects emotions such as joy, sadness, anger, fear, love, and surprise

Recommends three YouTube videos based on the detected emotion

Interactive interface created with Streamlit

Secure API key handling through environment variables or Hugging Face Secrets

Deployable on Hugging Face Spaces

Technology Stack
Component	Technology
Frontend	Streamlit
Backend	Python
Model	Scikit-learn (TF-IDF and Logistic Regression)
API	YouTube Data API v3
Deployment	Hugging Face Spaces
Dataset	Custom text–emotion dataset (train1.csv, test1.csv, val1.csv)
Folder Structure
AI_Emotion_Music_Recommender/
│
├── app.py               # Model training script
├── main.py              # Streamlit application
├── model.pkl            # Trained ML model
├── vectorizer.pkl       # TF-IDF vectorizer
├── train1.csv           # Training dataset
├── test1.csv            # Test dataset
├── val1.csv             # Validation dataset
├── requirements.txt     # Dependencies
└── README.md            # Documentation

Installation and Setup
Step 1: Clone the repository
git clone 
cd AI_Emotion_Music_Recommender

Step 2: Create a virtual environment
python -m venv venv
venv\Scripts\activate       # Windows
source venv/bin/activate    # Mac/Linux

Step 3: Install dependencies
pip install -r requirements.txt

Step 4: Add your YouTube API key

Create a .env file or set an environment variable:

YOUTUBE_API_KEY=your_api_key_here


For Hugging Face deployment, add the key under
Settings → Secrets → New Secret.

Running the Application
streamlit run main.py


The application will run at:
http://localhost:8501

Deployment

The project can be deployed on Hugging Face Spaces.

Project Contributors
Name	Role
Neil	Model development and testing
Gautam Vats	Streamlit interface
Rahul Reddy	API integration
Mohith Venkatesh	Dataset preparation and training

