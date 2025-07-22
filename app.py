import streamlit as st
import cv2
import numpy as np
from utils.detect_emotion import detect_emotion_from_image
from PIL import Image
import tempfile
import time

st.set_page_config(page_title="MoodMate", page_icon="😊", layout="centered")

# Animated emoji loader
def animated_loader():
    emojis = ["😊", "😢", "😠", "😮", "😍", "😐"]
    for _ in range(3):
        for emoji in emojis:
            st.markdown(f"<h2 style='text-align: center;'>{emoji}</h2>", unsafe_allow_html=True)
            time.sleep(0.15)

# App title
st.markdown("<h1 style='text-align: center;'>🎭 MoodMate</h1>", unsafe_allow_html=True)
st.markdown("## Upload an image or use webcam to detect emotion")

# Sidebar for user input
st.sidebar.markdown("### 📩 Enter Your Info")
name = st.sidebar.text_input("Name")
email = st.sidebar.text_input("Email")

# Choose input method
option = st.radio("Select input type:", ("📷 Use Webcam", "🖼️ Upload Image"))

# Webcam input
if option == "📷 Use Webcam":
    st.markdown("### Capture from Webcam")
    cap = cv2.VideoCapture(0)
    result_image = None

    if cap.isOpened():
        ret, frame = cap.read()
        if ret:
            st.image(frame, channels="BGR", caption="Captured Frame", use_column_width=True)
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            result_image, emotion = detect_emotion_from_image(frame_rgb)

            if result_image is not None:
                st.image(result_image, caption=f"Detected Emotion: {emotion}", use_column_width=True)
                st.success(f"{name}, you're feeling {emotion}!")
        else:
            st.warning("Unable to capture image from webcam.")
        cap.release()
    else:
        st.warning("Webcam not detected.")

# Image upload input
elif option == "🖼️ Upload Image":
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        image_np = np.array(image.convert("RGB"))
        result_image, emotion = detect_emotion_from_image(image_np)

        if result_image is not None:
            st.image(result_image, caption=f"Detected Emotion: {emotion}", use_column_width=True)
            st.success(f"{name}, you're feeling {emotion}!")

# Coming soon section
st.markdown("---")
st.markdown("🎙️ **Voice emotion detection coming soon...**", unsafe_allow_html=True)

# Emoji loading animation
with st.spinner("Analyzing..."):
    animated_loader()
