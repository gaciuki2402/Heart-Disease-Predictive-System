import pathlib
import pandas as pd
import numpy as np
import streamlit as st
import pickle as pk

# Correct the path for the pickled model file
model = pk.load(open(r"C:\Users\ADMIN\grace\HDM\Heart_Disease_Model.pkl", 'rb'))

# Correct the path for the CSV file
data = pd.read_csv(r"C:\Users\ADMIN\grace\HDM\Heart_Disease_Data.csv")

st.header('Heart Disease Predictor')

gender = st.selectbox("Choose Gender", data['Gender'].unique())
if gender == 'Male ':
    gen = 1
else:
    gen = 0

age = st.selectbox("Enter Age")