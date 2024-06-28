import streamlit as st
import time

# Function to create typing animation
def typing_animation(text, speed=0.05):
    animated_text = ''
    placeholder = st.empty()
    for char in text:
        animated_text += char
        placeholder.markdown(f'<p style="font-size:24px; color:#83B4FF; font-weight:bold;">{animated_text}</p>', unsafe_allow_html=True)
        time.sleep(speed)

@st.cache_data
def render_header_and_text():
    # Header
    st.title("Stock Tracking Dashboard")

    # Text with typing animation
    lines = [
        "Welcome to the stock tracking dashboard.",
        "Choose a stock from the sidebar dropdown.",
        "Compare two stocks side by side."
    ]

    for line in lines:
        typing_animation(line)
        time.sleep(1)
