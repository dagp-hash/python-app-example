import streamlit as st
import random

st.set_page_config(page_title="Python Magic 101", page_icon="🐍")

st.title("🐍 Python Mystery Number!")
st.write("Welcome, future coder! Python is more than just text; it's the brain behind this game.")

# Initialize the secret number in the session so it doesn't change on every click
if 'secret_number' not in st.session_state:
    st.session_state.secret_number = random.randint(1, 100)
    st.session_state.attempts = 0

# The Game Interface
guess = st.number_input("I'm thinking of a number between 1 and 100. Can you find it?", min_value=1, max_value=100)

if st.button("Check My Guess"):
    st.session_state.attempts += 1
    if guess < st.session_state.secret_number:
        st.warning("📈 Too low! Try a bigger number.")
    elif guess > st.session_state.secret_number:
        st.warning("📉 Too high! Go a bit lower.")
    else:
        st.success(f"🎉 BOOM! You got it in {st.session_state.attempts} tries!")
        st.balloons()
        if st.button("Play Again?"):
            st.session_state.secret_number = random.randint(1, 100)
            st.session_state.attempts = 0

# The "Interest Hook" - Explaining the code
with st.expander("👀 See the 'Brain' (The Code)"):
    st.code(f"""
# This is the logic you just played!
if guess < secret_number:
    print("Too low!")
elif guess > secret_number:
    print("Too high!")
else:
    print("You win!")
    """, language='python')