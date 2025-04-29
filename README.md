# Spotify Streaming Data Analysis App

This project is a Streamlit application that allows users to upload their Spotify streaming data and view various analyses and visualizations. The application is designed with a Spotify-themed user interface, providing an engaging experience for users to explore their listening habits.

## Features

- **Data Upload**: Users can upload their Spotify streaming history in JSON format.
- **Data Analysis**: The app processes the uploaded data to calculate various statistics, such as the probability of hearing a favorite track and the analysis of skipping behavior.
- **Visualizations**: The application generates visualizations to help users understand their listening patterns and preferences.

## Project Structure

```
spotify-streamlit-app
├── src
│   ├── app.py                # Main entry point of the Streamlit application
│   ├── components            # Contains reusable components for the app
│   │   ├── __init__.py
│   │   ├── data_upload.py    # File uploader for Spotify data
│   │   ├── data_analysis.py   # Functions for data analysis
│   │   └── visualization.py   # Functions for generating visualizations
│   ├── assets                # Contains static assets like CSS
│   │   └── spotify_theme.css  # Custom CSS for Spotify theme
│   └── utils                 # Utility functions for data processing and API interaction
│       ├── __init__.py
│       ├── data_processing.py # Functions for processing uploaded data
│       └── spotify_api.py    # Functions for interacting with the Spotify API
├── requirements.txt          # Project dependencies
├── README.md                 # Project documentation
└── .streamlit
    └── config.toml          # Streamlit configuration settings
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd spotify-streamlit-app
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the Streamlit application:
   ```
   streamlit run src/app.py
   ```

2. Open your web browser and navigate to `http://localhost:8501` to access the application.

3. Upload your Spotify streaming data in JSON format and explore the analyses and visualizations.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.