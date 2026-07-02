import streamlit as st

st.title("Product Review")

# Render native star feedback (returns an integer from 0 to 4, or None)
rating = st.feedback("stars")

if rating is not None:
    # Scale it to a 1-5 scale for better readability
    actual_stars = rating + 1
    st.write(f"You selected: {actual_stars} star(s)!")