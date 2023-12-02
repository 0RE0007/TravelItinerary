import streamlit as st
import requests
import os

def fetch_data_from_api(input_data):
    api_key = os.getenv("LLAMASTUDIO_API_KEY")
    url = 'https://llamastudio.dev/api/clp3teiua000dl608iajbg8sx'
    data = {'input': input_data}
    response = requests.post(url, json=data)
    return response.text

def main():
    st.title("LLAMA Studio API Integration")

    # Get user input
    user_input = st.text_input("Enter a location:", "London")

    # Make API request when user clicks the button
    if st.button("Fetch Data"):
        result = fetch_data_from_api(user_input)

        # Display the API response
        st.subheader("API Response:")
        st.text(result)

if _name_ == "_main_":
    main()