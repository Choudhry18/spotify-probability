import streamlit as st
import json

def upload_data(key):
    st.title(f"Upload Your Spotify {key}")
    st.markdown("Please upload as JSON file.")

    uploaded_file = st.file_uploader("Choose a file", type=["json"], key=key)

    if uploaded_file is not None:
        try:
            # Load the JSON data
            data = json.load(uploaded_file)
            st.success("File uploaded successfully!")
            # You can pass the data to the analysis component here
            return data
        except json.JSONDecodeError:
            st.error("Error: The file is not a valid JSON.")
        except Exception as e:
            st.error(f"An error occurred: {e}")

    return None