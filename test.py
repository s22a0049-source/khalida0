import pandas as pd

# URL of the raw CSV file on GitHub
csv_url = "https://raw.githubusercontent.com/s22a0049-source/khalida0/refs/heads/main/arts_faculty_data.csv"

try:
    # Read the CSV file directly into a pandas DataFrame
    arts_faculty_df = pd.read_csv(csv_url)
    
    # Display the first few rows to confirm it loaded
    print("Data loaded successfully! Head of the DataFrame:")
    print(arts_faculty_df.head())
    
    # You can now proceed with your analysis on arts_faculty_df
    # For example, to count genders:
    print("\nGender counts:")
    print(arts_faculty_df['Gender'].value_counts())
    
except Exception as e:
    print(f"An error occurred while loading the data: {e}")
