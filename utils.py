# utils.py
import streamlit as st
import random
import time

# ---------------------------
# Initialize session state
# ---------------------------
def setup_session_state():
    if "analysis_done" not in st.session_state:
        st.session_state.analysis_done = False
    if "analysis_result" not in st.session_state:
        st.session_state.analysis_result = None
    if "analysis_details" not in st.session_state:
        st.session_state.analysis_details = {}

# ---------------------------
# Analyze text content
# ---------------------------
def analyze_text(text, progress_bar=None):
    """
    Dummy function to simulate AI-generated text detection.
    Replace with a real ML/NLP model later.
    """
    details = {
        "length": len(text),
        "preview": text[:200] + "..." if len(text) > 200 else text
    }

    # Simulate processing with progress bar
    if progress_bar:
        for i in range(100):
            time.sleep(0.01)
            progress_bar.progress(i + 1)

    # Fake score for now
    score = random.uniform(0, 100)
    return score, details

# ---------------------------
# Analyze multimedia content
# ---------------------------
def analyze_content(modality, file_bytes, progress_bar=None, filename=None):
    """
    Dummy function for analyzing image, video, or audio.
    Replace with real ML model integration.
    """
    details = {
        "file_name": filename,
        "size_bytes": len(file_bytes),
        "modality": modality,
    }

    if progress_bar:
        for i in range(100):
            time.sleep(0.01)
            progress_bar.progress(i + 1)

    # Fake score for now
    score = random.uniform(0, 100)
    return score, details
