import streamlit as st
import pandas as pd
import plotly.express as px
from utils import load_data
# -------------------------------------------------------
# Page Configuration
# -------------------------------------------------------

st.set_page_config(
    page_title="Demographics",
    page_icon="👥",
    layout="wide"
)

# -------------------------------------------------------
# Load Data
# -------------------------------------------------------

df = load_data()

st.title("👥 Demographic Analysis")

st.markdown(
"""
Explore the demographic characteristics of diabetes patients using interactive filters and visualizations.
"""
)

# -------------------------------------------------------
# Sidebar Filters
# -------------------------------------------------------

st.sidebar.header("🔍 Filters")

district = st.sidebar.selectbox(
    "District",
    ["All"] + sorted(df["District"].unique())
)

sex = st.sidebar.selectbox(
    "Sex",
    ["All"] + sorted(df["Sex"].unique())
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

filtered_df = filtered_df.copy()

# -------------------------------------------------------
# KPI Cards
# -------------------------------------------------------

st.subheader("📌 Key Indicators")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "👥 Patients",
        f"{len(filtered_df):,}"
    )

with col2:
    st.metric(
        "🎂 Average Age",
        f"{filtered_df['Age'].mean():.1f} Years"
    )

with col3:
    st.metric(
        "⚖️ Average BMI",
        f"{filtered_df['BMI'].mean():.1f}"
    )

with col4:
    st.metric(
        "❤️ Life Expectancy",
        f"{filtered_df['Life_Expectancy_Years'].mean():.1f} Years"
    )

st.divider()

# -------------------------------------------------------
# Age Distribution
# -------------------------------------------------------

age_fig = px.histogram(
    filtered_df,
    x="Age",
    nbins=20,
    title="Age Distribution"
)

# -------------------------------------------------------
# Sex Distribution
# -------------------------------------------------------

sex_counts = (
    filtered_df["Sex"]
    .value_counts()
    .rename_axis("Sex")
    .reset_index(name="Patients")
)

sex_fig = px.bar(
    sex_counts,
    x="Sex",
    y="Patients",
    color="Sex",
    text="Patients",
    title="Sex Distribution"
)

sex_fig.update_traces(textposition="outside")

# -------------------------------------------------------
# Row 1
# -------------------------------------------------------

col1, col2 = st.columns(2)

with col1:
    st.plotly_chart(age_fig, use_container_width=True)

with col2:
    st.plotly_chart(sex_fig, use_container_width=True)

# -------------------------------------------------------
# District Distribution
# -------------------------------------------------------

district_counts = (
    filtered_df["District"]
    .value_counts()
    .rename_axis("District")
    .reset_index(name="Patients")
)

district_fig = px.bar(
    district_counts,
    x="District",
    y="Patients",
    color="Patients",
    text="Patients",
    title="Patients by District"
)

district_fig.update_traces(textposition="outside")

# -------------------------------------------------------
# BMI Distribution
# -------------------------------------------------------

bmi_fig = px.histogram(
    filtered_df,
    x="BMI",
    nbins=25,
    marginal="box",
    title="BMI Distribution"
)

# -------------------------------------------------------
# Row 2
# -------------------------------------------------------

col3, col4 = st.columns(2)

with col3:
    st.plotly_chart(district_fig, use_container_width=True)

with col4:
    st.plotly_chart(bmi_fig, use_container_width=True)

# -------------------------------------------------------
# Age Group Analysis
# -------------------------------------------------------

bins = [0,18,30,45,60,75,100]

labels = [
    "<18",
    "18-30",
    "31-45",
    "46-60",
    "61-75",
    ">75"
]

filtered_df["Age_Group"] = pd.cut(
    filtered_df["Age"],
    bins=bins,
    labels=labels,
    include_lowest=True
)

age_group = (
    filtered_df["Age_Group"]
    .value_counts()
    .sort_index()
    .rename_axis("Age Group")
    .reset_index(name="Patients")
)

age_group_fig = px.bar(
    age_group,
    x="Age Group",
    y="Patients",
    color="Patients",
    text="Patients",
    title="Patients by Age Group"
)

age_group_fig.update_traces(textposition="outside")

st.plotly_chart(
    age_group_fig,
    use_container_width=True
)

# -------------------------------------------------------
# Summary
# -------------------------------------------------------

st.divider()

st.subheader("📋 Demographic Summary")

male = (filtered_df["Sex"] == "Male").sum()
female = (filtered_df["Sex"] == "Female").sum()

st.write(f"""
### Key Findings

- **Total Patients:** {len(filtered_df):,}
- **Average Age:** {filtered_df['Age'].mean():.1f} years
- **Average BMI:** {filtered_df['BMI'].mean():.1f} kg/m²
- **Average Life Expectancy:** {filtered_df['Life_Expectancy_Years'].mean():.1f} years
- **Male Patients:** {male:,}
- **Female Patients:** {female:,}

These summaries automatically update when the sidebar filters are changed.
""")