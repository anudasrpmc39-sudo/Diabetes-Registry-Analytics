import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from utils import load_data

import streamlit as st
import pandas as pd
import plotly.express as px

from utils import load_data

# ======================================================
# Page Configuration
# ======================================================

st.set_page_config(
    page_title="Complications",
    page_icon="⚠️",
    layout="wide"
)

# ======================================================
# Load Data
# ======================================================

df = load_data()

# ======================================================
# Page Title
# ======================================================

st.title("⚠️ Diabetes Complications Dashboard")

st.markdown("""
This dashboard provides an overview of diabetes-related complications
among registered patients.

Use the filters on the left to explore complication patterns across
different patient groups.
""")

# ======================================================
# Sidebar Filters
# ======================================================

st.sidebar.header("🔍 Dashboard Filters")

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
# KPI Cards
# ======================================================

st.subheader("📌 Complication Summary")

retinopathy = (
    filtered_df["Retinopathy"].notna()
).mean() * 100

nephropathy = (
    filtered_df["Nephropathy"].notna()
).mean() * 100

neuropathy = (
    filtered_df["Neuropathy"].notna()
).mean() * 100

cad = (
    filtered_df["CAD"] == "Yes"
).mean() * 100

stroke = (
    filtered_df["Stroke"] == "Yes"
).mean() * 100

c1, c2, c3, c4, c5 = st.columns(5)

c1.metric("👁 Retinopathy", f"{retinopathy:.1f}%")
c2.metric("🩺 Nephropathy", f"{nephropathy:.1f}%")
c3.metric("🦶 Neuropathy", f"{neuropathy:.1f}%")
c4.metric("❤️ CAD", f"{cad:.1f}%")
c5.metric("🧠 Stroke", f"{stroke:.1f}%")

