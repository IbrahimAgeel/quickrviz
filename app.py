from pygwalker.api.streamlit import StreamlitRenderer
import pandas as pd
import streamlit as st
import sys
import pygwalker

st.set_page_config(layout="wide")

st.title("QuickrViz")

# Allow CSV files as well, as they are very common
uploaded_file = st.sidebar.file_uploader("Upload an Excel or CSV file", type=['xlsx', 'csv'])

if uploaded_file is not None:
    try:
        # Check the file type to use the correct pandas function
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)

        st.success("File loaded successfully! Explore your data below.")

        # --- FIX: Move these two lines inside the 'if' block ---
        pyg_app = StreamlitRenderer(df)
        pyg_app.explorer()
        # ---------------------------------------------------------

    except Exception as e:
        st.error(f"Error loading file: {e}")
else:
    st.info("☝️ Please upload a file to get started.")
