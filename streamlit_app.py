import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Ferry Pulse AI",
    page_icon="⛴️",
    layout="wide"
)

st.title("⛴️ Ferry Pulse AI")
st.subheader("Short-Term Ferry Ticket Demand Forecasting")

st.write(
    "A machine learning-based system for forecasting short-term "
    "ferry ticket demand and supporting predictive decisions."
)

st.header("Dataset")

uploaded_file = st.file_uploader(
    "Upload ferry ticket demand dataset",
    type=["csv"]
)

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.success("Dataset uploaded successfully!")

    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    st.subheader("Dataset Information")
    st.write(f"Number of rows: {df.shape[0]}")
    st.write(f"Number of columns: {df.shape[1]}")

    st.subheader("Dataset Statistics")
    st.dataframe(df.describe())

else:
    st.info("Please upload a CSV dataset to begin.")
