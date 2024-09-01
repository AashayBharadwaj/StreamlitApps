import streamlit as st
from data_management import load_data, preprocess_data
from visualizations import create_bar_chart,  create_bar_chart_company, create_folium_map  # Folium map function
from streamlit_folium import folium_static
from branca.element import Template, MacroElement


# Load and preprocess data
df = load_data('StreamlitApps/data.csv')
df = preprocess_data(df)

# Sidebar options
st.sidebar.title("GHG Emissions Dashboards")
option = st.sidebar.radio("Choose a Dashboard", ("Top GHG Emitters by Facility", "Emissions Map",  "Emissions by Company"))

if option == "Top GHG Emitters by Facility":
    top_n = st.selectbox("Select number of top emitters:", (10, 20, 30, 40, 50))
    fig = create_bar_chart(df, top_n)
    st.plotly_chart(fig)

elif option == "Emissions Map":
        folium_map = create_folium_map(df)
        folium_static(folium_map)
        st.write("### Legend")
        st.write("""
        - **Crimson Circle**: Indicates GHG emission points
        - **Circle Size**: Proportional to emission quantity(Hover over the circles to see the actual emissions)
        
        """)  # You can use Markdown to format this text
        

# Additional dashboard option "Sector Analysis" can be developed and integrated later
elif option =="Emissions by Company":
    top_n = st.selectbox("Select number of top emitters:", (10, 20, 30, 40, 50))
    fig = create_bar_chart_company(df, top_n)
    st.plotly_chart(fig)
