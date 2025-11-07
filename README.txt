🎶 AI Emotion Detection & Music Recommender System
👩‍💻 Project Overview

This project uses Artificial Intelligence (AI) to detect emotions from user text input and recommend mood-based YouTube songs.
It combines Machine Learning (ML) for emotion classification and YouTube API integration for real-time song recommendations.

🚀 Features

✅ Detects emotion from user text (like sadness, joy, anger, fear, love, surprise)
✅ Recommends 3 live YouTube songs matching the emotion
✅ Beautiful interactive UI built using Streamlit
✅ Secure API Key Handling using environment variables or Hugging Face Secrets
✅ Deployed on Hugging Face Spaces

🧠 Tech Stack
Component	Technology
Frontend	Streamlit
Backend	Python
Model	Scikit-learn (TF-IDF + Logistic Regression)
API	YouTube Data API v3
Deployment	Hugging Face Spaces
Dataset	Custom text–emotion dataset (train1.csv, test1.csv, val1.csv)
📁 Folder Structure
AI_Emotion_Music_Recommender/
│
├── app.py                  # Model training script
├── main.py                 # Streamlit web app
├── model.pkl               # Saved ML model
├── vectorizer.pkl          # Saved TF-IDF vectorizer
├── train1.csv              # Training dataset
├── test1.csv               # Test dataset
├── val1.csv                # Validation dataset
├── requirements.txt        # Project dependencies
└── README.md               # Project documentation

⚙️ Installation & Setup
🧩 Step 1: Clone this repository
git clone https://github.com/YOUR_USERNAME/AI_Emotion_Music_Recommender.git
cd AI_Emotion_Music_Recommender

🧩 Step 2: Create virtual environment
python -m venv venv
venv\Scripts\activate     # On Windows
# or
source venv/bin/activate  # On Mac/Linux

🧩 Step 3: Install dependencies
pip install -r requirements.txt

🧩 Step 4: Add your YouTube API Key

Create a .env file or use environment variables:

YOUTUBE_API_KEY=your_api_key_here


Or if deploying to Hugging Face,
go to Settings → Secrets → Add New Secret:

Name: YOUTUBE_API_KEY
Value: your_api_key_here

▶️ Run the Project Locally
streamlit run main.py


App will open at:
👉 http://localhost:8501

🌐 Deployment (Hugging Face Spaces)

Deployed live at:
👉 https://YOUR_USERNAME-AI_Emotion_Music_Recommender.hf.space

🧑‍🤝‍🧑 Project Members
Name	Role
Neil	Model Development & Testing
Gautam Vats	Streamlit Frontend
Rahul Reddy	API Integration
Mohith Venkatesh	Dataset & Model Training

📘 Developed as part of AI Mini Project – Emotion Detection & Music Recommender System

🧾 License

This project is released under the MIT License – feel free to modify and enhance it.

🌟 Show Some Love

If you like this project, consider giving it a ⭐ on GitHub and sharing it with your peers!
