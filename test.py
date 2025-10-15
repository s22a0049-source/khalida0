import streamlit as st
import plotly.express as px
import pandas as pd

# Define the URL for the CSV file
GITHUB_CSV_URL = 'https://raw.githubusercontent.com/s22a0049-source/khalida0/refs/heads/main/arts_faculty_data.csv'

# Use st.cache_data for efficient data loading. 
# This prevents the file from being downloaded on every app interaction.
@st.cache_data
def load_data(url):
    """Loads data from a URL using pandas with latin-1 encoding."""
    # Using the specified 'latin-1' encoding from your original code
    try:
        df = pd.read_csv(url, encoding='latin-1')
    except Exception as e:
        st.error(f"Error loading data from URL: {e}")
        return pd.DataFrame() # Return empty DataFrame on failure
    return df

# Load the DataFrame
df = load_data(GITHUB_CSV_URL)

# --- Streamlit App Layout ---

st.title("Arts Faculty Data Loader from GitHub")

if not df.empty:
    st.subheader("First 5 Rows of Data")

    # st.dataframe is the Streamlit equivalent of display(df.head())
    st.dataframe(df.head(), use_container_width=True)
else:

    st.warning("Data could not be loaded. Please check the URL and file.")


# 1. Define the Data Source URL
GITHUB_CSV_URL = "https://raw.githubusercontent.com/s22a0049-source/khalida0/refs/heads/main/arts_faculty_data.csv"

# 2. Function to Load and Cache Data
# @st.cache_data ensures the data is downloaded and loaded only once for efficiency.
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

# --- Streamlit App Layout ---

st.title("Gender Distribution in Arts Faculty")
st.subheader("Interactive Pie Chart (Plotly Express)")

# 3. Prepare Data for Plotly Express
try:
    # Corrected: Count the occurrences of each gender in the DataFrame (arts_faculty_df)
    gender_counts = arts_faculty_df['Gender'].value_counts().reset_index()
    
    # Rename columns for clarity in Plotly Express (standard practice)
    gender_counts.columns = ['Gender', 'Count'] 

    # 4. Create the Pie Chart using Plotly Express
    # Plotly uses 'names' for labels and 'values' for the size of the slices
    fig = px.pie(
        gender_counts,
        names='Gender',        # Column for labels
        values='Count',        # Column for values/size
        title='Distribution of Gender in Arts Faculty',
        hole=0.4,              # Optional: Creates a donut chart
        color_discrete_sequence=px.colors.qualitative.Safe # Optional: Nice color scheme
    )
    
    # Update layout for presentation
    fig.update_traces(textposition='inside', textinfo='percent+label', rotation=140)

    # 5. Display the chart in Streamlit
    st.plotly_chart(fig, use_container_width=True)

except KeyError:
    st.error("Error: The column 'Gender' was not found in the loaded data.")
except Exception as e:
    st.error(f"An unexpected error occurred: {e}")

st.header("1. Gender Distribution (Overall)")

if 'Gender' in arts_faculty_df.columns:
    gender_counts = arts_faculty_df['Gender'].value_counts().reset_index()
    gender_counts.columns = ['Gender', 'Count'] 

    fig_pie = px.pie(
        gender_counts,
        names='Gender',
        values='Count',
        title='Faculty Gender Distribution',
        hole=0.4 # Donut chart
    )
    st.plotly_chart(fig_pie, use_container_width=True)
else:
    st.warning("Skipping Viz 1: 'Gender' column not found.")

st.header("2. HSC GPA Distribution by Program")
try:
    if all(col in arts_faculty_df.columns for col in ['Program', 'HSC_GPA']):
        # Clean up Program names if they are too specific
        df_viz2 = arts_faculty_df.copy()
        df_viz2['Program_Short'] = df_viz2['Program'].str.split(' in ').str[-1].fillna('Other')
        
        fig2 = px.box(
            df_viz2,
            x='Program_Short',
            y='HSC_GPA',
            color='Program_Short',
            title='HSC GPA Distribution Across Arts Programs',
            template='plotly_white'
        )
        fig2.update_layout(xaxis_title="Program", yaxis_title="HSC GPA")
        st.plotly_chart(fig2, use_container_width=True)
except Exception as e:
    st.warning(f"Viz 2 Error: {e}")
