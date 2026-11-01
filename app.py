import streamlit as st

# Configure the webpage
st.set_page_config(
    page_title="RepoMentor",
    page_icon="📂",
    layout="wide"
)

# Main heading
st.title("📂 RepoMentor")

# Subtitle
st.subheader("AI-Powered GitHub Repository Assistant")

# Introduction
st.write(
    "Understand, explore and analyze GitHub repositories "
    "with the help of Artificial Intelligence."
)

# GitHub URL input
repo_url = st.text_input(
    "Enter GitHub Repository URL",
    placeholder="https://github.com/username/repository"
)

# Analyze button
if st.button("Analyze Repository", type="primary"):

    if repo_url.strip():

        st.success("GitHub URL received successfully!")

        st.write("Repository URL:", repo_url)

    else:

        st.warning("Please enter a GitHub repository URL.")
        