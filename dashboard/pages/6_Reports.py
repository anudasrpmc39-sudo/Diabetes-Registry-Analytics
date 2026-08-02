import streamlit as st

# ======================================================
# Page Configuration
# ======================================================

st.set_page_config(
    page_title="About",
    page_icon="ℹ️",
    layout="wide"
)

# ======================================================
# Header
# ======================================================

st.title("ℹ️ About the Project")

st.markdown("""
# Diabetes Registry Analytics Platform

A comprehensive Health Informatics dashboard developed to demonstrate
clinical data analytics, disease surveillance, and machine learning
using a synthetic diabetes registry dataset.
""")

st.divider()

# ======================================================
# Project Overview
# ======================================================

st.header("🎯 Project Objectives")

st.markdown("""
This project demonstrates how Health Informatics can support:

- Clinical decision support
- Disease surveillance
- Population health management
- Laboratory analytics
- Diabetes complication monitoring
- Predictive analytics using Machine Learning
""")

# ======================================================
# Dashboard Modules
# ======================================================

st.header("📊 Dashboard Modules")

modules = [
    "📊 Overview Dashboard",
    "👥 Demographics Dashboard",
    "🩸 Laboratory Dashboard",
    "⚠️ Complications Dashboard",
    "🤖 Machine Learning Dashboard",
    "📄 Reports & Export"
]

for module in modules:
    st.write(f"✅ {module}")

st.divider()

# ======================================================
# Dataset
# ======================================================

st.header("🗂 Dataset")

col1, col2 = st.columns(2)

with col1:
    st.metric("Patients", "700,000")
    st.metric("Clinical Variables", "24+")

with col2:
    st.metric("Disease", "Diabetes")
    st.metric("Data Type", "Synthetic Registry")

st.markdown("""
The dataset includes:

- Demographic information
- Laboratory investigations
- Diabetes type
- Complications
- Kidney function
- Cardiovascular outcomes
- High-risk classification
""")

st.divider()

# ======================================================
# Machine Learning
# ======================================================

st.header("🤖 Machine Learning")

st.markdown("""
The platform includes a Random Forest classifier that predicts
whether a patient is at high risk based on clinical variables.

Model outputs include:

- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC
- Confusion Matrix
- Feature Importance
- Individual Patient Prediction
""")

st.divider()

# ======================================================
# Technology Stack
# ======================================================

st.header("🛠 Technology Stack")

tech1, tech2 = st.columns(2)

with tech1:
    st.markdown("""
**Programming**

- Python
- Pandas
- NumPy
- Scikit-learn
""")

with tech2:
    st.markdown("""
**Visualization & Deployment**

- Streamlit
- Plotly
- Joblib
- Git & GitHub
""")

st.divider()

# ======================================================
# Developer
# ======================================================

st.header("👨‍⚕️ Developer")

st.markdown("""
**Dr. Anupom Das**

- MBBS
- Field Epidemiology Training Program (FETP)
- MSc Health Informatics
- Karolinska Institutet
""")

st.info("""
This project was developed as a professional portfolio project to
demonstrate expertise in Health Informatics, Clinical Data Analytics,
Machine Learning, and Interactive Dashboard Development.
""")

st.divider()

# ======================================================
# Footer
# ======================================================

st.caption("© 2026 Diabetes Registry Analytics Platform | Developed using Python & Streamlit")