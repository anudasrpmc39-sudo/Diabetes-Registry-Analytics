from pathlib import Path
import pandas as pd
import streamlit as st


@st.cache_data
def load_data():
    """
    Load the diabetes registry dataset.
    """

    # Project root directory
    project_root = Path(__file__).resolve().parent.parent

    # Path to the CSV file
    data_file = project_root / "data" / "synthetic_diabetes_registry_700000.csv"

    # Read dataset
    df = pd.read_csv(data_file)

    return df