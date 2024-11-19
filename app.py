import streamlit as st
from server import generate_bio  # Import the backend function

# Streamlit UI
st.title("About Me Generator")

# Input fields
name = st.text_input("Name")
profession = st.text_input("Profession")
skills = st.text_area("Skills (comma-separated)")
tone = st.selectbox("Select Tone", ["Casual", "Professional", "Enthusiastic", "Custom"])

# Generate Bio Button
if st.button("Generate Bio"):
    if name and profession and skills and tone:
        with st.spinner("Generating bio..."):
            bio = generate_bio(name, profession, skills, tone)
            st.text_area("Your Generated Bio:", value=bio, height=200)
    else:
        st.warning("Please fill in all fields.")
