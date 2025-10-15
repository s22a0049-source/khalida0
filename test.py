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

st.header("4. Average Semester Performance Trend")
try:
    sem_cols = [col for col in arts_faculty_df.columns if col.endswith('_Sem_1') or col.endswith('_Sem_2') or col.endswith('_Sem_3')]
    
    if sem_cols:
        # Calculate the mean performance for each semester column
        semester_averages = arts_faculty_df[sem_cols].mean().reset_index()
        semester_averages.columns = ['Semester', 'Average_Score']
        
        # Order the semesters logically for the line chart
        semester_order = [
            '1st_Sem_1', '1st_Sem_2', '1st_Sem_3', 
            '2nd_Sem_1', '2nd_Sem_2', '2nd_Sem_3', 
            '3rd_Sem_1', '3rd_Sem_2', '3rd_Sem_3', 
            '4th_Sem_1', '4th_Sem_2', '4th_Sem_3'
        ]
        semester_averages['Semester'] = pd.Categorical(semester_averages['Semester'], categories=semester_order, ordered=True)
        semester_averages = semester_averages.sort_values('Semester').dropna()
        
        fig4 = px.line(
            semester_averages,
            x='Semester',
            y='Average_Score',
            markers=True,
            title='Average Performance Across All Semesters',
            template='plotly_white'
        )
        st.plotly_chart(fig4, use_container_width=True)
except Exception as e:
    st.warning(f"Viz 4 Error: {e}")
