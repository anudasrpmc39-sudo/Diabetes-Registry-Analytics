from utils import load_data
diabetes_type = st.sidebar.selectbox(
    "Diabetes Type",
    ["All"] + sorted(df["Diabetes_Type"].unique())
)

if diabetes_type != "All":
    filtered_df = filtered_df[
        filtered_df["Diabetes_Type"] == diabetes_type
    ]

poor_control = (
    filtered_df["HbA1c_pct"] >= 7
).mean() * 100

reduced_egfr = (
    filtered_df["eGFR"] < 60
).mean() * 100

c1, c2 = st.columns(2)

with c1:
    st.metric(
        "Poor Glycemic Control",
        f"{poor_control:.1f}%"
    )

with c2:
    st.metric(
        "Reduced Kidney Function",
        f"{reduced_egfr:.1f}%"
    )

import plotly.express as px

corr = filtered_df[
    [
        "Age",
        "BMI",
        "HbA1c_pct",
        "FBS_mmol_L",
        "RBS_mmol_L",
        "Creatinine_mg_dL",
        "eGFR"
    ]
].corr(numeric_only=True)

fig = px.imshow(
    corr,
    text_auto=".2f",
    color_continuous_scale="RdBu_r",
    title="Correlation Heatmap"
)

st.plotly_chart(fig, use_container_width=True)

import plotly.express as px

corr = filtered_df[
    [
        "Age",
        "BMI",
        "HbA1c_pct",
        "FBS_mmol_L",
        "RBS_mmol_L",
        "Creatinine_mg_dL",
        "eGFR"
    ]
].corr(numeric_only=True)

fig = px.imshow(
    corr,
    text_auto=".2f",
    color_continuous_scale="RdBu_r",
    title="Correlation Heatmap"
)

st.plotly_chart(fig, use_container_width=True)
