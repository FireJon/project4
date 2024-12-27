import streamlit as st
import pandas as pd
import plotly_express as px

car_data = pd.read_csv('vehicles_us.csv')

st.header('Data viewer')
st.dataframe(car_data)

# Below in the hashtags, I was trying to figure out a way to create a checkbox for vehicles that were 4wd.  I might come back to this problem at a future date. 
#four_wheel_drive = st.checkbox('Check for 4WD')
#if not four_wheel_drive:
#    car_data = car_data.groupby('is_4wd').isin('no')

normalize = st.checkbox('Normalize histogram', value=True)
if normalize:
    histnorm = 'percent'
else:
    histnorm = None

st.header('Histograms of Model Year by Cylinder Count')
cylinders_order = [3.0, 4.0, 5.0, 6.0, 8.0, 10.0, 12.0]
st.write(px.histogram(car_data, x='model_year', color='cylinders', histnorm=histnorm, category_orders={'cylinders': cylinders_order}))

st.header('Scatterplots to test correlation between model year and price based on car type.')
st.write(px.scatter(car_data, x='model_year', y='price', color='type'))