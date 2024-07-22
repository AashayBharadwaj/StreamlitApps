import plotly.express as px
import matplotlib.pyplot as plt
import folium


def create_bar_chart(df, top_n):
    """
    Create an interactive bar chart showing the top N GHG emitters.
    """
    data = df.nlargest(top_n, 'Amount')
    fig = px.bar(data, x='Regulated Entity Name', y='Amount', title=f'Top {top_n} spills in Texas')
    # Set the range of y-axis explicitly to avoid auto-scaling issues
    max_amount = data['Amount'].max()
    fig.update_layout(
        width=1400, 
        height=600, 
        yaxis=dict(range=[0, max_amount * 1.1])  # 10% more than the max to ensure all bars are fully visible
    )
    return fig

def create_bar_chart_new(df, top_n):
    """
    Create an interactive bar chart showing the top N GHG emitters using Matplotlib.
    """
    # Ensure the data is sorted and the top N is selected
    data = df.nlargest(top_n, 'Amount')

    # Creating the plot
    plt.figure(figsize=(10, 6))
    plt.bar(data['Regulated Entity Name'], data['Amount'], color='blue')
    plt.title(f'Top {top_n} spills in Texas')
    plt.xlabel('Regulated Entity Name')
    plt.ylabel('Amount')
    plt.xticks(rotation=45, ha='right')  # Rotate entity names for better readability
    plt.tight_layout()  # Adjust layout to make room for label rotation

    # Return the figure
    return plt.gcf()  # Get the current figure (plt.show() is not needed here as Streamlit handles it)


# def create_aggregated_bar_chart(df, top_n, title="Cumulative Spills by Entity"):
#     """
#     Create an interactive bar chart showing the cumulative spills by each regulated entity, limited to the top N entities.

#     Parameters:
#         df (pd.DataFrame): The DataFrame containing spill data.
#         top_n (int): Number of top entities to display.
#         title (str): The title of the chart.

#     Returns:
#         fig (plotly.graph_objs._figure.Figure): A Plotly figure object with the bar chart.
#     """
#     # Aggregate the data by 'Regulated Entity Name' and sum the 'Amount'
#     aggregated_data = df.groupby('Regulated Entity Name')['Amount'].sum().reset_index()

#     # Sort the data and select the top N entries
#     top_entities = aggregated_data.sort_values('Amount', ascending=False).head(top_n)

#     # Create a bar chart
#     fig = px.bar(top_entities, x='Regulated Entity Name', y='Amount', title=title)

#     # Update layout to better accommodate long entity names
#     fig.update_layout(xaxis_title="Regulated Entity",
#                       yaxis_title="Total Amount of Spills",
#                       xaxis_tickangle=-45,  # Rotate labels for better visibility if needed
#                       width=1400, height=600)
    
#     return fig


def create_aggregated_bar_chart(df, top_n, title="Cumulative Spills by Entity"):
    """

    """
    # Aggregate the data by 'Regulated Entity Name' for sum and count
    aggregated_data = df.groupby('Regulated Entity Name').agg(
        Total_Amount=('Amount', 'sum'),
        Spill_Count=('Amount', 'count')
    ).reset_index()

    # Sort the data and select the top N entries
    top_entities = aggregated_data.sort_values('Total_Amount', ascending=False).head(top_n)

    # Create a bar chart for the total amount of spills
    fig_sum = px.bar(top_entities, x='Regulated Entity Name', y='Total_Amount', title=f"{title} - Total Amount")
    fig_sum.update_layout(xaxis_title="Regulated Entity",
                          yaxis_title="Total Amount of Spills",
                          xaxis_tickangle=-45,  # Rotate labels for better visibility if needed
                          width=1400, height=600)

    # Create a bar chart for the count of spills
    fig_count = px.bar(top_entities, x='Regulated Entity Name', y='Spill_Count', title=f"{title} - Spill Count")
    fig_count.update_layout(xaxis_title="Regulated Entity",
                            yaxis_title="Count of Spills",
                            xaxis_tickangle=-45,  # Rotate labels for better visibility if needed
                            width=1400, height=600)

    return fig_sum, fig_count


def create_folium_map(df, initial_coords=(31.9686, -99.9018), initial_zoom=6):
    """
    Create an interactive map showing spill data using Folium.
    """
    # Create a map centered around the initial coordinates (Texas)
    map = folium.Map(location=initial_coords, zoom_start=initial_zoom, tiles='OpenStreetMap')
    
    # Add circle markers for each data point
    for idx, row in df.iterrows():
        # Calculate a scaled radius for visibility; adjust scaling factor as needed
        scaled_radius = row['Amount'] / 1000  # Example scaling factor, adjust this as per your data scale

        folium.CircleMarker(
            location=(row['latitude'], row['longitude']),
            radius=scaled_radius,  # Radius scaled based on the Amount
            popup=f"{row['County']}<br>Amount: {row['Amount']}",
            color='crimson',
            fill=True,
            fill_color='crimson'
        ).add_to(map)
    
    return map