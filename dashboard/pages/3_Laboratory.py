# 3_Laboratory.py
# Complete Laboratory Dashboard
# Replace your existing dashboard/pages/3_Laboratory.py with this file.

import streamlit as st
import pandas as pd
import plotly.express as px
from utils import load_data

st.set_page_config(page_title="Laboratory Analysis", page_icon="🩸", layout="wide")
df=load_data()

st.title("🩸 Laboratory Analysis Dashboard")
st.markdown("Use the filters on the left to explore laboratory results.")

st.sidebar.header("🔍 Laboratory Filters")
district=st.sidebar.selectbox("District",["All"]+sorted(df["District"].unique()))
sex=st.sidebar.selectbox("Sex",["All"]+sorted(df["Sex"].unique()))
diabetes_type=st.sidebar.selectbox("Diabetes Type",["All"]+sorted(df["Diabetes_Type"].unique()))

filtered_df=df.copy()
if district!="All":
    filtered_df=filtered_df[filtered_df["District"]==district]
if sex!="All":
    filtered_df=filtered_df[filtered_df["Sex"]==sex]
if diabetes_type!="All":
    filtered_df=filtered_df[filtered_df["Diabetes_Type"]==diabetes_type]

poor_control=(filtered_df["HbA1c_pct"]>=7).mean()*100
reduced_egfr=(filtered_df["eGFR"]<60).mean()*100
high_ldl=(filtered_df["LDL_mg_dL"]>100).mean()*100
high_creatinine=(filtered_df["Creatinine_mg_dL"]>1.2).mean()*100

st.subheader("📌 Laboratory Summary")
c1,c2,c3,c4=st.columns(4)
c1.metric("Average HbA1c",f"{filtered_df['HbA1c_pct'].mean():.2f}%")
c2.metric("Average FBS",f"{filtered_df['FBS_mmol_L'].mean():.2f}")
c3.metric("Average RBS",f"{filtered_df['RBS_mmol_L'].mean():.2f}")
c4.metric("Average eGFR",f"{filtered_df['eGFR'].mean():.1f}")

c5,c6,c7,c8=st.columns(4)
c5.metric("Poor Glycemic Control",f"{poor_control:.1f}%")
c6.metric("Reduced Kidney Function",f"{reduced_egfr:.1f}%")
c7.metric("High LDL",f"{high_ldl:.1f}%")
c8.metric("High Creatinine",f"{high_creatinine:.1f}%")

st.divider()
st.subheader("🩸 Blood Glucose Analysis")
a,b=st.columns(2)
with a:
    st.plotly_chart(px.histogram(filtered_df,x="HbA1c_pct",nbins=25,title="HbA1c Distribution"),use_container_width=True)
with b:
    st.plotly_chart(px.histogram(filtered_df,x="FBS_mmol_L",nbins=25,title="FBS Distribution"),use_container_width=True)

c,d=st.columns(2)
with c:
    st.plotly_chart(px.histogram(filtered_df,x="RBS_mmol_L",nbins=25,title="RBS Distribution"),use_container_width=True)
with d:
    st.plotly_chart(px.histogram(filtered_df,x="2HBS_mmol_L",nbins=25,title="2HBS Distribution"),use_container_width=True)

st.divider()
st.subheader("🩺 Kidney Function")
e,f=st.columns(2)
with e:
    st.plotly_chart(px.histogram(filtered_df,x="Creatinine_mg_dL",nbins=25,title="Creatinine"),use_container_width=True)
with f:
    st.plotly_chart(px.histogram(filtered_df,x="eGFR",nbins=25,title="eGFR"),use_container_width=True)

st.divider()
st.subheader("📦 Clinical Boxplots")
x1,x2,x3=st.columns(3)
with x1:
    st.plotly_chart(px.box(filtered_df,y="HbA1c_pct",color="Sex"),use_container_width=True)
with x2:
    st.plotly_chart(px.box(filtered_df,y="Creatinine_mg_dL",color="Sex"),use_container_width=True)
with x3:
    st.plotly_chart(px.box(filtered_df,y="eGFR",color="Sex"),use_container_width=True)

st.divider()
st.subheader("🔥 Correlation Heatmap")
corr=filtered_df[["Age","BMI","Duration_Years","HbA1c_pct","FBS_mmol_L","RBS_mmol_L","2HBS_mmol_L","Creatinine_mg_dL","eGFR","LDL_mg_dL"]].corr(numeric_only=True)
st.plotly_chart(px.imshow(corr,text_auto=".2f",color_continuous_scale="RdBu_r"),use_container_width=True)

st.divider()
st.subheader("📋 Clinical Interpretation")
st.info(f"""Average HbA1c: {filtered_df['HbA1c_pct'].mean():.2f}%

Average eGFR: {filtered_df['eGFR'].mean():.2f}

Poor Glycemic Control: {poor_control:.1f}%
Reduced Kidney Function: {reduced_egfr:.1f}%""")