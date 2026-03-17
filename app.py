import streamlit as st
import random

# --- PAGE CONFIG ---
st.set_page_config(page_title="Python Discovery Lab", page_icon="🧪")

# --- SIDEBAR NAVIGATION ---
st.sidebar.title("🚀 Projects")
app_mode = st.sidebar.selectbox(
    "Choose a Project:",
    ["Home", "🔢 Mystery Number", "🤖 Cyber-Hero Creator", "🌈 Mood Painter", "📐 Triangle Master"]
)

# --- HOME ---
if app_mode == "Home":
    st.title("🐍 Python Discovery Lab")
    st.markdown("""
    ### Welcome Grade 8! 
    Today, you aren't just using an app—you're looking at the **logic** that builds the internet. 
    Pick a project in the sidebar to begin.
    """)
    st.image("https://images.unsplash.com/photo-1542831371-29b0f74f9713?w=800")

# --- 1. MYSTERY NUMBER ---
elif app_mode == "🔢 Mystery Number":
    st.title("🔢 The Mystery Number Game")
    if 'secret' not in st.session_state:
        st.session_state.secret = random.randint(1, 100)
        st.session_state.count = 0
    guess = st.number_input("Guess (1-100):", min_value=1, max_value=100)
    if st.button("Check Guess"):
        st.session_state.count += 1
        if guess < st.session_state.secret: st.warning("Higher! 📈")
        elif guess > st.session_state.secret: st.warning("Lower! 📉")
        else: 
            st.success(f"Correct! Found in {st.session_state.count} tries.")
            st.balloons()
            if st.button("Reset"): del st.session_state.secret

# --- 2. HERO CREATOR ---
elif app_mode == "🤖 Cyber-Hero Creator":
    st.title("🤖 Cyber-Hero Identity")
    u_name = st.text_input("What is your name?")
    if st.button("Generate Hero"):
        if u_name:
            hero = f"Cyber {u_name}"
            st.header(f"Hero: {hero}")
            st.image(f"https://robohash.org/{hero}.png?set=set1", width=250)
        else: st.error("Enter a name!")

# --- 3. MOOD PAINTER ---
elif app_mode == "🌈 Mood Painter":
    st.title("🌈 Mood Painter")
    mood_text = st.text_input("How are you feeling?")
    if st.button("Analyze Mood"):
        if mood_text:
            st.image(f"https://picsum.photos/seed/{mood_text}/800/400")
            st.success("Mood visualized!")

# --- 4. TRIANGLE MASTER ---
elif app_mode == "📐 Triangle Master":
    st.title("📐 Triangle Master")
    calc = st.radio("Calculate:", ["Area", "Perimeter", "Hypotenuse"])
    if calc == "Area":
        b = st.number_input("Base:", min_value=0.1)
        h = st.number_input("Height:", min_value=0.1)
        if st.button("Calculate"): st.success(f"Area: {0.5 * b * h}")
    elif calc == "Perimeter":
        s1 = st.number_input("Side 1:", min_value=0.1)
        s2 = st.number_input("Side 2:", min_value=0.1)
        s3 = st.number_input("Side 3:", min_value=0.1)
        if st.button("Calculate"): st.success(f"Perimeter: {s1+s2+s3}")
    else:
        a = st.number_input("Side a:", min_value=0.1)
        b = st.number_input("Side b:", min_value=0.1)
        if st.button("Calculate"): st.success(f"Hypotenuse: {round((a**2 + b**2)**0.5, 2)}")

st.sidebar.markdown("---")
st.sidebar.write("🛠️ Created for Grade 8 Tech Lab")
