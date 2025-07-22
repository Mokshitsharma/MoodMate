# MoodMate 😄

**MoodMate** is an AI-based facial emotion detection app using webcam or image uploads. It uses OpenCV and CVlib for face detection and streams results via a clean Streamlit UI.

## Features

- 📷 Webcam and image upload
- 😀 Real-time emoji-based emotion recognition
- 📩 Collects name and email (for logs)
- 🎙️ Voice detection – Coming soon!
- 🌐 Deployable on platforms like Render or Replit

## Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Runtime

Uses Python 3.10.13 (set in `runtime.txt` for Render compatibility)
