import streamlit as st
import pandas as pd
import plotly.express as px
from bs4 import BeautifulSoup
import requests


def main(df):
    st.header('NZX Main Board')
    st.data_editor(df)

def volume(df):
    st.header('Line Chart Volumes Traded by Company')
    st.plotly_chart(fig)

def price(df):
    st.header('Histogram Groupning Price')
    st.plotly_chart(fig3)

def capital(df):
    st.header('Capitalisation By Company')
    st.plotly_chart(fig2)

def value(df):
    st.header('Value of Trades')
    st.plotly_chart(fig4)

url='https://www.nzx.com/markets/NZSX'
data=requests.get(url).text
soup=BeautifulSoup(data,'html.parser')

tables=soup.find_all('table')
market_table=pd.read_html(url)
df=market_table[1]




st.set_page_config(layout='wide')
st.title('NZX Main Board')
st.logo('nzx-logo-test.svg',link="https://www.nzx.com/markets/NZSX")
st.write('This app is a test  to show data from a live website and is not interpreting or offering advice on information from NZX')

st.sidebar.title('Market Performance')

options=st.sidebar.radio('Pages', options=['Main Board','Value','Price','Volume','Capitalisation'])

fig=px.line(df,x='Code',y='Volume',markers=True)

fig2=px.bar(df,x='Code',y='Capitalisation',color='Capitalisation')

fig3=px.histogram(df,x='Price',nbins=15)

fig4=px.scatter(df, x='Code',y='Value',color='Code')


if options=='Main Board':
    main(df)
if options=='Volume':
    volume(df)
if options=='Price':
    price(df)
if options=='Capitalisation':
    capital(df)
if options=='Value':
    value(df)
