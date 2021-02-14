# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 00:55:18 2020

@author: User
"""
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import base64
from io import BytesIO
from PIL import Image
def about_proj_iit():
    st.markdown("# About Project: IIT Seat predictor")
    st.markdown("""JEE Main College Predictor helps you to know college admission chances based on your JEE Main Rank, Home State, Caste, Gender
Choose your specialisation of interest in top institutes like NITs, IIITs and CFTIs
Check results for multiple State counselling like Haryana, Maharashtra, West Bengal, Delhi which accept admission via JEE Main.
The College Predictor lets you know your probable Institution from an extensive list of Colleges across the Nation. It includes premium institutes like NITs, IIITs and CFTIs, many States/ Institutes accept admissions through JEE Main.

Simply Predict your College admission chances:
Based on your Category, Gender
Get to know in which course/ specialisation you have a good chance Get a personalised report
Pdf report with recommended colleges and college counselling process""")
    image = Image.open('Boddu_Venkatesh.jpg')
    st.image(image, width=100)


def getdata():
    df=pd.read_excel("K://5. Projects//iit//2018.xlsx",sheet_name=6)

    if st.sidebar.checkbox("Explore"):
        c=st.selectbox('College',df['Institute'].unique())
        a_p=st.selectbox('Course',df['Academic Program Name'].unique())
        st.table(df[(df['Institute']==c) & (df['Academic Program Name']==a_p)].sort_values(by=['Opening Rank']))


    r=st.sidebar.number_input("Enter rank")
    #g=st.sidebar.selectbox("Gende",('Male','Female','Other'))
    #c=st.sidebar.selectbox("Category",df['Seat Type'].unique())
    #s=st.sidebar.selectbox("State",df['])
    new_df=df[df['Closing Rank']>r].sort_values(by=['Opening Rank'])
    if st.sidebar.checkbox('show all'):
        st.table(new_df)
    if st.sidebar.checkbox("Choose"):
        c=st.sidebar.multiselect('College',df['Institute'].unique())
        a_p=st.sidebar.multiselect('Course',df['Academic Program Name'].unique())
        final=new_df[(new_df['Institute'].isin(c)) & (new_df['Academic Program Name'].isin(a_p))]
        if final.shape[0]>0:
            st.table(final)
        else:
            st.write("Select your prefered college and branch")
    return new_df
def to_excel(df):
    output = BytesIO()
    writer = pd.ExcelWriter(output, engine='xlsxwriter')
    df.to_excel(writer, index = False, sheet_name='Sheet1',float_format="%.2f")
    writer.save()
    processed_data = output.getvalue()
    return processed_data

def get_table_download_link(df):
    """Generates a link allowing the data in a given panda dataframe to be downloaded
    in:  dataframe
    out: href string
    """
    val = to_excel(df)
    b64 = base64.b64encode(val)  # val looks like b'...'
    return f'<a href="data:application/octet-stream;base64,{b64.decode()}" download="Your_File.xlsx">Download Excel file</a>' # decode b'abc' => abc
