import streamlit as st
from data_management import load_data, preprocess_data
from visualizations import create_bar_chart,  create_bar_chart_company, create_choropleth_map, create_folium_map  # Folium map function
from streamlit_folium import folium_static


# Load and preprocess data
df = load_data('StreamlitApps/EPA-Data/data.csv')
df = preprocess_data(df)

# Sidebar options
st.sidebar.title("GHG Emissions Dashboards")
option = st.sidebar.radio("Choose a Dashboard", ("Top GHG Emitters by Facilities", "Emissions Map",  "Emissions by Company"))

if option == "Top GHG Emitters by Facilities":
    top_n = st.selectbox("Select number of top emitters:", (10, 20, 30, 40, 50))
    fig = create_bar_chart(df, top_n)
    st.plotly_chart(fig)

elif option == "Emissions Map":
    st.write("This is the Emissions Map dashboard.")  # Debug statement
    folium_map = create_folium_map(df)
        # Streamlit's method to display Folium maps
    folium_static(folium_map)

# Additional dashboard option "Sector Analysis" can be developed and integrated later
elif option =="Emissions by Company":
    top_n = st.selectbox("Select number of top emitters:", (10, 20, 30, 40, 50))
    fig = create_bar_chart_company(df, top_n)
    st.plotly_chart(fig)
