import streamlit as st
from transformers import pipeline

# Load the summarization pipeline
summarizer = pipeline("summarization")

# Streamlit app title
st.title("Basic Text Summarizer App")

# Input text box
st.header("Enter Text to Summarize")
user_input = st.text_area("Paste your text here", height=300)

# Summarize button
if st.button("Summarize"):
    if user_input.strip():
        # Summarize the text
        with st.spinner("Summarizing..."):
            summary = summarizer(user_input, max_length=130, min_length=30, do_sample=False)
            st.subheader("Summary")
            st.write(summary[0]['summary_text'])
    else:
        st.error("Please enter some text to summarize.")
