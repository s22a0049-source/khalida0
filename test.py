import streamlit as st
import pandas as pd

# The raw URL for the CSV file on GitHub
GITHUB_CSV_URL = "https://raw.githubusercontent.com/s22a0049-source/khalida0/refs/heads/main/arts_faculty_data.csv"

# Use st.cache_data to load the data efficiently.
# This prevents the data from being re-downloaded every time the app updates.
@st.cache_data
def load_data(url):
    """Loads data from a URL using pandas, trying common encodings."""
    try:
        # Most web files are UTF-8
        df = pd.read_csv(url, encoding='utf-8')
    except UnicodeDecodeError:
        # Fallback to Latin-1 if UTF-8 fails
        df = pd.read_csv(url, encoding='latin-1')
    return df

# Load the DataFrame
arts_faculty_df = load_data(GITHUB_CSV_URL)

# --- Streamlit App Layout ---

st.title("Arts Faculty Data from GitHub")

st.subheader("First 5 Rows of the DataFrame")

# Display the head of the DataFrame using Streamlit's data functions
st.dataframe(arts_faculty_df.head(), use_container_width=True)

# Optional: Display overall statistics or the whole DataFrame
# st.subheader("Data Overview")
# st.write(f"Total rows: {len(arts_faculty_df)}")
