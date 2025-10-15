import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

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



# 1. Define the Data Source
GITHUB_CSV_URL = "https://raw.githubusercontent.com/s22a0049-source/khalida0/refs/heads/main/arts_faculty_data.csv"

# 2. Function to Load and Cache Data
# Use st.cache_data to load the data efficiently from the web
@st.cache_data
def load_data(url):
    """Loads data from a URL using pandas, trying common encodings."""
    try:
        df = pd.read_csv(url, encoding='utf-8')
    except UnicodeDecodeError:
        df = pd.read_csv(url, encoding='latin-1')
    return df

# Load the DataFrame
arts_faculty_df = load_data(GITHUB_CSV_URL)

# --- Streamlit App ---

st.title("Gender Distribution in Arts Faculty")
st.subheader("Visualized with Matplotlib")

# 3. Create the Matplotlib Plot
try:
    # Corrected: Count the occurrences of each gender in the DataFrame
    gender_counts = arts_faculty_df['Gender'].value_counts()

    # Create the figure instance
    fig, ax = plt.subplots(figsize=(6, 6))

    # Generate the pie chart on the axis object (ax)
    ax.pie(
        gender_counts,
        labels=gender_counts.index,
        autopct='%1.1f%%',
        startangle=140
    )
    ax.set_title('Distribution of Gender in Arts Faculty')
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    # 4. Display the plot in Streamlit
    # st.pyplot() takes the Matplotlib figure object (fig) as an argument
    st.pyplot(fig)

except KeyError:
    st.error("Error: Could not find the 'Gender' column in the loaded data.")
except Exception as e:
    st.error(f"An unexpected error occurred: {e}")
