import streamlit as st
import base64

def load_image(image_path):
    with open(image_path, "rb") as file:
        return file.read()

def create_id_card(name):
    # Load the image data
    image_data = load_image("images/man-purple.png")
    
    # Encode image data to base64 for HTML embedding
    encoded_image = base64.b64encode(image_data).decode()

    st.markdown(
        f"""
        <div style="
            background-color: #ffffff; 
            border: 1px solid #ddd; 
            border-radius: 10px; 
            padding: 20px; 
            margin: 15px;  
            text-align: center; 
            box-shadow: 4px 4px 15px rgba(0, 0, 0, 0.1);
            width: 230px; 
            height: auto; 
            display: flex;
            flex-direction: column;
            justify-content: space-between;">
            <img src="data:image/png;base64,{encoded_image}" alt="Profile Image" style="width:100px; height:auto; align-self: center;">
            <h3 style="color: #0077b6; font-size: 1.5rem; margin: 10px 0; text-align: center; font-weight: bold;">
                {name}
            </h3>
        </div>
        """,
        unsafe_allow_html=True
    )

def main():
    st.title("Custom ID Card Generator")
    name_input = st.text_input("Enter your name", "John Doe")
    
    if st.button("Generate ID Card"):
        create_id_card(name_input)

if __name__ == "__main__":
    main()
