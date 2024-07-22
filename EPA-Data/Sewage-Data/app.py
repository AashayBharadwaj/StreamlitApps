import streamlit as st 
import pandas as pd
import plotly.express as px
from viz import create_bar_chart, create_aggregated_bar_chart, create_bar_chart_new, create_folium_map 
from streamlit_folium import st_folium

st.title("Spillage data")
df = pd.read_csv("data_cleaned.csv")


# Sidebar options
st.sidebar.title("Spillage data")
option = st.sidebar.radio('Choose an option', ("Top n spills by entity", "Top n individual spills", "Map", "Data by year"))

if option == "Top n spills by entity":
    top_n = st.number_input("Enter the number of top emitters:", min_value=1, max_value=100, value=10)
    fig_sum, fig_count = create_aggregated_bar_chart(df, top_n)
    st.plotly_chart(fig_sum)  # Corrected function to display the Plotly chart
    st.write("The above data is the total spills by the entities mentioned in the chart during the total time period. These are not individual spills.")
    st.plotly_chart(fig_count)
    st.write("The above data is the count of spills for the entities.")
    
    
    st.write(df.head(top_n))  # Display only the top_n rows of the sorted DataFrame
    
elif option == "Top n individual spills":
    top_n = st.number_input("Enter the number of top emitters:", min_value=1, max_value=100, value=10)
    fig = create_bar_chart_new(df, top_n)  # Make sure to use the correct function name for Matplotlib
    st.pyplot(fig)  # Use st.pyplot to display Matplotlib figures
    st.write(df.head(top_n))  # Display only the top_n rows of the sorted DataFrame

elif option == "Map":
        # Create the folium map using the defined function
    emissions_map = create_folium_map(df)

    # Display the folium map in Streamlit using st_folium
    st_folium(emissions_map, width=700, height=500)