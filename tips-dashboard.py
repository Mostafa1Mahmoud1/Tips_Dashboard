# Import Libraries
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

st.set_page_config(page_title = 'Tips Dashboard',
                   page_icon='📈',
                   layout='wide',
                   initial_sidebar_state='expanded')
# Loading data 

df = pd.read_csv('tip.csv')

# Sidebar

st.sidebar.header("Tips Dashboard")

st.sidebar.image("tips.jpg")

st.sidebar.write("This dashboard is using Tips dataset from Kaggle")

st.sidebar.write("---")

st.sidebar.write("Filter your data: ")
cat_filter = st.sidebar.selectbox("Categorical Filtering",[None,'sex','smoker','day','time'])
num_filter = st.sidebar.selectbox("Numerical Filtering",[None,'tip','total_bill'])
row_filter = st.sidebar.selectbox("Row Filtering",[None,'sex','smoker','day','time'])
col_filter = st.sidebar.selectbox("Column Filtering",[None,'sex','smoker','day','time'])




st.sidebar.write("----")
st.sidebar.markdown("Made with ❤️ by [Mostafa Mahmoud](+201280824603)")


# Body

# row a

a1 , a2 , a3 , a4 = st.columns(4)
a1.metric("Max. Total Bill",df['total_bill'].max())
a2.metric("Max. Tip",df['tip'].max())
a3.metric("Min. Total Bill",df['total_bill'].min())
a4.metric("Min. Tip",df['tip'].min())
st.write("---")

# # row b

# st.subheader("Total Bill vs. Tips")

st.markdown("<h3 style='text-align: center;'>Total Bill vs. Tips</h3>", unsafe_allow_html=True)


fig = px.scatter(data_frame=df,
                 x = 'total_bill',
                 y = 'tip',
                 color = cat_filter,
                 size = num_filter,
                 facet_col=col_filter,
                 facet_row=row_filter)

st.plotly_chart(fig,use_container_width=True)

st.write("---")


# row c

c1 , c2 , c3 = st.columns([4,3,3])

with c1:
    st.markdown("<h5> Sex vs. Total Bills</h5>", unsafe_allow_html=True)
   
    fig = px.bar(data_frame=df,
                 x='sex',
                 y = 'total_bill',
                 color=cat_filter)
    st.plotly_chart(fig,use_container_width=True)


with c2:
    st.markdown("<h5> Smoker / Non-smoker vs. Tips</h5>", unsafe_allow_html=True)
    fig = px.pie(data_frame=df,
                 names ='smoker',
                 values = 'tip',
                 color=cat_filter)
    st.plotly_chart(fig,use_container_width=True)


with c3:
    st.markdown("<h5> Days vs. Tips</h5>", unsafe_allow_html=True)
    fig = px.pie(data_frame=df,
                 names ='day',
                 values = 'tip',
                 color=cat_filter,
                 hole=0.3)

    st.plotly_chart(fig,use_container_width=True)
