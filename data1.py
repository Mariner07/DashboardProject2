import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

DATE_COLUMN = 'date'

@st.cache
def load_data():
    data = pd.read_csv('https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv')
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

data_load_state= st.text("Data is in oven")
data = load_data()
data_load_state.text("Data is cooked")


st.title('COVID dashboard Hélène & Maxime & Nurlan')

country_options = st.multiselect(
     'Which countries do you want do display ?',
     data['location'].unique(),
     ['France'])

st.write('You selected:', country_options)

def filtered_countries(selected_countries_list):
    data_filtered= data[data['location'].isin(selected_countries_list)]
    return data_filtered

data_filtered=filtered_countries(country_options)

def plot_cases(figure_format, title):
    fig=px.line(data_filtered, x=data_filtered['date'], y=data_filtered[select_figure], title = title)
    return fig

def plot_deaths():
    fig=px.line(data_filtered, x=data_filtered['date'], y=data_filtered[select_figure], title = title)

    return fig


page = st.sidebar.selectbox("Dashboard Options", ("Simple: 1 country", "Home Page"))

if page== "Simple: 1 country":
  if st.checkbox('Show simple graph'):
    st.subheader('Simple graph')
    st.pyplot(simpleGraph(country_options), use_container_width = True)
    
#Date slider
show_timerange = st.sidebar.checkbox("Show date range")
if show_timerange == True:
    min_ts = min(data[DATE_COLUMN]).to_pydatetime()
    max_ts = max(data[DATE_COLUMN]).to_pydatetime()
    day_date = pd.to_datetime(st.sidebar.slider("Date choice", min_value=min_ts, max_value=max_ts, value=max_ts))
    st.write(f"Data for {day_date.date()}")
    df = data[(data['date'] == day_date)]

#Selectbox for data
select_data = st.sidebar.selectbox('Data options', ('Cases', 'Deaths'))
if select_data == 'Cases':
    st.plotly_chart(plot_cases(), use_container_width=True)

if select_data == 'Deaths':
    st.plotly_chart(plot_deaths(), use_container_width=True)
    
#Selectbox for figure format
#select_figure = st.sidebar.selectbox('Figure format', ("Number", "Cumulated number", "7-day rolling average"))
#if select_figure == 'Number':
#    st.plotly_chart(plot_cases(), use_container_width=True)

#if select_figure == 'Cumulater number':
#    st.plotly_chart(plot_deaths(), use_container_width=True)

#if select_figure == '7-day rolling average':
#    st.plotly_chart(plot(), use_container_width=True)
