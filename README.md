# PDF Text Extractor and Summarizer

## Overview

This is a Python application built with Streamlit that allows you to upload a PDF file, extract the text from it, and generate a summary. It's useful for quickly getting the main points from a PDF document without having to read through the entire thing.

## Features

* **PDF Text Extraction:** Extracts all readable text from uploaded PDF files.
* **Text Summarization:** Generates a concise summary of the extracted text.
* **File Upload:** Users can upload PDF files directly through the Streamlit interface.
* **Summary Length Adjustment:** A slider allows users to control the maximum number of sentences in the summary.
* **Error Handling:** The app handles common errors such as file not found and unreadable content, providing informative messages to the user.
* **Clear Output:** The extracted text and the generated summary are displayed in the Streamlit interface.

## How It Works

1.  **File Upload:** The user uploads a PDF file through the Streamlit web interface.
2.  **Text Extraction:** The application extracts the text content from the uploaded PDF using the `pypdf` library.
3.  **Text Summarization:** The extracted text is then summarized using the following process:
    * The text is tokenized into words and sentences using the `nltk` library.
    * Stop words are removed, and a frequency table of the remaining words is created.
    * Sentences are scored based on the frequency of the words they contain.
    * The top-scoring sentences are selected to form the summary.
4.  **Output:** The extracted text and the summary are displayed in the Streamlit web interface.

## Technologies Used

* Python
* Streamlit
* pypdf
* NLTK (Natural Language Toolkit)

## Setup

### Prerequisites

* Python 3.6 or higher 
* pip (Python package installer)

### Installation

1.  **Clone the repository (Optional):**
    ```bash
    git clone <repository_url>
    cd <repository_name>
    ```
2.  **Create a virtual environment (Recommended):**
    ```bash
    python3 -m venv .venv
    ```
    * Activate the virtual environment:
        * On macOS and Linux:
            ```bash
            source .venv/bin/activate
            ```
        * On Windows:
            ```bash
            .venv\Scripts\activate
            ```
3.  **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```
    * A `requirements.txt` file should contain:
        ```
        streamlit
        pypdf
        nltk
        ```

### Running the Application

1.  Run the Streamlit application from your terminal:
    ```bash
    streamlit run your_app_file.py
    ```
    (Replace `your_app_file.py` with the name of your Python file, e.g., `pdf_summarizer.py`)
2.  The application will open in your default web browser.

## Usage

1.  Open the application in your web browser.
2.  Click on the "Browse files" button to upload a PDF file.
3.  The application will process the file and display the extracted text and a summary.
4.  Use the slider to adjust the maximum number of sentences in the summary.

##  Important Notes

* The application requires the `nltk` library, and it downloads the `punkt` and `stopwords` datasets.
* The uploaded PDF file is temporarily stored on the server during processing and is deleted afterward.
* The quality of the summary depends on the content of the PDF file.
