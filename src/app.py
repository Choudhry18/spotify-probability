import streamlit as st
import json
from components.data_upload import upload_data
from components.data_analysis import analyze_streaming_data
from components.visualization import plot_play_distribution

# Set the page configuration
st.set_page_config(page_title="Spotify Streaming Data Analysis", layout="wide")

# Load custom CSS for Spotify theme
with open("src/assets/spotify_theme.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Title of the app
st.title("Spotify Streaming Data Analysis")

# File uploader for Spotify streaming data

wrapped_data = upload_data("Wrapped Data")
streaming_data = upload_data("Streaming Data")

if streaming_data is not None and wrapped_data is not None:
    # Read the uploaded data

    # Analyze the data
    analysis_results = analyze_streaming_data(streaming_data, wrapped_data)

    # Display the analysis results
    st.subheader("Analysis Results")
    st.write(analysis_results)

    # Visualizations
    st.subheader("Visualizations")
    plot_play_distribution(analysis_results)
else:
    st.info("Please upload your Spotify streaming and wrapped data to get started.")