import plotly.express as px

def create_bar_chart(df, top_n):
    """
    Create an interactive bar chart showing the top N GHG emitters.
    """
    data = df.nlargest(top_n, 'GHG QUANTITY (METRIC TONS CO2e)')
    fig = px.bar(data, x='FACILITY NAME', y='GHG QUANTITY (METRIC TONS CO2e)', title=f'Top {top_n} GHG Emitters in Texas')
    fig.update_layout(width=1400, height=600)
    return fig



def create_bar_chart_company(df, top_n):
    """
    Create an interactive bar chart showing the top N GHG emitters by parent company.
    """
    # Group by 'PARENT COMPANIES' and sum 'GHG QUANTITY (METRIC TONS CO2e)'
    data = df.groupby('PARENT COMPANIES')['GHG QUANTITY (METRIC TONS CO2e)'].sum().reset_index()
    
    # Sort the data and select the top N companies
    data = data.nlargest(top_n, 'GHG QUANTITY (METRIC TONS CO2e)')
    
    # Create the bar chart
    fig = px.bar(data, x='PARENT COMPANIES', y='GHG QUANTITY (METRIC TONS CO2e)', title=f'Top {top_n} GHG Emitters in Texas by Company')
    fig.update_layout(width=1400, height=600)  # Adjust these dimensions as needed
    return fig

import folium
from branca.element import MacroElement, Template, Element

def create_folium_map(df, initial_coords=(31.9686, -99.9018), initial_zoom=6):
    """
    Create an interactive GHG emissions map using Folium.
    """
    # Create a map centered around Texas
    map = folium.Map(location=initial_coords, zoom_start=initial_zoom, tiles='OpenStreetMap')
    
    # Add markers for each facility
    for idx, row in df.iterrows():
        folium.CircleMarker(
            location=(row['LATITUDE'], row['LONGITUDE']),
            radius=row['GHG QUANTITY (METRIC TONS CO2e)'] / 1000000,  # Adjust size for visibility
            popup=f"{row['FACILITY NAME']}<br>GHG: {row['GHG QUANTITY (METRIC TONS CO2e)']} metric tons CO2e",
            color='crimson',
            fill=True,
            fill_color='crimson'
        ).add_to(map)
        
    return map
