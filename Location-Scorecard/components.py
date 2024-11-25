import streamlit as st

def display_text_input():
    # Create a text input box and display the entered text
    user_input = st.text_input("Enter some text")
    st.write(f'You entered: {user_input}')

def display_button():
    # Create a button and display a message when clicked
    if st.button('Click Me'):
        st.write('Button was clicked!')

def display_checkbox():
    # Create a checkbox and display whether it is checked
    check = st.checkbox('Check me')
    if check:
        st.write('Checkbox is checked')
    else:
        st.write('Checkbox is unchecked')
