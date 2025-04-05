# app.py
import streamlit as st
import folium
from functions import create_location_card, create_salesperson_card, create_leaderboard_card
from data_dict import location_metrics, salesperson_metrics, location_coords, salesleaderboard_metrics

st.set_page_config(initial_sidebar_state="collapsed")

def main():
    # Sidebar Navigation
    st.sidebar.title('Navigation')
    page_selection = st.sidebar.selectbox(
        "Select a View:",
        ["Location Scorecard Overview", "Sales Overview", "Map", "Sales Leaderboard"]
    )

    # Add a dropdown to select the time period
    st.sidebar.title('Select a time period')
    time_period = st.sidebar.selectbox(
        "Select Time Period:",
        ["YTD", "MTD", "Last Year"],
        index=0  # Default to "YTD"
    )

    if page_selection == "Location Scorecard Overview":
        st.image(
            "Location-Scorecard/images/Wide-NFL.png",
            use_column_width=True
        )
        st.markdown(
            "<h1 style='text-align: center; color:black'>Lone Star Listings - Locations Overview</h1>",
            unsafe_allow_html=True,
        )
        st.markdown(
            """
            <h2 style='text-align: center;'>
            <strong>Gamifying Analytics : Track and compare branch metrics to spark competition.</strong>.
            </h2>
            """,
            unsafe_allow_html=True
        )
        locations = list(location_metrics.keys())
        for i in range(0, len(locations), 3):
            cols = st.columns(3)
            for idx, col in enumerate(cols):
                if i + idx < len(locations):
                    with col:
                        create_location_card(locations[i + idx])

    elif page_selection == "Sales Overview":
        st.image(
            "Location-Scorecard/images/Sale_Racechart.png",  # Replace with the path to your image
            use_column_width=True
        )
        st.markdown(
            "<h1 style='text-align: center;'>Lone Star Listings - Overview</h1>",
            unsafe_allow_html=True,
        )
        salespersons = list(salesperson_metrics.keys())
        for i in range(0, len(salespersons), 3):  # Adjust for 3 cards per row
            cols = st.columns(3)
            for idx, col in enumerate(cols):
                if i + idx < len(salespersons):
                    with col:
                        create_salesperson_card(salespersons[i + idx])

    elif page_selection == "Map":
        import folium
        from streamlit_folium import st_folium
        from data_dict import location_coords, reported_issues  # Ensure these are defined in `data_dict.py`

        # Initialize the map centered at the US
        m = folium.Map(location=[37.0902, -95.7129], zoom_start=4)

        # Add location markers and circles for reported issues
        for location, metrics in location_metrics.items():
            if location in location_coords:
                lat = location_coords[location]["Lat"]
                lon = location_coords[location]["Lon"]
                
                # Create the popup content
                popup_content = f"""
                <b>Location:</b> {location}<br>
                <b>Headcount:</b> {metrics['Headcount']}<br>
                <b>Turnover Rate:</b> {metrics['Turnover Rate']}<br>
                <b>Total Revenue:</b> {metrics['Total Revenue']}<br>
                <b>Total Proposals:</b> {metrics['Total Proposals']}<br>
                <b>Active Projects:</b> {metrics['Active Projects']}<br>
                <b>Reported Issues:</b> {reported_issues[location]}
                """
                
                # Add the marker
                folium.Marker(
                    location=[lat, lon],
                    popup=folium.Popup(popup_content, max_width=300),
                    icon=folium.Icon(color="blue", icon="info-sign"),
                ).add_to(m)

                # Add a red circle for reported issues with a tooltip
                folium.Circle(
                    location=[lat, lon],
                    radius=reported_issues[location] * 15000,  # Scale the circle size
                    color="red",
                    fill=True,
                    fill_color="red",
                    fill_opacity=0.4,
                    tooltip=f"{reported_issues[location]} issues reported in the last month.",  # Tooltip with the issue count
                ).add_to(m)

        # Render the map in Streamlit
        st_folium(m, width=800, height=500)

    elif page_selection == "Sales Leaderboard":
        st.image(
            "Location-Scorecard/images/leaderboard.jpg",  # Replace with the path to your image
            use_column_width=True
        )
        st.markdown(
            "<h1 style='text-align: center;'>Lone Star Listings - Sales Leaderboard</h1>",
            unsafe_allow_html=True,
        )
        st.markdown(
            """
            <h2 style="font-size: 2rem; font-weight: bold; margin-bottom: 10px; text-align: center;">
            CELEBRATE THE TOP PERFORMERS!
            </h2>
            """,
            unsafe_allow_html=True,
        )
        # Display leaderboard cards
        salespeople = list(salesleaderboard_metrics.keys())
        for i in range(0, len(salespeople), 4):  # Adjust for 4 cards per row
            cols = st.columns(4)  # Create 4 columns in the row
            for idx, col in enumerate(cols):
                if i + idx < len(salespeople):  # Ensure not to exceed the number of salespeople
                    with col:
                        create_leaderboard_card(salespeople[i + idx])

if __name__ == "__main__":
    main()
