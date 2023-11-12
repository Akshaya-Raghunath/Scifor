## Text Sentiment Analysis

## Overview

This project is a simple sentiment analysis application built with Python using the Streamlit library for the user interface and TextBlob for sentiment analysis. 
The application allows users to analyze the sentiment of individual text inputs or upload a CSV file for batch sentiment analysis.

## Features

1. **Analyze Text:**
   - Input any text into the application.
   - Instantly see the sentiment analysis results, including polarity and subjectivity scores.

2. **Analyze CSV:**
   - Upload a CSV file containing a 'text' column.
   - Perform sentiment analysis on each text entry in the CSV.
   - View the sentiment scores and analysis for the first ten entries.

3. **Download Results:**
   - Download the analyzed data as a CSV file for further analysis.

## Dependencies

- Python 3.x
- TextBlob
- pandas
- streamlit

## Access the application in your browser at [http://localhost:8501](http://localhost:8501).

## Usage

- Enter text in the 'Analyze Text' section to perform sentiment analysis on individual inputs.
- Upload a CSV file in the 'Analyze CSV' section to analyze sentiment for multiple entries.
- Download the analyzed data using the 'Download data as CSV' button.
