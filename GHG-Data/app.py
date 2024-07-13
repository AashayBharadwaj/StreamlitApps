import streamlit as st
from functions import load_data, filter_data_for_year, create_choropleth_figure, plot_gdp_vs_ghg

# Set page configuration to wide
st.set_page_config(layout="wide")

# Initialize session state for checkboxes
if 'show_global_emissions' not in st.session_state:
    st.session_state.show_global_emissions = True

if 'show_country_level' not in st.session_state:
    st.session_state.show_country_level = False

# Title
st.title("Global GHG Emissions Visualization Tool")

# Sidebar for selecting the view
st.sidebar.header("Select View")

# Checkbox for GHG emissions over the years
if st.sidebar.checkbox("GHG emissions over the years", value=st.session_state.show_global_emissions):
    st.session_state.show_global_emissions = True
    st.session_state.show_country_level = False
else:
    st.session_state.show_global_emissions = False

# Checkbox and Selectbox for Country level data
if st.sidebar.checkbox("Country level data", value=st.session_state.show_country_level):
    st.session_state.show_global_emissions = False
    st.session_state.show_country_level = True
    country_option = st.sidebar.selectbox(
        'Select Country Data View',
        ('GDP vs GHG Emissions', 'Option 2', 'Option 3')
    )
else:
    st.session_state.show_country_level = False

# Load data
data = load_data()

if st.session_state.show_global_emissions:
    # Slider for year selection based on available years in the data
    year = st.slider("Select Year", min_value=int(data['year'].min()), max_value=int(data['year'].max()), value=int(data['year'].min()))

    # Filter data for the selected year
    year_data = filter_data_for_year(data, year)

    # Create Plotly figure
    fig = create_choropleth_figure(year_data)

    # Center-align the map
    st.markdown(
        """
        <style>
        .center-align {
            display: flex;
            justify-content: center;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown('<div class="center-align">', unsafe_allow_html=True)
    st.plotly_chart(fig)
    st.markdown('</div>', unsafe_allow_html=True)

    # Show detailed data button
    if st.button("Show Detailed Data"):
        st.write(year_data)

if st.session_state.show_country_level:
    if country_option == 'GDP vs GHG Emissions':
        country = st.selectbox("Select Country", data['country'].unique())
        plot_gdp_vs_ghg(data, country)
    else:
        st.write(f"Country level data - {country_option} will be displayed here.")
        # Placeholder for the other country-level data function
        # You will provide the function details
