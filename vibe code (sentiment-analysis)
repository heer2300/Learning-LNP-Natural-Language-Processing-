import streamlit as st
from transformers import pipeline

classifier = pipeline("sentiment-analysis")

st.title("Sentiment Analyzer")

text = st.text_area("Enter your review:")

if st.button("Analyze"):
    if text:
        result = classifier(text)[0]

        st.write("Sentiment:", result["label"])
        st.write("Confidence:", f"{result['score'] * 100:.2f}%")
    else:
        st.warning("Please enter some text.")
