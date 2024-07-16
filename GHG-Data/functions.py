import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
import time

@st.cache_data
def load_data():
    return pd.read_csv('data/ghg_emissions_with_coordinates.csv')

@st.cache_data
def filter_data_for_year(data, year):
    return data[data['year'] == year]

def create_choropleth_figure(data):
    # Custom color scale from light red to dark red with 10 shades
    custom_color_scale = [
        [0.0, 'rgb(255,204,204)'],  # Light red
        [0.1, 'rgb(255,178,178)'],
        [0.2, 'rgb(255,153,153)'],
        [0.3, 'rgb(255,128,128)'],
        [0.4, 'rgb(255,102,102)'],
        [0.5, 'rgb(255,77,77)'],
        [0.6, 'rgb(255,51,51)'],
        [0.7, 'rgb(255,26,26)'],
        [0.8, 'rgb(255,0,0)'],
        [0.9, 'rgb(204,0,0)'],
        [1.0, 'rgb(153,0,0)']       # Dark red
    ]

    # Create Plotly figure with animation
    fig = px.choropleth(
        data,
        locations="iso_code",
        color="co2",
        hover_name="country",
        color_continuous_scale=custom_color_scale,  # Use custom color scale here
        animation_frame="year",  # Set animation frame to year
        title="CO2 Emissions Over Time",
        labels={'co2': 'CO2 Emissions'}
    )

    # Update the layout to change the background color and size
    fig.update_layout(
        geo=dict(
            bgcolor='rgba(34,34,34,1)'  # Set the background color of the map area to dark grey
        ),
        paper_bgcolor='rgba(34,34,34,1)',  # Set the background color of the entire figure to dark grey
        plot_bgcolor='rgba(34,34,34,1)',  # Set the background color of the plot area to dark grey
        width=1000,  # Set the width of the figure
        height=600,  # Set the height of the figure
        coloraxis_colorbar=dict(
            title="CO2 Emissions (million metric tons)",
            titlefont=dict(color='white'),  # Color of the legend title
            tickfont=dict(color='white'),   # Color of the legend ticks
            bgcolor='rgba(0,0,0,0)',        # Background color of the color bar (transparent)
        )
    )

    return fig

def plot_gdp_vs_ghg(data, country):
    country_data = data[data['country'] == country]
    fig = go.Figure()

    # Add GDP trace with left y-axis
    fig.add_trace(go.Scatter(
        x=country_data['year'], 
        y=country_data['gdp'], 
        mode='lines', 
        name='GDP',
        yaxis='y1'
    ))

    # Add GHG Emissions trace with right y-axis
    fig.add_trace(go.Scatter(
        x=country_data['year'], 
        y=country_data['total_ghg'], 
        mode='lines', 
        name='Total GHG Emissions',
        yaxis='y2'
    ))

    # Update layout for dual y-axis and black background
    fig.update_layout(
        title=f"{country} - GDP vs GHG Emissions",
        xaxis=dict(title="Year"),
        yaxis=dict(
            title="GDP",
            titlefont=dict(color="#1f77b4"),
            tickfont=dict(color="#1f77b4")
        ),
        yaxis2=dict(
            title="Total GHG Emissions",
            titlefont=dict(color="#ff7f0e"),
            tickfont=dict(color="#ff7f0e"),
            overlaying='y',
            side='right'
        ),
        legend=dict(x=0, y=1),
        paper_bgcolor='rgba(0,0,0,1)',  # Set the background color to black
        plot_bgcolor='rgba(0,0,0,1)',   # Set the plot background color to black
        font=dict(color='white')        # Set the font color to white
    )

    st.plotly_chart(fig)

def animate_year_slider():
    start_year = 1750
    mid_year = 1950
    end_year = 2022
    early_interval = 10
    late_interval = 5
    sleep_time = 0.5

    current_year = start_year

    st.write("Animation started")
    
    while current_year <= mid_year:
        st.write(f"Updating year to: {current_year}")
        st.session_state.year = current_year
        time.sleep(sleep_time)
        current_year += early_interval
        st.rerun()

    while current_year <= end_year:
        st.write(f"Updating year to: {current_year}")
        st.session_state.year = current_year
        time.sleep(sleep_time)
        current_year += late_interval
        st.rerun()
    
    st.write("Animation ended")

@st.cache_data
def plot_regional_co2_trends():
    # Load data
    data = pd.read_csv('data/by_region.csv')

    # Rename columns for ease of use
    data.columns = ['Entity', 'Code', 'Year', 'Annual_CO2_emissions']

    # Create the stacked area chart
    fig = px.area(
        data,
        x='Year',
        y='Annual_CO2_emissions',
        color='Entity',
        title='Annual CO2 Emissions by World Region',
        labels={'Annual_CO2_emissions': 'CO2 Emissions (tonnes)', 'Year': 'Year'},
        color_discrete_sequence=px.colors.qualitative.Plotly  # Customize colors as needed
    )

    # Customize the layout and increase the height
    fig.update_layout(
        xaxis_title='Year',
        yaxis_title='CO2 Emissions (tonnes)',
        legend_title='Region',
        template='plotly_dark',  # Use 'plotly' for a light theme
        height=800  # Adjust the height as needed
    )

    # Display the chart in Streamlit
    st.plotly_chart(fig)
