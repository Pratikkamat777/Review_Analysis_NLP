
import streamlit as st
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Download required data
nltk.download("vader_lexicon", quiet=True)

# Create analyzer
sia = SentimentIntensityAnalyzer()

# Streamlit web app
st.title("Review Analysis Using NLTK")
st.write("Enter a review to analyze its sentiment.")

# Input review
review = st.text_area("Enter your review:")

# Analyze button
if st.button("Analyze Review"):
    if review.strip():
        score = sia.polarity_scores(review)

        st.write("### Sentiment Scores")
        st.write(score)

        if score["compound"] >= 0.05:
            st.success("Positive Review 😊")
        elif score["compound"] <= -0.05:
            st.error("Negative Review 😞")
        else:
            st.info("Neutral Review 😐")
    else:
        st.warning("Please enter a review.")
