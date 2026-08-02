import streamlit as st
import pandas as pd
import plotly.express as px
import joblib
from pathlib import Path
from utils import load_data

st.set_page_config(page_title="Machine Learning", page_icon="🤖", layout="wide")

st.title("🤖 Machine Learning Dashboard")
st.markdown("Predict high-risk diabetes patients using a trained Random Forest model.")

df = load_data()

BASE_DIR = Path(__file__).resolve().parent.parent.parent
MODEL_PATH = BASE_DIR / "models" / "diabetes_random_forest.pkl"
METRICS_PATH = BASE_DIR / "models" / "model_metrics.pkl"

if not MODEL_PATH.exists():
    st.error(f"Model not found: {MODEL_PATH}")
    st.stop()

if not METRICS_PATH.exists():
    st.error(f"Metrics file not found: {METRICS_PATH}")
    st.stop()

model = joblib.load(MODEL_PATH)
metrics = joblib.load(METRICS_PATH)

features = metrics["features"]

st.subheader("📊 Model Information")
a,b,c = st.columns(3)
a.metric("Model","Random Forest")
b.metric("Features",len(features))
c.metric("Patients",f"{len(df):,}")

st.divider()
st.subheader("📈 Model Performance")
k1,k2,k3,k4,k5 = st.columns(5)
k1.metric("Accuracy",f"{metrics['accuracy']:.3f}")
k2.metric("Precision",f"{metrics['precision']:.3f}")
k3.metric("Recall",f"{metrics['recall']:.3f}")
k4.metric("F1 Score",f"{metrics['f1']:.3f}")
k5.metric("ROC-AUC",f"{metrics['auc']:.3f}")

st.divider()
st.subheader("📋 Confusion Matrix")
cm = pd.DataFrame(metrics["confusion_matrix"],
                  index=["Actual Low","Actual High"],
                  columns=["Predicted Low","Predicted High"])
st.plotly_chart(px.imshow(cm,text_auto=True,color_continuous_scale="Blues"),
                use_container_width=True)

st.divider()
st.subheader("🔥 Feature Importance")
imp = pd.DataFrame({"Feature":metrics["features"],
                    "Importance":metrics["feature_importance"]}).sort_values("Importance",ascending=True)
fig = px.bar(imp,x="Importance",y="Feature",orientation="h",text="Importance",color="Importance")
fig.update_traces(texttemplate="%{text:.3f}")
st.plotly_chart(fig,use_container_width=True)

st.divider()
st.subheader("🩺 Predict Patient Risk")
l,r = st.columns(2)
with l:
    age=st.number_input("Age",20,100,55)
    bmi=st.number_input("BMI",15.0,50.0,28.0)
    duration=st.number_input("Duration (Years)",0,40,8)
    fbs=st.number_input("FBS",3.0,25.0,7.2)
    rbs=st.number_input("RBS",4.0,30.0,10.5)
with r:
    hbs2=st.number_input("2HBS",4.0,30.0,9.5)
    hba1c=st.number_input("HbA1c",4.0,15.0,7.1)
    creatinine=st.number_input("Creatinine",0.3,5.0,1.0)
    egfr=st.number_input("eGFR",10,150,90)
    ldl=st.number_input("LDL",30,250,100)

if st.button("Predict Risk", use_container_width=True):
    patient = pd.DataFrame([[age,bmi,duration,fbs,rbs,hbs2,hba1c,creatinine,egfr,ldl]], columns=features)
    pred=model.predict(patient)[0]
    prob=model.predict_proba(patient)[0][1]
    if pred==1:
        st.error("🔴 High Risk Patient")
        st.metric("Prediction Probability",f"{prob:.1%}")
    else:
        st.success("🟢 Low Risk Patient")
        st.metric("Prediction Probability",f"{1-prob:.1%}")

st.divider()
st.subheader("📋 Model Summary")
st.success(f"""Random Forest model\n\nAccuracy: {metrics['accuracy']:.3f}\nPrecision: {metrics['precision']:.3f}\nRecall: {metrics['recall']:.3f}\nF1: {metrics['f1']:.3f}\nROC-AUC: {metrics['auc']:.3f}""")