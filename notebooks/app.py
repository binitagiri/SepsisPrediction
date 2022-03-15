#!/usr/bin/env python
# coding: utf-8

# 

# In[ ]:


import numpy as np
import pickle
import pandas as pd
#from flasgger import Swagger
import streamlit as st 

from PIL import Image


# In[ ]:


pickle_in = open("classifier.pkl","rb")
classifier=pickle.load(pickle_in)


# In[ ]:


def predict_sepsis(df):
  prediction=classifier.predict(df)
  print(prediction)
  return prediction


# In[ ]:


def main():
    st.title("Early Sepsis Predictor")
    html_temp = """
    <div style="http://localhost:8888/notebooks/app.ipynb#background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Early Sepsis Predictor App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    
    HR = st.number_input("HR")
    O2Sat = st.number_input("O2Sat")
    Temp = st.number_input("Temp")
    SBP = st.number_input("SBP")
    MAP = st.number_input("MAP")
    DBP = st.number_input("DBP")
    
    Resp = st.number_input("Resp")
    EtCO2 = st.number_input("EtCO2")
    BaseExcess = st.number_input("BaseExcess")
    HCO3 = st.number_input("HCO3")
    FiO2 = st.number_input("FiO2")
    pH = st.number_input("pH")
    PaCO2 = st.number_input("PaCO2")
    SaO2 = st.number_input("SaO2")
    
    AST = st.number_input("AST")
    BUN = st.number_input("BUN")
    Alkalinephos = st.number_input("Alkalinephos")
    Calcium = st.number_input("Calcium")
    Chloride = st.number_input("Chloride")
    Creatinine = st.number_input("Creatinine")
    
    Bilirubin_direct = st.number_input("Bilirubin_direct")
    Glucose = st.number_input("Glucose")
    Lactate = st.number_input("Lactate")
    Magnesium = st.number_input("Magnesium")
    Phosphate = st.number_input("Phosphate")
    Potassium = st.number_input("Potassium")
    
    Bilirubin_total = st.number_input("Bilirubin_total")
    TroponinI = st.number_input("TroponinI")
    Hct = st.number_input("Hct")
    Hgb = st.number_input("Hgb")
    PTT = st.number_input("PTT")
    WBC = st.number_input("WBC")
    
    Fibrinogen = st.number_input("Fibrinogen")
    Platelets = st.number_input("Platelets")
    Age = st.number_input("Age")
    Gender = st.number_input("Gender")
    ICULOS = st.number_input("ICULOS")
    
    input_data = [{'HR': HR,'O2Sat': O2Sat,'Temp':Temp,'SBP':SBP,
       'MAP':MAP, 'DBP':DBP, 'Resp':Resp, 'EtCO2':EtCO2, 'BaseExcess':BaseExcess, 'HCO3':HCO3, 'FiO2':FiO2, 'pH':pH,
       'PaCO2':PaCO2, 'SaO2':SaO2, 'AST':AST, 'BUN':BUN, 'Alkalinephos':Alkalinephos, 'Calcium':Calcium, 'Chloride':Chloride,
       'Creatinine':Creatinine, 'Bilirubin_direct':Bilirubin_direct, 'Glucose':Glucose, 'Lactate':Lactate, 'Magnesium':Magnesium,
       'Phosphate':Phosphate, 'Potassium':Potassium, 'Bilirubin_total':Bilirubin_total, 'TroponinI':TroponinI, 'Hct':Hct, 'Hgb':Hgb,
       'PTT':PTT, 'WBC':WBC, 'Fibrinogen':Fibrinogen, 'Platelets':Platelets, 'Age':Age, 'Gender':Gender,'ICULOS':ICULOS}]
    df = pd.DataFrame(input_data)
    result=""
    if st.button("Predict"):
        result=predict_sepsis(df)
    st.success('The output is {}'.format(result))


# In[ ]:


if __name__=='__main__':
    main()

