import streamlit as st
import random

# 1. Page Configuration
st.set_page_config(page_title="Python Discovery Lab", page_icon="🧪")

# 2. Sidebar Navigation
st.sidebar.title("Select a Project")
app_mode = st.sidebar.selectbox(
    "What do you want to try?",
    ["Home", "🔢 Mystery Number", "🤖 Cyber-Hero Creator"]
)

# --- HOME PAGE ---
if app_mode == "Home":
    st.title("🐍 Welcome to the Python Lab!")
    st.write("""
    This app was built entirely in **Python**. 
    Use the menu on the left to switch between two different projects!
    
    * **Project 1:** Tests your logic with numbers.
    * **Project 2:** Uses text and images to create something new.
    """)
    st.image("https://images.unsplash.com/photo-1515879218367-8466d910aaa4?w=800", caption="Coding is your new superpower.")

# --- PROJECT 1: MYSTERY NUMBER ---
elif app_mode == "🔢 Mystery Number":
    st.title("🔢 The Mystery Number Game")
    
    if 'secret' not in st.session_state:
        st.session_state.secret = random.randint(1, 100)
        st.session_state.count = 0

    guess = st.number_input("Guess a number (1-100):", min_value=1, max_value=100)
    
    if st.button("Submit Guess"):
        st.session_state.count += 1
        if guess < st.session_state.secret:
            st.warning("Higher! 📈")
        elif guess > st.session_state.secret:
            st.warning("Lower! 📉")
        else:
            st.success(f"Correct! It took you {st.session_state.count} tries.")
            st.balloons()
            if st.button("Reset Game"):
                del st.session_state.secret

# --- PROJECT 2: CYBER-HERO ---
elif app_mode == "🤖 Cyber-Hero Creator":
    st.title("🤖 Cyber-Hero Identity")
    
    u_name = st.text_input("Enter your name:")
    u_power = st.selectbox("Choose your Element:", ["Fire", "Ice", "Code", "Gravity"])
    
    if st.button("Initialize Hero"):
        if u_name:
            adj = ["Quantum", "Shadow", "Neon", "Turbo"]
            hero_name = f"{random.choice(adj)} {u_name}"
            st.header(f"Hero Name: {hero_name}")
            st.subheader(f"Power: {u_power} Manipulation")
            
            # Generates a unique robot based on the name
            st.image(f"https://robohash.org/{hero_name}.png?set=set1", width=200)
        else:
            st.error("Please enter a name first!")

# --- FOOTER ---
st.sidebar.markdown("---")
st.sidebar.write("Created with ❤️ by your Teacher")
