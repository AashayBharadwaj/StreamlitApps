import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px

def create_gender_pie_chart(male, female):
    data = {'Gender': ['Male', 'Female'], 'Count': [male, female]}
    fig = px.pie(data, values='Count', names='Gender', color='Gender',
                 color_discrete_map={'Male': '#3498db', 'Female': '#e74c3c'})
    fig.update_traces(textposition='inside', textinfo='percent+label')
    return fig



# Sample data for the locations
location_metrics = {
    "Dallas": {
        "Headcount": 120,
        "YTD Turnover Rate": "8%",
        "Gender Representation": {"Male": 70, "Female": 50}
    },
    "Austin": {
        "Headcount": 95,
        "YTD Turnover Rate": "10%",
        "Gender Representation": {"Male": 55, "Female": 40}
    },
    "New York": {
        "Headcount": 150,
        "YTD Turnover Rate": "7%",
        "Gender Representation": {"Male": 90, "Female": 60}
    },
    "Chicago": {
        "Headcount": 130,
        "YTD Turnover Rate": "9%",
        "Gender Representation": {"Male": 75, "Female": 55}
    },
    
  
    "Miami": {
        "Headcount": 80,
        "YTD Turnover Rate": "5%",
        "Gender Representation": {"Male": 40, "Female": 40}
    },
    "Seattle": {
        "Headcount": 115,
        "YTD Turnover Rate": "12%",
        "Gender Representation": {"Male": 60, "Female": 55}
    },
    "Denver": {
        "Headcount": 90,
        "YTD Turnover Rate": "11%",
        "Gender Representation": {"Male": 45, "Female": 45}
    },
    "Atlanta": {
        "Headcount": 100,
        "YTD Turnover Rate": "6%",
        "Gender Representation": {"Male": 50, "Female": 50}
    },
    "Boston": {
        "Headcount": 85,
        "YTD Turnover Rate": "8%",
        "Gender Representation": {"Male": 45, "Female": 40}
    },
      "San Francisco": {
        "Headcount": 110,
        "YTD Turnover Rate": "6%",
        "Gender Representation": {"Male": 60, "Female": 50}
    }
}
import streamlit as st
import matplotlib.pyplot as plt
def create_card(location, metrics):
    with st.container():
        st.markdown(f"""
            <style>
            .metric {{
                font-size: 16px;
                text-align: left;
                margin-bottom: 10px;
                color: #2c3e50;  # Adjust text color as needed
            }}
            .card {{
                background-color: #ffffff;
                border-radius: 8px;
                padding: 15px;
                box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
                margin: 10px;
            }}
            </style>
            <div class="card">
                <h2 style="color: #2980b9;">{location} Metrics</h2>
                <div class="metric"><strong>Headcount:</strong> {metrics["Headcount"]}</div>
                <div class="metric"><strong>YTD Turnover Rate:</strong> {metrics["YTD Turnover Rate"]}</div>
                <div class="metric"><strong>Gender Representation:</strong>
                """, unsafe_allow_html=True)
        # Display the pie chart
        fig = create_gender_pie_chart(metrics["Gender Representation"]["Male"], metrics["Gender Representation"]["Female"])
        st.plotly_chart(fig, use_container_width=True)
        st.markdown("</div></div>", unsafe_allow_html=True)


def main():
    st.image('Bravas-Football-Theme.png', caption='KNOW YOUR NUMBERS! LEAD THE GAME!!', use_column_width=True)
    st.title('Bravas Location Metrics Dashboard')

    # Sidebar selection for the number of cards
    number_of_cards = st.sidebar.selectbox(
        "How many locations do you want to display?",
        options=[str(n) for n in range(1, len(location_metrics) + 1)],
        index=4  # Default to 5 cards
    )
    number_of_cards = int(number_of_cards)

    # Display the selected number of cards
    locations = list(location_metrics.keys())[:number_of_cards]
    num_rows = (len(locations) + 4) // 5  # Calculate rows needed for 5 cards per row
    index = 0
    for _ in range(num_rows):
        cols = st.columns(3)  # Always create 5 columns
        for col in cols:
            if index < len(locations):
                location = locations[index]
                with col:
                    create_card(location, location_metrics[location])
                index += 1
            else:
                break

if __name__ == "__main__":
    main()
