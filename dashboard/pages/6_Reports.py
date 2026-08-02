import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from utils import load_data

import streamlit as st
import pandas as pd

# ======================================================
# Page Configuration
# ======================================================

st.set_page_config(
    page_title="Reports & Export",
    page_icon="📄",
    layout="wide"
)

# ======================================================
# Load Data
# ======================================================

df = load_data()

# ======================================================
# Title
# ======================================================

st.title("📄 Reports & Export")

st.markdown("""
Generate reports and download filtered diabetes registry data.
""")

# ======================================================
# Sidebar Filters
# ======================================================

st.sidebar.header("🔍 Filters")

district = st.sidebar.selectbox(
    "District",
    ["All"] + sorted(df["District"].unique())
)

sex = st.sidebar.selectbox(
    "Sex",
    ["All"] + sorted(df["Sex"].unique())
)

diabetes_type = st.sidebar.selectbox(
    "Diabetes Type",
    ["All"] + sorted(df["Diabetes_Type"].unique())
)

filtered_df = df.copy()

if district != "All":
    filtered_df = filtered_df[
        filtered_df["District"] == district
    ]

if sex != "All":
    filtered_df = filtered_df[
        filtered_df["Sex"] == sex
    ]

if diabetes_type != "All":
    filtered_df = filtered_df[
        filtered_df["Diabetes_Type"] == diabetes_type
    ]

# ======================================================
# Registry Summary
# ======================================================

st.subheader("📊 Registry Summary")

c1, c2, c3, c4 = st.columns(4)

c1.metric("Patients", f"{len(filtered_df):,}")
c2.metric("Average Age", f"{filtered_df['Age'].mean():.1f}")
c3.metric("Average HbA1c", f"{filtered_df['HbA1c_pct'].mean():.2f}%")
c4.metric("Average BMI", f"{filtered_df['BMI'].mean():.1f}")

st.divider()

# ======================================================
# Data Preview
# ======================================================

st.subheader("📋 Filtered Dataset")

st.dataframe(
    filtered_df,
    use_container_width=True
)

# ======================================================
# Download CSV
# ======================================================

csv = filtered_df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="⬇ Download Filtered CSV",
    data=csv,
    file_name="filtered_diabetes_registry.csv",
    mime="text/csv"
)

# ======================================================
# Summary Statistics
# ======================================================

summary = filtered_df.describe(include="all")

summary_csv = summary.to_csv().encode("utf-8")

st.download_button(
    label="⬇ Download Summary Statistics",
    data=summary_csv,
    file_name="summary_statistics.csv",
    mime="text/csv"
)