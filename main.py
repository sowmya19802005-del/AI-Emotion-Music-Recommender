import streamlit as st
import pickle
import os
from googleapiclient.discovery import build

# -------------------------------
# 🎯 Load Model and Vectorizer
# -------------------------------
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# -------------------------------
# 🔐 Load YouTube API Key Securely
# -------------------------------
if "youtube" in st.secrets:
    API_KEY = st.secrets["youtube"]["api_key"]
else:
    # fallback for local testing
    API_KEY = os.getenv("YOUTUBE_API_KEY", "YOUR_API_KEY_HERE")

YOUTUBE = build("youtube", "v3", developerKey=API_KEY)


def get_youtube_songs(emotion, max_results=3):
    """Search for emotion-based songs on YouTube dynamically."""
    query = f"{emotion} mood songs"
    request = YOUTUBE.search().list(
        part="snippet",
        q=query,
        type="video",
        maxResults=max_results
    )
    response = request.execute()

    songs = []
    for item in response.get("items", []):
        video_title = item["snippet"]["title"]
        video_url = f"https://www.youtube.com/watch?v={item['id']['videoId']}"
        songs.append((video_title, video_url))
    return songs


# -------------------------------
# 🌈 Streamlit Page Configuration
# -------------------------------
st.set_page_config(page_title="AI Emotion Music Recommender", page_icon="🎵", layout="centered")

# Custom styling
st.markdown("""
    <style>
        body {
            background: linear-gradient(135deg, #f3ec78, #af4261);
            color: #222;
        }
        .stButton>button {
            background-color: #ff4b4b;
            color: white;
            border-radius: 10px;
            height: 3em;
            width: 100%;
            font-size: 18px;
            font-weight: bold;
        }
        .stTextArea textarea {
            border-radius: 10px;
            font-size: 16px;
        }
    </style>
""", unsafe_allow_html=True)

# -------------------------------
# 🎧 App UI
# -------------------------------
st.title("🎶 AI Emotion Detection + Live YouTube Song Recommender")
st.markdown("**Describe your feelings** and let the AI find songs that match your mood 💫")

user_input = st.text_area("💬 How are you feeling today?", placeholder="e.g. I'm feeling stressed about exams...")

if st.button("🎵 Get My Songs"):
    if user_input.strip() != "":
        # Predict emotion
        input_vec = vectorizer.transform([user_input])
        emotion = model.predict(input_vec)[0].lower()

        # Display detected emotion
        st.success(f"**Detected Emotion:** {emotion.capitalize()} 🧠")

        # 🎨 Visual effects based on emotion
        if "happy" in emotion or "joy" in emotion or "excited" in emotion:
            st.balloons()
        elif "sad" in emotion:
            st.snow()
        elif "anger" in emotion or "angry" in emotion:
            st.warning("😡 Take a deep breath — here are some songs to cool off!")
        elif "love" in emotion:
            st.info("💖 Love is in the air — enjoy your songs!")
        else:
            st.write("🎧 Here's some music to match your vibe!")

        # Fetch dynamic YouTube recommendations
        st.subheader("🎧 Recommended Songs Just for You:")
        songs = get_youtube_songs(emotion)

        if songs:
            for title, url in songs:
                st.markdown(f"- 🎵 [{title}]({url})")
        else:
            st.warning("⚠️ No songs found — try again with a different mood!")
    else:
        st.error("Please enter some text first 💬")

# -------------------------------
# 👩‍💻 Project Credits
# -------------------------------
st.markdown(
    """
    <hr style='border: 1px solid #444; margin-top: 50px;'>
    <div style='text-align: center; color: #E0E0E0; font-family: "Segoe UI", sans-serif;'>
        <h3 style='color: #7FFFD4;'>👩‍💻 Project Members</h3>
        <p><b>Neil</b> • <b>Gautam Vats</b> • <b>Rahul Reddy</b> • <b>Mohith Venkatesh</b></p>
        <p style='font-size: 15px; color: #aaa;'>
            📘 Developed as part of <i>AI Mini Project – Emotion Detection & Music Recommender System</i>
        </p>
    </div>
    """,
    unsafe_allow_html=True
)
