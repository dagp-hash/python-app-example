import streamlit as st
import random
import time

# --- 1. PAGE CONFIG ---
st.set_page_config(page_title="Python Discovery Lab", page_icon="🧪")

# --- 2. SIDEBAR ---
app_mode = st.sidebar.selectbox(
    "Choose a Project:",
    ["Home", "🔢 Mystery Number", "🤖 Cyber-Hero Creator", "🌈 Mood Painter", "📐 Triangle Master", "⚡ Reaction Timer"]
)

# --- HOME / MYSTERY / HERO / MOOD / TRIANGLE (Keep your existing simple code here) ---
if app_mode == "Home":
    st.title("🐍 Python Discovery Lab")
    st.write("Fast, reliable, and powered by code!")
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

# --- NEW! PROJECT 5: REACTION TIMER (No Camera Needed) ---
elif app_mode == "⚡ Reaction Timer":
    st.title("⚡ Python Reaction Test")
    st.write("How fast are your reflexes? Click the button as soon as it turns **GREEN**!")

    if 'start_time' not in st.session_state:
        st.session_state.start_time = 0
        st.session_state.waiting = False

    if not st.session_state.waiting:
        if st.button("Ready?"):
            st.session_state.waiting = True
            wait_time = random.uniform(2, 5)
            time.sleep(wait_time)
            st.session_state.start_time = time.time()
            st.rerun()
    else:
        if st.button("!! CLICK NOW !!"):
            reaction_time = time.time() - st.session_state.start_time
            st.success(f"Your Reaction Time: {round(reaction_time, 3)} seconds!")
            if reaction_time < 0.3: st.balloons()
            st.session_state.waiting = False
