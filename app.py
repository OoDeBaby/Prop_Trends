import streamlit as st
import subprocess
import pandas as pd

# Function to run data.py
def run_data_py():
    # Run data.py using subprocess
    subprocess.run(["python", "data.py"], check=True)

# Function to run filters.py
def run_filters_py():
    # Run filters.py using subprocess
    subprocess.run(["python", "filters.py"], check=True)

# Function to load CSV data
def load_csv_data():
    try:
        df_8 = pd.read_csv('players_8_filters.csv')
        df_7 = pd.read_csv('players_7_filters.csv')
        df_6 = pd.read_csv('players_6_filters.csv')
        return df_8, df_7, df_6
    except FileNotFoundError:
        st.error("One or more CSV files are missing!")
        return None, None, None

# Main App Interface
def main():
    st.title("Basketball Player Filters App")
    
    st.write("""
    Click Button, Get Money
    """)
    
    # Button to trigger the process
    if st.button('Generate and View Filters'):
        with st.spinner("Running data.py and filters.py..."):
            # Run data.py and filters.py in sequence
            run_data_py()  # Runs data.py
            run_filters_py()  # Runs filters.py
        st.success("Process complete!")
        
        # Load and display CSV data
        df_8, df_7, df_6 = load_csv_data()
        
        if df_8 is not None:
            st.subheader("Players hitting 8 filters")
            st.write(df_8)

        if df_7 is not None:
            st.subheader("Players hitting 7 filters")
            st.write(df_7)
        
        if df_6 is not None:
            st.subheader("Players hitting 6 filters")
            st.write(df_6)

# Run the app
if __name__ == "__main__":
    main()
