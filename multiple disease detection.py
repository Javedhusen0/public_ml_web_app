# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 23:32:04 2024

@author: Dell
"""

import pickle
import numpy as np
import streamlit as st
from streamlit_option_menu import option_menu

diabetes_model = pickle.load(open('C:/Users/Dell/OneDrive/Desktop/multiple disease detection/multiple disease/diabetes_dataset_model', 'rb'))
heart_model = pickle.load(open('C:/Users/Dell/OneDrive/Desktop/multiple disease detection/multiple disease/heart_diseases_model', 'rb'))
parkinson_model = pickle.load(open('C:/Users/Dell/OneDrive/Desktop/multiple disease detection/multiple disease/parkinsons_disease_model', 'rb'))

# sidebar for navigate

with st.sidebar : # it help to cut and can return back the ml model
    
    selected = option_menu('Multiple Disease Detection using ML',
                           ['diabetes disease prediction',
                            'heart disease prediction',
                            'parkinsons disease prediction'],
                           icons = ['activity','heart','person'],
                           default_index=1) # default value is 0 , it is change able also
    
    
# Diabetes Prediction system

if(selected == 'diabetes disease prediction'):
    # the title
    st.title("Diabetes disease prediction using ML")   
    
    
    # getting the input data from the user
    # columns for input field
    col1, col2, col3 = st.columns(3) # data shape are converted into the three columns
    
    with col1:
        Pregnancies = st.text_input("Number of Pregnancies")
        
    with col2:
        Glucose = st.text_input("Glucose")
    
    with col3:
        BloodPressure = st.text_input("Blood Pressure value")

    with col1:
        SkinThickness = st.text_input("Skin Thickness value")
    
    with col2:
        Insulin = st.text_input("Insuline level")
        
    with col3:    
        BMI = st.text_input("BMI value")
        
    with col1:    
        DiabetesPedigreeFunction = st.text_input("Diabetes Predigree Function value")
    
    with col2:
        Age = st.text_input("Age of the Person")
    
    
    diab_dignosis = ''
    
    # creating a button for prediction
    
    if st.button('diabetes test result'):
        
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
    
        if(diab_prediction[0]==1):
            diab_dignosis = "The person is diabetes patient"
        else:
            diab_dignosis = "The person is not diabetes patient"
            
    st.success(diab_dignosis)
            
      
            
      
            
   # age	sex	cp	trestbps	chol	fbs	restecg	thalach	exang	oldpeak	slope	ca	thal	
         
if(selected == 'heart disease prediction'):
    # the title
    st.title("Heart disease prediction using ML")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input("Age of the person")
        
    with col2:
        sex = st.text_input("Gender")
        
    with col3:
        cp = st.text_input("Constrictive pericarditis value")
        
    with col1:
        trestbps = st.text_input("Trestbps level")
        
    with col2:
        chol = st.text_input("chol value")
        
    with col3:
        fbs  = st.text_input("fbs value")
        
    with col1:
        restecg = st.text_input("restecg value")
        
    with col2:
        thalach = st.text_input("thalach value")
        
    with col3:
        exang = st.text_input("exang value")
        
    with col1:
        oldpeak = st.text_input("oldpeak value")
    
    with col2:
        slope = st.text_input("slope value")    
    
    with col3:
        ca = st.text_input("Coronary artery value")
        
    with col1:
        thal = st.text_input("thal value")
        
    
    heart_dig = ''

    if st.button('Heart disease test result'):
        heart_dig = heart_model.predict([[age, sex,	cp,	trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
    
        if(heart_dig[0]==1):
            heart_dig = 'person is heart disease patient'
            
        else:
            heart_dig = 'person is not heart patient'
    
    st.success(heart_dig)
    
    
    
    
    
    # name	MDVP:Fo(Hz)	MDVP:Fhi(Hz)	MDVP:Flo(Hz)	MDVP:Jitter(%)	MDVP:Jitter(Abs)	MDVP:RAP	MDVP:PPQ	Jitter:DDP	MDVP:Shimmer	
    #MDVP:Shimmer(dB)	Shimmer:APQ3	Shimmer:APQ5	MDVP:APQ	Shimmer:DDA	NHR	HNR		RPDE	DFA	spread1	spread2	D2	PPE

if(selected == "parkinsons disease prediction"):
    # the title
    st.title("parkinsons disease prediction using Ml")
    
    col1, col2, col3 = st.columns(3)
        
    #with col1:
        #name = st.text_input("Name of the person")
        
    with col2:
        MDVP_fo = st.text_input("MDVP:Fo(Hz) value")
        
    with col3:
        MDVP_fi = st.text_input("MDVP:Fhi(Hz) value")
        
    with col1:
        MDVP_f = st.text_input("MDVP:Flo(Hz) value")
        
    with col2:
        MDVP_j = st.text_input("MDVP:Jitter(%) value")
        
    with  col3:
        MDVP_ja = st.text_input("MDVP:Jitter(Abs) value")
        
    with col1:
        MDVP_R = st.text_input("MDVP:RAP value")
        
    with col2:
        MDVP_P = st.text_input("MDVP:PPQ value")
        
    with col3:
        Jitter_D = st.text_input("Jitter:DDP value")
        
    with col1:
        MDVP_S = st.text_input("MDVP:Shimmer value")
        
    with col2:
        MDVP_Sdb = st.text_input("MDVP:Shimmer(dB) value")
        
    with col3:
        Shimmer_A = st.text_input("Shimmer:APQ3 value")
        
    with col1:
        Shimmer_A5 = st.text_input("Shimmer:APQ5 value")
        
    with col2:
        MDVP_AQ = st.text_input("MDVP:APQ value")
        
    with col3: 
        Shimmer_DD = st.text_input("Shimmer:DDA value")
        
    with col1:
        NHR = st.text_input("NHR value")
        
    with col2:
        HNR = st.text_input("HNR level")
        
    with col3:
        RPDE = st.text_input("RPDE value")
        
    with col1:
        DFA = st.text_input("DFA value")
        
    with col2:
        spread1 = st.text_input("spread1 value(In negative)")
        
    with col3:
        spread2 = st.text_input("spread2 value")
        
    with col1:
        D2 = st.text_input("D2 value")    
        
    with col2:
        PPE = st.text_input("PPE value")
        
        
    parkinson_disease = ''

    
    if st.button("parkinsons test result"):
        
        parkinson_disease = parkinson_model.predict([[	MDVP_fo, MDVP_fi, MDVP_f,MDVP_j, 
                                                      MDVP_ja, MDVP_R, MDVP_P, Jitter_D, MDVP_S,	
        MDVP_Sdb, Shimmer_A, Shimmer_A5, MDVP_AQ,	Shimmer_DD, NHR, HNR, 	RPDE, DFA, spread1,	spread2, D2,PPE]])
        
        if (parkinson_disease[0]==1):
            parkinson_disease = 'Person is parkinson disease patient'
            
        else:
            parkinson_disease = 'Person is not parkinson disease patient'
            
    st.success(parkinson_disease)    
            
        
    