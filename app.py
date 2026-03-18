import streamlit as st
import random
import time
import pandas as pd

# --- 1. INITIALIZE GAME STATES ---
if 'clicks' not in st.session_state:
    st.session_state.clicks = 0
    st.session_state.multiplier = 1
    st.session_state.start_time = None
    st.session_state.time_limit = 60
    st.session_state.game_over = False
    st.session_state.cost_mult = 100
    st.session_state.cost_time = 50
    st.session_state.cost_freeze = 25
    st.session_state.freeze_until = 0
    st.session_state.leaderboard = []

# --- 2. SIDEBAR NAVIGATION ---
st.sidebar.title("🚀 Python Lab")
app_mode = st.sidebar.selectbox(
    "Select a Project:",
    ["Home", "🔢 Mystery Number", "🤖 Cyber-Hero Creator", "🌈 Mood Painter", "📐 Triangle Master", "🚀 Clicker Tycoon"]
)

# --- 3. PROJECT: HOME ---
if app_mode == "Home":
    st.title("🐍 Welcome to the Python Discovery Lab")
    st.write("Pick a project in the sidebar to see Python in action!")
    st.image("https://images.unsplash.com/photo-1542831371-29b0f74f9713?w=800")

# --- 4. PROJECT: MYSTERY NUMBER ---
elif app_mode == "🔢 Mystery Number":
    st.title("🔢 The Mystery Number")
    if 'secret' not in st.session_state: st.session_state.secret = random.randint(1, 100)
    guess = st.number_input("Guess (1-100):", min_value=1, max_value=100)
    if st.button("Check"):
        if guess < st.session_state.secret: st.warning("Higher! 📈")
        elif guess > st.session_state.secret: st.warning("Lower! 📉")
        else: 
            st.success("Correct! 🎉")
            st.balloons()
            del st.session_state.secret

# --- 5. PROJECT: CYBER-HERO ---
elif app_mode == "🤖 Cyber-Hero Creator":
    st.title("🤖 Cyber-Hero Identity")
    u_name = st.text_input("Enter your name:")
    if st.button("Generate"):
        if u_name:
            st.header(f"Hero: Cyber {u_name}")
            st.image(f"https://robohash.org/{u_name}.png?set=set1", width=250)
        else: st.error("Please enter a name!")

# --- 6. PROJECT: MOOD PAINTER ---
elif app_mode == "🌈 Mood Painter":
    st.title("🌈 Mood Painter")
    mood_text = st.text_input("How are you feeling?")
    if st.button("Analyze Mood"):
        st.image(f"https://picsum.photos/seed/{mood_text}/800/400")
        st.success("Visualizing your vibe...")

# --- 7. PROJECT: TRIANGLE MASTER ---
elif app_mode == "📐 Triangle Master":
    st.title("📐 Triangle Master")
    b = st.number_input("Base:", min_value=0.1)
    h = st.number_input("Height:", min_value=0.1)
    if st.button("Calculate Area"):
        st.success(f"The Area is: {0.5 * b * h}")

# --- 8. PROJECT: CLICKER TYCOON ---
elif app_mode == "🚀 Clicker Tycoon":
    st.title("🚀 Python Clicker Tycoon")
    
    # Timer Logic
    if st.session_state.start_time is not None and not st.session_state.game_over:
        if time.time() < st.session_state.freeze_until:
            st.info(f"❄️ TIME FROZEN! ({int(st.session_state.freeze_until - time.time())}s)")
            time_left = st.session_state.display_time_left # Keep time same during freeze
        else:
            elapsed = time.time() - st.session_state.start_time
            time_left = max(0, st.session_state.time_limit - elapsed)
            st.session_state.display_time_left = time_left
        
        if time_left <= 0: st.session_state.game_over = True
    else:
        time_left = st.session_state.time_limit

    # Stats Display
    c1, c2, c3 = st.columns(3)
    c1.metric("Clicks", f"{st.session_state.clicks:.0f}")
    c2.metric("Multiplier", f"x{st.session_state.multiplier}")
    c3.metric("Time", f"{int(time_left)}s")

    if not st.session_state.game_over:
        if st.button("🖱️ CLICK FOR CASH!", use_container_width=True):
            if st.session_state.start_time is None: st.session_state.start_time = time.time()
            st.session_state.clicks += (1 * st.session_state.multiplier)
            st.rerun()
    else:
        st.error("⌛ GAME OVER!")
        final_score = st.session_state.clicks
        name = st.text_input("Enter name for Leaderboard:")
        if st.button("Save Score"):
            st.session_state.leaderboard.append({"User": name, "Score": final_score})
            # Reset Game
            st.session_state.clicks, st.session_state.multiplier = 0, 1
            st.session_state.start_time, st.session_state.game_over = None, False
            st.session_state.cost_mult, st.session_state.cost_time, st.session_state.cost_freeze = 100, 50, 25
            st.rerun()

    st.divider()
    st.subheader("🛒 Upgrade Shop")
    s1, s2, s3 = st.columns(3)
    
    with s1:
        if st.button(f"x2 Mult ({st.session_state.cost_mult}c)"):
            if st.session_state.clicks >= st.session_state.cost_mult:
                st.session_state.clicks -= st.session_state.cost_mult
                st.session_state.multiplier *= 2
                st.session_state.cost_mult *= 2
                st.rerun()
    with s2:
        if st.button(f"+1 Min ({st.session_state.cost_time}c)"):
            if st.session_state.clicks >= st.session_state.cost_time:
                st.session_state.clicks -= st.session_state.cost_time
                st.session_state.time_limit += 60
                st.session_state.cost_time *= 2
                st.rerun()
    with s3:
        if st.button(f"Freeze ({st.session_state.cost_freeze}c)"):
            if st.session_state.clicks >= st.session_state.cost_freeze:
                st.session_state.clicks -= st.session_state.cost_freeze
                st.session_state.freeze_until = time.time() + 10
                st.session_state.time_limit += 10 # Add 10s to offset the freeze
                st.session_state.cost_freeze *= 2
                st.rerun()

    st.divider()
    if st.session_state.leaderboard:
        st.subheader("🏆 Leaderboard")
        st.table(pd.DataFrame(st.session_state.leaderboard).sort_values(by="Score", ascending=False))

# --- FOOTER ---
st.sidebar.markdown("---")
st.sidebar.write("✅ All systems go!")
