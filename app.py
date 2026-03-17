import streamlit as st
import random
import random
import cv2
import mediapipe as mp
from streamlit_webrtc import webrtc_streamer, VideoTransformerBase

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(page_title="Python Discovery Lab", page_icon="🧪", layout="centered")

# --- 2. SIDEBAR NAVIGATION ---
st.sidebar.title("🚀 Navigation")
st.sidebar.write("Switch between projects below:")
app_mode = st.sidebar.selectbox(
    "Choose a Project:",
    ["Home", "🔢 Mystery Number", "🤖 Cyber-Hero Creator", "🖌️ Mood Painter","📷Cam Game"]
)

# --- 3. HOME PAGE ---
if app_mode == "Home":
    st.title("🐍 Welcome to the Python Lab!")
    st.markdown("""
    ### Why are we here?
    Today, you aren't just using an app—you're looking at the **logic** that builds the internet. 
    Python is the language used by NASA, Spotify, and Netflix.
    
    **Try the projects in the sidebar to see what Python can do!**
    """)
    # A cool coding-themed image
    st.image("https://images.unsplash.com/photo-1542831371-29b0f74f9713?w=800", caption="Code is the language of the future.")

# --- 4. PROJECT 1: MYSTERY NUMBER ---
elif app_mode == "🔢 Mystery Number":
    st.title("🔢 The Mystery Number Game")
    st.write("Can you beat the computer's brain?")
    
    if 'secret' not in st.session_state:
        st.session_state.secret = random.randint(1, 100)
        st.session_state.count = 0

    guess = st.number_input("Enter a guess (1-100):", min_value=1, max_value=100)
    
    if st.button("Check Guess"):
        st.session_state.count += 1
        if guess < st.session_state.secret:
            st.warning("Too low! 📈 Try a bigger number.")
        elif guess > st.session_state.secret:
            st.warning("Too high! 📉 Try a smaller number.")
        else:
            st.success(f"BOOM! You found it in {st.session_state.count} tries!")
            st.balloons()
            if st.button("Play Again?"):
                st.session_state.secret = random.randint(1, 100)
                st.session_state.count = 0

# --- 5. PROJECT 2: CYBER-HERO CREATOR ---
elif app_mode == "🤖 Cyber-Hero Creator":
    st.title("🤖 Cyber-Hero Identity")
    st.write("Input your data to generate a unique digital avatar.")
    
    u_name = st.text_input("What is your name?")
    u_power = st.selectbox("Select your Power Source:", ["Solar", "Atomic", "Digital", "Magic"])
    
    if st.button("Generate Hero"):
        if u_name:
            adjectives = ["Quantum", "Shadow", "Neon", "Turbo", "Glitch", "Iron"]
            hero_name = f"{random.choice(adjectives)} {u_name}"
            st.header(f"Your Hero: {hero_name}")
            st.info(f"Primary Ability: {u_power} Blasts")
            
            # This generates a unique robot face based on the hero name
            st.image(f"https://robohash.org/{hero_name}.png?set=set1", width=250)
        else:
            st.error("Please enter a name first!")

# --- 6. PROJECT 3: MOOD PAINTER ---
elif app_mode == "🖌️ Mood Painter":
    st.title("🖌️ Python Mood Painter")
    st.write("How are you feeling today? Python will 'read' your words.")

    user_text = st.text_input("Type a sentence about your day:", placeholder="I'm feeling amazing!")

    if st.button("Analyze My Vibes"):
        if user_text:
            # Simple keyword matching logic
            pos_words = ["happy", "great", "amazing", "good", "cool", "fun", "excited", "awesome"]
            neg_words = ["sad", "bad", "bored", "tired", "angry", "hate", "terrible"]

            score = 0
            text_lower = user_text.lower()
            for word in pos_words:
                if word in text_lower: score += 1
            for word in neg_words:
                if word in text_lower: score -= 1

            if score > 0:
                st.balloons()
                st.success("✨ POSITIVE VIBES DETECTED!")
                # Shows a bright colorful image
                st.image(f"https://picsum.photos/seed/{user_text}/800/400", caption="Your Mood in Colors")
            elif score < 0:
                st.info("🌧️ Rainy day vibes detected.")
                # Shows a grayscale image
                st.image(f"https://picsum.photos/seed/{user_text}/800/400?grayscale", caption="The Grayscale of Logic")
            else:
                st.warning("😐 Neutral / Mystery Vibes. Try more descriptive words!")
            
            st.write(f"**Python Logic Result:** Happiness Score = {score}")
        else:
            st.error("You need to type something first!")

# --- NEW! PROJECT 4: AI GESTURE CAMERA ---
    elif app_mode == "📸 AI Gesture Camera":
        st.title("📸 AI Hand-Tracking Camera")
        st.write("This uses **Mediapipe AI** to track your hand in real-time through the browser!")
    
        # Mediapipe setup
        mp_hands = mp.solutions.hands
        hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.5)
        mp_draw = mp.solutions.drawing_utils
    
        class VideoProcessor(VideoTransformerBase):
            def transform(self, frame):
                img = frame.to_ndarray(format="bgr24")
                img = cv2.flip(img, 1)
                
                # AI Processing
                results = hands.process(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
                
                if results.multi_hand_landmarks:
                    for hand_lms in results.multi_hand_landmarks:
                        mp_draw.draw_landmarks(img, hand_lms, mp_hands.HAND_CONNECTIONS)
                        
                        # Detect Pinch (Calculation like your code)
                        thumb = hand_lms.landmark[4]
                        index = hand_lms.landmark[8]
                        dist = ((thumb.x - index.x)**2 + (thumb.y - index.y)**2)**0.5
                        
                        if dist < 0.04:
                            cv2.putText(img, "PINCH DETECTED!", (50, 50), 
                                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                
                return img
    
        webrtc_streamer(key="gesture", video_transformer_factory=VideoProcessor)
        
        st.info("💡 Note: You'll need to allow camera access in your browser to try this!")

# (Make sure to include the elif blocks for the other projects we built above!)

# --- FOOTER ---
st.sidebar.markdown("---")
st.sidebar.write("🛠️ Created for Grade 8 Tech Lab")

