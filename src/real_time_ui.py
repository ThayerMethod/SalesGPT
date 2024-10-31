import streamlit as st

def display_response(transcription, response):
    st.write("### Real-Time Transcription")
    st.write(transcription)
    
    st.write("### Suggested Response")
    st.write(response)
