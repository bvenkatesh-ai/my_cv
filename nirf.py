# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 21:05:08 2020

@author: User
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
#----------------------------------------------------------------------------#
#    OBE-------------------------------#
#----------------------------------------------------------------------------#
#q=st.sidebar.text_input("Q no")
#co=st.sidebar.text_input("CO no")
#btl=st.sidebar.text_input("btl")
#----------------------------------------------------------------------------#
#   NIRF 2020-------------------------------#
#----------------------------------------------------------------------------#
def about_proj_nirf():
    st.markdown("# About Proj NIRF")
def nirf(cat):
    df=pd.read_excel("C://Users//User//examples//my_cv//nirf2020.xlsx",sheet_name=cat)
    df=df.drop(['Institute ID'],axis=1)
    #st.write(df.head())
    if st.sidebar.checkbox("Top 10 institutions",key='n1'):
        st.table(df.head(10))
    if st.sidebar.checkbox("top 10 in state",key='n2'):
        s=st.sidebar.selectbox("state",df['State'].unique())
        st.table(df[df['State']==s])
    if st.sidebar.checkbox("Choose city",'n3'):
        c=st.sidebar.selectbox("City",df['City'].unique())
        st.table(df[df['City']==c])
    if st.sidebar.checkbox("Compare colleges",'n4'):
        com=st.sidebar.multiselect("Compare colleges",df['Name'].unique())
        st.table(df[df['Name'].isin(com)])
    st_count=df["State"].value_counts()
    if st.sidebar.checkbox('State wise colleges','n5'):
        st.bar_chart(st_count)
    if st.sidebar.checkbox('Score distribution','n6'):
        fig, ax = plt.subplots()
        ax = plt.hist(df['Score'],bins=10)
        st.pyplot(fig)

#st.title("NIRF Analytics 2020")
def get_proj_nirf():
    category=['Overall','University','Engineering','Management','Pharmacy','College','Medical','Law','Architecture','Dental']
    choose_cat=st.sidebar.selectbox('Category',category)
    for c in category:
       if c==choose_cat:
            c2=category.index(c)
            nirf(c2)
