import streamlit as st
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as pe

df = pd.read_excel('June_Report.xlsx')

st.title('Finacial Analysis freamework')
st.header('Payment table')
st.write(df)


st.header('Simple descripitve')
st.write(df.describe())

st.header('Unit chart')
st.line_chart(df.set_index('OrderDate')['Units'])

st.header('Total chart')
st.area_chart(df['Total'])

st.header('Region chart')
st.pie_chart(df.set_index('Region')['Units'])