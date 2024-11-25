import streamlit as st
from data_dict import location_metrics  # Import the dummy data
st.set_page_config( initial_sidebar_state="collapsed")

def create_location_card(location_name):
    """Function to create a card with metrics for a location."""
    metrics = location_metrics[location_name]  # Fetch metrics for the location
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
            <h3 style="color: #0077b6; font-size: 1.5rem; margin: 0; text-align: center; font-weight: bold;">
                {location_name}
            </h3>
            <hr style="border: none; height: 1px; background-color: #ddd; margin: 10px 0;">
            <p style="margin: 5px 0; font-size: 0.9rem; color: #555;"><strong>Headcount:</strong> {metrics['Headcount']}</p>
            <p style="margin: 5px 0; font-size: 0.9rem; color: #555;"><strong>Turnover Rate:</strong> {metrics['Turnover Rate']}</p>
            <p style="margin: 5px 0; font-size: 0.9rem; color: #555;"><strong>Total Revenue:</strong> {metrics['Total Revenue']}</p>
            <p style="margin: 5px 0; font-size: 0.9rem; color: #555;"><strong>Total Proposals:</strong> {metrics['Total Proposals']}</p>
            <p style="margin: 5px 0; font-size: 0.9rem; color: #555;"><strong>Active Projects:</strong> {metrics['Active Projects']}</p>
        </div>
        """,
        unsafe_allow_html=True
    )


# Add the cover image
st.image(
    "images/Wide-NFL.png",  # Replace with the path to your image
    use_column_width=True  # Ensures the image spans the full width
)

# Add your title below the image
st.markdown(
    """
    <h1 style="font-size: 2.5rem; font-weight: bold; margin-bottom: 10px; text-align: center;">
    KNOW YOUR NUMBERS!<br>LEAD THE GAME!!
    </h1>
    """,
    unsafe_allow_html=True
)

def main():
    st.markdown(
        "<h2 style='text-align: center;'>Bravas Locations Overview</h2>",
        unsafe_allow_html=True,
    )

    # Add a dropdown to select the time period
    st.sidebar.title('Select a time period')
    time_period = st.sidebar.selectbox(
        "Select Time Period:",
        ["YTD", "MTD", "Last Year"],
        index=0  # Default to "YTD"
    )

    # Display selected time period
    st.markdown(
    f"""
    <div style="text-align: center; font-size: 1rem; margin-top: 10px;">
        Showing <strong>{time_period}</strong> data!
    </div>
    """,
    unsafe_allow_html=True
)

    # Get all location names
    locations = list(location_metrics.keys())

    # Display cards
    cols1 = st.columns(3)
    for i in range(3):
        with cols1[i]:
            create_location_card(locations[i])

    cols2 = st.columns(3)
    for j in range(3, 6):
        with cols2[j - 3]:
            create_location_card(locations[j])

    cols3 = st.columns(3)
    for k in range(6, 9):
        with cols3[k - 6]:
            create_location_card(locations[k])

    cols4 = st.columns(3)
    for l in range(9, 12):
        with cols4[l - 9]:
            create_location_card(locations[l])


if __name__ == "__main__":
    main()