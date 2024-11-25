import streamlit as st
import folium
from streamlit_folium import st_folium
from data_dict import location_metrics  # Import your data

# Define the coordinates for each location
location_coords = {
    "Dallas": {"Lat": 32.7767, "Lon": -96.7970},
    "Austin": {"Lat": 30.2672, "Lon": -97.7431},
    "Denver": {"Lat": 39.7392, "Lon": -104.9903},
    "Houston": {"Lat": 29.7604, "Lon": -95.3698},
    "San Francisco": {"Lat": 37.7749, "Lon": -122.4194},
    "Miami": {"Lat": 25.7617, "Lon": -80.1918},
    "Boston": {"Lat": 42.3601, "Lon": -71.0589},
    "Seattle": {"Lat": 47.6062, "Lon": -122.3321},
    "Chicago": {"Lat": 41.8781, "Lon": -87.6298},
    "Phoenix": {"Lat": 33.4484, "Lon": -112.0740},
    "Los Angeles": {"Lat": 34.0522, "Lon": -118.2437},
    "New York": {"Lat": 40.7128, "Lon": -74.0060},
}

# Initialize the map centered at the US
m = folium.Map(location=[37.0902, -95.7129], zoom_start=4)

# Add location markers
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
        <b>Active Projects:</b> {metrics['Active Projects']}
        """
        
        # Add the marker
        folium.Marker(
            location=[lat, lon],
            popup=folium.Popup(popup_content, max_width=300),
            icon=folium.Icon(color="blue", icon="info-sign"),
        ).add_to(m)

# Streamlit App
st.title("Bravas Locations - Interactive Map with Folium")

# Render the map in Streamlit
st_folium(m, width=800, height=500)
