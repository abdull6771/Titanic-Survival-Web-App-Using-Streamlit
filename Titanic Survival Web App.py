# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pickle 
import streamlit as st
import pandas as pd
import numpy as np
file= open("C:/Users/USER/Desktop/TitanicPrediction/trained_modek.sav","rb")
loaded_model = pickle.load(file)
#file.close()
html_temp1 = """
 <div style ="background-color:red;padding:5px">
 <h2 style="color:white;text-align:center;">User Input Features</h2>
"""
st.sidebar.markdown(html_temp1,unsafe_allow_html=True)

st.sidebar.write("We need some information from you")
def titanic_prediction(input_data):
     input_array = np.asarray(input_data)
     input_array_reshaped = input_array.reshape(1,-1)
     prediction = loaded_model.predict(input_array_reshaped)
     if (prediction[0]==2): 
        return "The Person has Survived" 
     return "The Person has not Survived"
def user_input_feature():
     html_temp = """
     <div style ="background-color:blue;padding:10px">
     <h2 style="color:white;text-align:center;">Titanic Prediction Machile Learnig App</h2>
    """
     st.markdown(html_temp,unsafe_allow_html=True)
     st.write("**This App predict Weather the Person Embarked in Titanic or Not**")
     Pclass =st.sidebar.text_input("Pclass")
     Sex=st.sidebar.text_input("Sex")
     Age = st.sidebar.text_input("Age")
     SibSp= st.sidebar.text_input("SibSp")
     Parch=st.sidebar.text_input("Parch")
     Fare=st.sidebar.text_input("Fare")
     Embarked=st.sidebar.text_input("Emabarked")
     data = {
         "Pclass":Pclass,
         "Sex":Sex,
         "Age":Age,
         "SibSp":SibSp,
         "Parch":Parch,
         "Fare":Fare,
         "Embarked":Embarked,
         }
     features = pd.DataFrame(data,index=[0])
     return features
df = user_input_feature()
 
st.subheader("User Input Parameters")
 
st.write(df)

st.subheader("Prediction") 
person = ""

if st.button("Predict"):
        person = titanic_prediction(df)
st.success(person)
 
if st.sidebar.button("About"):
    st.sidebar.text("Created By Abdullahi Ahmad Babura")
    st.sidebar.text("Reach me through +2348067718392")
    st.sidebar.text("@abdull6771/twiter")
    st.sidebar.text("Abdull6771@Github")
if __name__ == "user_input_feature":
    user_input_feature()
    
 
    
 
    
 
    
 
    
 
    
 
    
 
    
 
    
 
    