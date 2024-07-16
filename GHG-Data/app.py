import streamlit as st
from functions import load_data, filter_data_for_year, create_choropleth_figure, plot_gdp_vs_ghg, animate_year_slider, plot_regional_co2_trends

# Set page configuration to wide
st.set_page_config(layout="wide")

# Initialize session state for checkboxes
if 'show_global_emissions' not in st.session_state:
    st.session_state.show_global_emissions = True

if 'show_country_level' not in st.session_state:
    st.session_state.show_country_level = False

if 'show_regional_trends' not in st.session_state:
    st.session_state.show_regional_trends = False

if 'year' not in st.session_state:
    st.session_state.year = 1750



# Sidebar for selecting the view
st.sidebar.header("Select View")

# Add new sidebar option for Regional CO2 Trends
view_option = st.sidebar.radio(
    "Choose a view",
    ("Global Emissions Over Time", "Country Level Data", "Regional CO2 Trends")
)

# Logic to handle different view options
if view_option == "Global Emissions Over Time":
    st.session_state.show_global_emissions = True
    st.session_state.show_country_level = False
    st.session_state.show_regional_trends = False
elif view_option == "Country Level Data":
    st.session_state.show_global_emissions = False
    st.session_state.show_country_level = True
    st.session_state.show_regional_trends = False
elif view_option == "Regional CO2 Trends":
    st.session_state.show_global_emissions = False
    st.session_state.show_country_level = False
    st.session_state.show_regional_trends = True

# Load data
data = load_data()

if st.session_state.show_global_emissions:
    # Title
    st.title("Global GHG Emissions Visualization Tool")
    # Slider for year selection based on available years in the data
    year = st.slider("Select Year", min_value=int(data['year'].min()), max_value=int(data['year'].max()), value=st.session_state.year, key='year_slider')

    # Filter data for the selected year
    year_data = filter_data_for_year(data, year)

    # Create Plotly figure
    fig = create_choropleth_figure(year_data)

    # Create columns for layout
    col1, col2 = st.columns([3, 2])  # Adjust ratio as needed

    # Place the map in the first column
    with col1:
        st.plotly_chart(fig)

    # Add explanatory text in the second column
    with col2:
        st.markdown("""
        <div style="font-size:20px;">
        <h3>Key Insights</h3>
        <ul>
            <li><strong>Data Source</strong>: The data is sourced from the "Our World in Data" database, providing a comprehensive view of global GHG emissions over the years.</li>
            <li><strong>Trends</strong>: Observe the changes in CO2 emissions over time, identifying key trends. (Notice the trend: GHG emissions in the US rose from the mid-1800s to the late 1900s, then declined. During this decline, emissions in China and India began to rise.)</li>
            <li><strong>Interactivity</strong>: Use the slider to explore emissions data for different years. Hover over countries to see detailed information.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div style="font-size:16px; margin-top:20px;">
        Watch the animation of how GHG emissions have changed over time.
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("Watch Animation"):
            animate_year_slider()

    # Show detailed data button
    if st.button("Show Detailed Data"):
        st.write(year_data)

if st.session_state.show_country_level:
    country = st.selectbox("Select Country", data['country'].unique())
    plot_gdp_vs_ghg(data, country)

    # Placeholder for the other country-level data function
    # You will provide the function details

if st.session_state.show_regional_trends:
    st.title("Testing the title for now!")
    plot_regional_co2_trends()
