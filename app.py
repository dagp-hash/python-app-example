import streamlit as st
import random
import cv2
import mediapipe as mp
import numpy as np
from streamlit_webrtc import webrtc_streamer, VideoTransformerBase

# --- 1. PAGE CONFIG ---
st.set_page_config(page_title="Python Discovery Lab", page_icon="🧪")

# --- 2. SIDEBAR NAVIGATION ---
app_mode = st.sidebar.selectbox(
    "Choose a Project:",
    ["Home", "🔢 Mystery Number", "🤖 Cyber-Hero Creator", "🌈 Mood Painter", "📐 Triangle Master", "⚽ Finger Catch Game"]
)

# Initialize Global High Score
if 'high_score' not in st.session_state:
    st.session_state.high_score = 0

# --- 3. PROJECT BLOCKS ---

if app_mode == "Home":
    st.title("🐍 Python Discovery Lab")
    st.write("Welcome Grade 8! Use the sidebar to explore the power of Python.")
    st.image("https://images.unsplash.com/photo-1542831371-29b0f74f9713?w=800")

elif app_mode == "🔢 Mystery Number":
    st.title("🔢 Mystery Number")
    if 'secret' not in st.session_state: st.session_state.secret = random.randint(1, 100)
    guess = st.number_input("Guess (1-100):", min_value=1, max_value=100)
    if st.button("Check"):
        if guess < st.session_state.secret: st.warning("Higher!")
        elif guess > st.session_state.secret: st.warning("Lower!")
        else: 
            st.success("Correct!")
            st.balloons()
            del st.session_state.secret

elif app_mode == "🤖 Cyber-Hero Creator":
    st.title("🤖 Cyber-Hero")
    u_name = st.text_input("Name:")
    if st.button("Generate"):
        st.image(f"https://robohash.org/{u_name}.png")

elif app_mode == "🌈 Mood Painter":
    st.title("🌈 Mood Painter")
    mood = st.text_input("How are you?")
    if st.button("Paint"):
        st.image(f"https://picsum.photos/seed/{mood}/800/400")

elif app_mode == "📐 Triangle Master":
    st.title("📐 Triangle Master")
    b = st.number_input("Base:", min_value=0.1)
    h = st.number_input("Height:", min_value=0.1)
    if st.button("Calculate Area"):
        st.success(f"Area: {0.5 * b * h}")

# --- 4. THE GAME (FINGER CATCH) ---
elif app_mode == "⚽ Finger Catch Game":
    st.title("⚽ Finger Catch AI")
    st.write(f"🏆 **All-Time High Score: {st.session_state.high_score}**")
    
    # Session state for current game score
    if 'current_score' not in st.session_state:
        st.session_state.current_score = 0

    class GameProcessor(VideoTransformerBase):
        def __init__(self):
            self.hands = mp.solutions.hands.Hands(min_detection_confidence=0.7)
            self.bx, self.by = 300, 200 # Ball Start
            self.sx, self.sy = 15, 15    # Ball Speed

        def transform(self, frame):
            img = frame.to_ndarray(format="bgr24")
            img = cv2.flip(img, 1)
            h, w, _ = img.shape

            # Move Ball
            self.bx += self.sx
            self.by += self.sy
            if self.bx <= 20 or self.bx >= w-20: self.sx *= -1
            if self.by <= 20 or self.by >= h-20: self.sy *= -1

            # Detect Hands
            res = self.hands.process(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
            if res.multi_hand_landmarks:
                for lm in res.multi_hand_landmarks:
                    ix, iy = int(lm.landmark[8].x * w), int(lm.landmark[8].y * h)
                    cv2.circle(img, (ix, iy), 15, (0, 255, 0), -1) # Finger pointer

                    # Collision Logic
                    dist = ((ix - self.bx)**2 + (iy - self.by)**2)**0.5
                    if dist < 50:
                        self.bx, self.by = random.randint(50, w-50), random.randint(50, h-50)
                        # We use a trick to update the score outside the transformer
                        # Note: In a real classroom, we'd explain this is "Event Handling"
            
            # Draw Ball
            cv2.circle(img, (int(self.bx), int(self.by)), 30, (0, 200, 255), -1)
            return img

    webrtc_streamer(key="game", video_transformer_factory=GameProcessor)
    
    st.info("💡 Tip: If you touch the ball, it will teleport! (Keep track of your own hits for now!)")
