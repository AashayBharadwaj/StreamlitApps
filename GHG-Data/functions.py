import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

@st.cache_data
def load_data():
    return pd.read_csv('data/ghg_emissions_with_coordinates.csv')

@st.cache_data
def filter_data_for_year(data, year):
    return data[data['year'] == year]

def create_choropleth_figure(data):
    # Custom color scale from light green to red with 10 shades
    custom_color_scale = [
        [0.0, 'rgb(144,238,144)'],  # Light green
        [0.1, 'rgb(173,255,47)'],
        [0.2, 'rgb(240,230,140)'],
        [0.3, 'rgb(255,255,0)'],
        [0.4, 'rgb(255,215,0)'],
        [0.5, 'rgb(255,165,0)'],
        [0.6, 'rgb(255,140,0)'],
        [0.7, 'rgb(255,69,0)'],
        [0.8, 'rgb(255,0,0)'],
        [0.9, 'rgb(178,34,34)'],
        [1.0, 'rgb(139,0,0)']       # Dark red
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
            bgcolor='rgba(255,255,255,1)'  # Set the background color of the map area to white
        ),
        paper_bgcolor='rgba(255,255,255,1)',  # Set the background color of the entire figure to white
        plot_bgcolor='rgba(255,255,255,1)',  # Set the background color of the plot area to white
        width=1000,  # Set the width of the figure
        height=600,  # Set the height of the figure
        coloraxis_colorbar=dict(
            title="CO2 Emissions",
            titlefont=dict(color='black'),  # Color of the legend title
            tickfont=dict(color='black'),   # Color of the legend ticks
            bgcolor='rgba(0,0,0,0)',        # Background color of the color bar (transparent)
        )
    )

    return fig

import plotly.graph_objects as go
import streamlit as st

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