# -*- coding: utf-8 -*-
"""Deploying ML model

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xKk7mhoThzcJLlz0YioWn5wIdC2q3SRM
"""

import streamlit as st
import pickle
import numpy as np
import tensorflow as tf
from tensorflow import keras


model = tf.keras.models.load_model('best_model.h5',compile=False)

from sklearn.preprocessing import StandardScaler
sc=StandardScaler()

def predict_LC(sensubmerge, argonconsumption, shrouddippingdepth, Carbon ,
       Mn , Nb , Va , Cr , Si , liq_Temp ,
       Super_Heat , Casting_Powder , Heat_in_Td , Spray_Plan , HMO ,
       Avg_speed, Avg_heatfluxfix, Avg_heatfluxloose, Avg_heatfluxleft,
       Avg_heatfluxright):
    
    
    
    input=np.array([[sensubmerge, argonconsumption, shrouddippingdepth, Carbon,
       Mn, Nb , Va , Cr , Si , liq_Temp ,
       Super_Heat , Casting_Powder , Heat_in_Td , Spray_Plan , HMO ,
       Avg_speed, Avg_heatfluxfix, Avg_heatfluxloose, Avg_heatfluxleft,
       Avg_heatfluxright]]).astype(np.float64)
    
    input=sc.fit_transform(input)
    prediction =model.predict(input)
    if(prediction>0.5):
        pred=1
    else:
        pred=0
    
    return pred

def main():

    st.title("Longitudinal Crack Prediction")
    html_temp = """
    <div style="background:#025246 ;padding:10px">
    <h2 style="color:white;text-align:center;">LC Prediction ML App </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html = True)
    sensubmerge = st.text_input("Sensubmerge")
    argonconsumption = st.text_input("argonconsumption")
    shrouddippingdepth= st.text_input("shrouddippingdepth")
    Carbon = st.text_input("Carbon")
    Mn = st.text_input("Mn %")
    Nb = st.text_input("Nb %")
    Va = st.text_input("Va %")
    Cr = st.text_input("Cr %")
    Si = st.text_input("Si %")
    liq_Temp = st.text_input("liq_temp")
    Super_Heat = st.text_input("Super Heat")
    Casting_Powder = st.text_input("Casting Powder")
    Heat_in_Td = st.text_input("Heat in Tundish")
    Spray_Plan= st.text_input("Spray Plan")
    HMO = st.text_input("HMO")
    Avg_speed = st.text_input("Average speed")
    Avg_heatfluxfix= st.text_input("Avg_heatfluxfix")
    Avg_heatfluxloose = st.text_input("Avg_heatfluxloose")
    Avg_heatfluxleft = st.text_input("Avg_heatfluxleft")
    Avg_heatfluxright = st.text_input("Avg_heatfluxright")
  
            


    LC_html ="""  
      <div style="background-color:#80ff80; padding:10px >
      <h2 style="color:white;text-align:center;"> LC is present</h2>
      </div>
    """
    NO_LC_html ="""  
      <div style="background-color:#F4D03F; padding:10px >
      <h2 style="color:white;text-align:center;"> No LC</h2>
      </div>
    """
   
    

    if st.button("Predict LC"):
        
        output = predict_LC(sensubmerge, argonconsumption, shrouddippingdepth, Carbon,
       Mn, Nb , Va , Cr , Si , liq_Temp ,
       Super_Heat , Casting_Powder , Heat_in_Td , Spray_Plan , HMO ,
       Avg_speed, Avg_heatfluxfix, Avg_heatfluxloose, Avg_heatfluxleft,
       Avg_heatfluxright)
        st.success('Model Output {}'.format(output))

        if output == 1:
            st.markdown(LC_html,unsafe_allow_html=True)
        elif output == 0:
            st.markdown(NO_LC_html,unsafe_allow_html=True)
      

if __name__=='__main__':
    main()