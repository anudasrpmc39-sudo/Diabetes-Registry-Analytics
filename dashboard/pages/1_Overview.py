import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from utils import load_data

import streamlit as st
import plotly.express as px
import pandas as pd

from utils import load_data
from dashboard.utils import load_data

# ============================================================
# Page Configuration
# ============================================================

st.set_page_config(
    page_title="Overview",
    page_icon="📊",
    layout="wide"
)

# ============================================================
# Load Dataset
# ============================================================

df = load_data()

# ============================================================
# Page Title
# ============================================================

st.title("📊 Diabetes Registry Overview")

st.markdown("""
Welcome to the **Overview Dashboard**.

This page provides a high-level summary of the diabetes registry,
including patient demographics, disease burden, and key clinical indicators.

Use the **filters on the left** to interactively explore the data.
""")

# ============================================================
# Sidebar Filters
# ============================================================

st.sidebar.header("🔍 Dashboard Filters")

district = st.sidebar.selectbox(
    "District",
    ["All"] + sorted(df["District"].unique())
)

sex = st.sidebar.selectbox(
    "Sex",
    ["All"] + sorted(df["Sex"].unique())
)

if district != "All":
    df = df[df["District"] == district]

if sex != "All":
    df = df[df["Sex"] == sex]

df = df.copy()

# ============================================================
# KPI Cards
# ============================================================

st.subheader("📌 Key Performance Indicators")

risk = (df["High_Risk"] == "Yes").mean() * 100

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "👥 Patients",
        f"{len(df):,}"
    )

with col2:
    st.metric(
        "🎂 Average Age",
        f"{df['Age'].mean():.1f} Years"
    )

with col3:
    st.metric(
        "🩸 Average HbA1c",
        f"{df['HbA1c_pct'].mean():.2f}%"
    )

with col4:
    st.metric(
        "⚠️ High Risk",
        f"{risk:.1f}%"
    )

st.divider()

# ============================================================
# Age Distribution
# ============================================================

age_chart = px.histogram(
    df,
    x="Age",
    nbins=20,
    marginal="box",
    title="Age Distribution"
)

# ============================================================
# Sex Distribution
# ============================================================

sex_count = (
    df["Sex"]
    .value_counts()
    .rename_axis("Sex")
    .reset_index(name="Patients")
)

sex_chart = px.bar(
    sex_count,
    x="Sex",
    y="Patients",
    text="Patients",
    color="Sex",
    title="Sex Distribution"
)

sex_chart.update_traces(textposition="outside")

# ============================================================
# Row 1
# ============================================================

col1, col2 = st.columns(2)

with col1:
    st.plotly_chart(
        age_chart,
        use_container_width=True
    )

with col2:
    st.plotly_chart(
        sex_chart,
        use_container_width=True
    )

st.divider()

# ============================================================
# District Distribution
# ============================================================

district_count = (
    df["District"]
    .value_counts()
    .rename_axis("District")
    .reset_index(name="Patients")
)

district_chart = px.bar(
    district_count,
    x="District",
    y="Patients",
    text="Patients",
    color="Patients",
    title="Patients by District"
)

district_chart.update_traces(textposition="outside")

# ============================================================
# Diabetes Type
# ============================================================

type_count = (
    df["Diabetes_Type"]
    .value_counts()
    .rename_axis("Diabetes Type")
    .reset_index(name="Patients")
)

type_chart = px.pie(
    type_count,
    names="Diabetes Type",
    values="Patients",
    hole=0.45,
    title="Diabetes Type Distribution"
)

# ============================================================
# Row 2
# ============================================================

col3, col4 = st.columns(2)

with col3:
    st.plotly_chart(
        district_chart,
        use_container_width=True
    )

with col4:
    st.plotly_chart(
        type_chart,
        use_container_width=True
    )

# ============================================================
# Registry Summary
# ============================================================

st.divider()

st.subheader("📋 Registry Summary")

summary = pd.DataFrame({

    "Indicator": [
        "Total Patients",
        "Average Age",
        "Average HbA1c",
        "Average BMI",
        "High-Risk Patients"
    ],

    "Value": [
        f"{len(df):,}",
        f"{df['Age'].mean():.1f} Years",
        f"{df['HbA1c_pct'].mean():.2f} %",
        f"{df['BMI'].mean():.1f} kg/m²",
        f"{risk:.1f}%"
    ]
})

st.table(summary)

# ============================================================
# Key Findings
# ============================================================

st.divider()

st.subheader("📖 Key Findings")

st.markdown(f"""
- 👥 **Total Patients:** **{len(df):,}**
- 🎂 **Average Age:** **{df['Age'].mean():.1f} years**
- 🩸 **Average HbA1c:** **{df['HbA1c_pct'].mean():.2f}%**
- ⚖️ **Average BMI:** **{df['BMI'].mean():.1f} kg/m²**
- ⚠️ **High-Risk Patients:** **{risk:.1f}%**

**Note:** All charts and summary statistics update automatically based on the selected filters.
""")