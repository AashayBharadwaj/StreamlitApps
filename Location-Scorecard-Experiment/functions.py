import base64
import streamlit as st
from data_dict import location_metrics, salesperson_metrics, salesleaderboard_metrics

def load_image(image_path):
    """Helper function to encode an image file to base64."""
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode('utf-8')

def create_location_card(location_name):
    """Function to create a card with metrics, an image, manager info, and a button to view the org chart for a location."""
    metrics = location_metrics[location_name]
    encoded_image = load_image(metrics['Image'])

    st.markdown(
        f"""
        <div style="
            background-color: #ffffff; 
            border: 1px solid #ddd; 
            border-radius: 10px; 
            padding: 20px; 
            margin: 15px;  
            text-align: left; 
            box-shadow: 4px 4px 15px rgba(0, 0, 0, 0.1);
            width: 230px; 
            height: auto; 
            display: flex;
            flex-direction: column;
            justify-content: space-between;">
            <img src="data:image/png;base64,{encoded_image}" style="width: 100%; border-radius: 10px; margin-bottom: 10px;">
            <h3 style="color: #0077b6; font-size: 1.5rem; margin: 0; text-align: center; font-weight: bold;">
                {location_name}
            </h3>
            <p style="color: #666; font-size: 1rem; margin-top: 5px; text-align: center;">
                LOM: {metrics['Manager']}
            </p>
            <hr style="border: none; height: 1px; background-color: #ddd; margin: 10px 0;">
            <p style="margin: 5px 0; font-size: 0.9rem; color: #555;"><strong>Headcount:</strong> {metrics['Headcount']}</p>
            <p style="margin: 5px 0; font-size: 0.9rem; color: #555;"><strong>Turnover Rate:</strong> {metrics['Turnover Rate']}</p>
            <p style="margin: 5px 0; font-size: 0.9rem; color: #555;"><strong>Total Revenue:</strong> {metrics['Total Revenue']}</p>
            <p style="margin: 5px 0; font-size: 0.9rem; color: #555;"><strong>Total Proposals:</strong> {metrics['Total Proposals']}</p>
            <p style="margin: 5px 0; font-size: 0.9rem; color: #555;"><strong>Active Projects:</strong> {metrics['Active Projects']}</p>
            <button style="margin-top: 10px; padding: 5px 20px; font-size: 0.9rem; background-color: #0077b6; color: white; border: none; border-radius: 5px;">
                   <a href="https://bravasdesign-my.sharepoint.com/:u:/g/personal/aashay_bharadwaj_bravas_com/EeA_dotWCIZJn_5dsHdvE_MB_d2WflsrLo6qtGLAOpg1Ow?e=Wm7hT1" style="text-decoration: none; color: white;" onclick="document.getElementById('org-chart-image').style.display='block';return false;">
                        View Org Chart
                    </a>
            </button>
        </div>
        """,
        unsafe_allow_html=True
    )
    

def create_salesperson_card(salesperson_name):
    """Function to create a card with salesperson metrics and an image."""
    metrics = salesperson_metrics[salesperson_name]  # Fetch metrics for the salesperson
    encoded_image = load_image(metrics['Image'])

    st.markdown(
        f"""
        <div style="
            background-color: #ffffff; 
            border: 1px solid #ddd; 
            border-radius: 10px; 
            padding: 20px; 
            margin: 15px;  
            text-align: left; 
            box-shadow: 4px 4px 15px rgba(0, 0, 0, 0.1);
            width: 230px; 
            height: auto; 
            display: flex;
            flex-direction: column;
            justify-content: space-between;">
            <img src="data:image/png;base64,{encoded_image}" style="width: 100%; border-radius: 20px; margin-bottom: 10px;">
            <h3 style="color: #0077b6; font-size: 1.5rem; margin: 0; text-align: center; font-weight: bold;">
                {salesperson_name}
            </h3>
            <hr style="border: none; height: 1px; background-color: #ddd; margin: 10px 0;">
            <p style="margin: 5px 0; font-size: 0.9rem; color: #555;"><strong>Tenure:</strong> {metrics['Tenure']}</p>
            <p style="margin: 5px 0; font-size: 0.9rem; color: #555;"><strong>Number of Proposals:</strong> {metrics['Number of Proposals']}</p>
            <p style="margin: 5px 0; font-size: 0.9rem; color: #555;"><strong>MTD Sales:</strong> {metrics['MTD Sales']}</p>
            <p style="margin: 5px 0; font-size: 0.9rem; color: #555;"><strong>YTD Sales:</strong> {metrics['YTD Sales']}</p>
            <button style="margin-top: 10px; padding: 5px 20px; font-size: 0.9rem; background-color: #0077b6; color: white; border: none; border-radius: 5px;">
                    <a href="https://bravasdesign-my.sharepoint.com/:u:/g/personal/aashay_bharadwaj_bravas_com/EeA_dotWCIZJn_5dsHdvE_MB_d2WflsrLo6qtGLAOpg1Ow?e=Wm7hT1" style="text-decoration: none; color: white;" onclick="document.getElementById('org-chart-image').style.display='block';return false;">
                        View Detailed Sales
                    </a>
            </button>
        </div>
        """,
        unsafe_allow_html=True
    )



def create_leaderboard_card(salesperson_name):
    """Function to create a card for the sales leaderboard."""
    metrics = salesleaderboard_metrics[salesperson_name]
    encoded_image = load_image(metrics["Image"])

    st.markdown(
        f"""
        <div style="
            background-color: #ffffff; 
            border: 1px solid #ddd; 
            border-radius: 10px; 
            padding: 15px; 
            margin: 10px;  
            text-align: center; 
            box-shadow: 4px 4px 15px rgba(0, 0, 0, 0.1);
            width: 150px; 
            height: 400px;  /* Ensures consistent card height */
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: space-between;">
            <img src="data:image/png;base64,{encoded_image}" style="width: 80px; height: 80px; border-radius: 50%; margin-bottom: 10px;">
            <h3 style="color: #0077b6; font-size: 1.25rem; margin: 0; font-weight: bold;">
                {salesperson_name}
            </h3>
            <hr style="border: none; height: 1px; background-color: #ddd; margin: 10px 0;">
            <p style="margin: 5px 0; font-size: 0.9rem; color: #555;"><strong>MTD Sales:</strong> {metrics["MTD Sales"]}</p>
            <p style="margin: 5px 0; font-size: 0.9rem; color: #555;"><strong>% of MTD Goal:</strong> {metrics["% of MTD Goal"]}</p>
            <p style="margin: 5px 0; font-size: 0.9rem; color: #555;"><strong>YTD Sales 2024:</strong> {metrics["YTD Sales 2024"]}</p>
        </div>
        """,
        unsafe_allow_html=True
    )
