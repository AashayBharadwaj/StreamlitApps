import pandas as pd

def load_data(filepath):
    """
    Load the GHG emissions data from a CSV file.
    """
    return pd.read_csv(filepath)

def preprocess_data(df):
    """
    Preprocess the data as needed for the app.
    """
    # Example preprocessing steps (to be customized based on actual data needs)
    df = df.dropna(subset=['LATITUDE', 'LONGITUDE'])  # Removing rows with missing coordinates
    return df
