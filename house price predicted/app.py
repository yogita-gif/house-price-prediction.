import streamlit as st
import joblib
import numpy as np

model = joblib.load("model.pkl")

st.title("House price prediction App")

st.divider()

st.write("This app is use machine learning for predicting house price with given features of the house")

st.divider()

bedrooms = st.number_input("number of bedrooms",min_value=0,value=0)
bathrooms = st.number_input("number of bathrooms",min_value=0,value=0)
living_area = st.number_input("living area",min_value=0,value=2000)
condition = st.number_input("condition",min_value=0,value=3)
schools = st.number_input("number of schools nearby",min_value=0,value=0)
st.divider()

x = [[bedrooms,bathrooms,living_area,condition,schools]]
predictbutton = st.button("predict")
if predictbutton:
  st.balloons()
  x_array = np.array(x)
  prediction = model.predict(x_array)[0]
  st.write(f"price prediction is {prediction:,.2f} ")
else:
  st.write("click the predict button")




#order of x x Index(['number of bedrooms', 'number of bathrooms', # 'living area','condition of the house', 
# 'Number of schools nearby'],dtype='object')

