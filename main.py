import streamlit as st
from pypdf import PdfReader
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import tempfile

# Ensure necessary NLTK data is downloaded (done only once per session)
try:
    nltk.data.find('punkt')
except LookupError:
    nltk.download('punkt')
try:
    nltk.data.find('stopwords')
except LookupError:
    nltk.download('stopwords')

# Function to extract text from a PDF
def extract_text_from_pdf(file_path):
    """
    Extracts text from a PDF file.

    Args:
        file_path (str): Path to the PDF file.

    Returns:
        str: Extracted text, or an error message if the file cannot be processed.
    """
    try:
        reader = PdfReader(file_path)
        all_text = "".join(page.extract_text() for page in reader.pages if page.extract_text())
        return all_text if all_text.strip() else "No readable text found in the PDF."
    except FileNotFoundError:
        return f"Error: File '{file_path}' not found."
    except Exception as e:
        return f"An error occurred: {e}"

# Function to summarize text
def summarize_text(text, max_sentences=30):
    """
    Summarizes the given text.

    Args:
        text (str): The text to summarize.
        max_sentences (int, optional): Maximum number of sentences in the summary. Defaults to 30.

    Returns:
        str: The summary of the text.
    """
    if not text.strip():
        return "No content to summarize."

    # Preprocess text
    stop_words = set(stopwords.words("english"))
    words = word_tokenize(text)

    # Create a frequency table for words
    freq_table = {}
    for word in words:
        word = word.lower()
        if word.isalpha() and word not in stop_words:  # Include only alphabetic, non-stop words
            freq_table[word] = freq_table.get(word, 0) + 1

    # Score sentences based on word frequencies
    sentences = sent_tokenize(text)
    sentence_scores = {}
    for sentence in sentences:
        for word in freq_table:
            if word in sentence.lower():
                sentence_scores[sentence] = sentence_scores.get(sentence, 0) + freq_table[word]

    # Sort and select top sentences
    ranked_sentences = sorted(sentence_scores.items(), key=lambda item: item[1], reverse=True)
    top_sentences = [sentence for sentence, _ in ranked_sentences[:max_sentences]]

    # Join top sentences to form the summary
    summary = " ".join(top_sentences)
    return summary if summary.strip() else "The text could not be summarized meaningfully."

def main():
    """
    Main function to run the Streamlit app.
    """
    st.title("PDF Text Extractor and Summarizer")

    # File upload section
    uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

    if uploaded_file is not None:
        # Save the uploaded file to a temporary location
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_file.write(uploaded_file.read())
            file_path = temp_file.name  # Get the path to the temp file

        st.info(f"File uploaded successfully. Processing: {uploaded_file.name}") # show file name

        # Extract text from PDF
        text = extract_text_from_pdf(file_path)

        if text.startswith("Error") or text == "No readable text found in the PDF.":
            st.error(text)  # Display error/no text message
        else:
            st.subheader("Extracted Text:")
            st.text(text)

            st.subheader("Summary:")
            # Use a slider for adjusting the summary length
            max_sentences = st.slider("Maximum Summary Sentences", min_value=1, max_value=50, value=10, step=1)
            summary = summarize_text(text, max_sentences=max_sentences)
            st.write(summary)
        # Clean up the temporary file
        import os
        os.remove(file_path)

if __name__ == "__main__":
    main()

