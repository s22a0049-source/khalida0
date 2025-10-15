import pandas as pd

try:
    df = pd.read_csv('/content/drive/MyDrive/STUDENT-SURVEY.csv', encoding='utf-8')
except UnicodeDecodeError:
    df = pd.read_csv('/content/drive/MyDrive/STUDENT-SURVEY.csv', encoding='latin-1')
import streamlit as st
import pandas as pd

# The raw URL for the CSV file on GitHub
GITHUB_CSV_URL = 'https://raw.githubusercontent.com/s22a0049-source/khalida0/refs/heads/main/arts_faculty_data.csv'

# Use st.cache_data to load the data efficiently. 
# This decorator ensures the data is only downloaded once when the app is run.
@st.cache_data
def load_data(url):
    """Loads data from a URL using pandas, trying common encodings."""
    try:
        # Try UTF-8 first (standard for web files)
        df = pd.read_csv(url, encoding='utf-8')
    except UnicodeDecodeError:
        # Fallback to Latin-1 if UTF-8 fails
        df = pd.read_csv(url, encoding='latin-1')
    except Exception as e:
        # Handle other loading errors
        st.error(f"Error loading data from URL: {e}")
        return pd.DataFrame() # Return empty DataFrame on failure
    return df

# Load the DataFrame
df = load_data(GITHUB_CSV_URL)

# --- Streamlit App Layout ---

st.title("Arts Faculty Data from GitHub")

if not df.empty:
    st.subheader("First 5 Rows of Data")

    # st.dataframe replaces the Jupyter/Colab 'display(df.head())'
    st.dataframe(df.head(), use_container_width=True)
else:
    st.warning("Data could not be loaded. Please check the URL and file.")
display(df.head())
