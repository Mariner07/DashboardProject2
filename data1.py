import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

#Loading data
DATE_COLUMN = 'date'

@st.cache
def load_data():
    data = pd.read_csv('https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv')
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

data_load_state= st.text("Data is in oven")
data = load_data()
data_load_state.text("Data is cooked")

#Page configuration
st.set_page_config(layout="wide")
st.title('COVID dashboard HMN & co.')

#Multiselection tool
country_options = st.multiselect(
     'Which countries do you want do display ?',
     data['location'].unique(),
     ['France'])

def filtered_countries(selected_countries_list):
    data_filtered= data[data['location'].isin(selected_countries_list)]
    return data_filtered

data_filtered=filtered_countries(country_options)

#Plotting
def plot(select_figure):
    fig=px.line(data_filtered, x=data_filtered['date'], y=data_filtered[select_figure], color='location')
    return fig
    
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

#Selectbox for figure format
select_figure = st.sidebar.selectbox('Figure format', ("Number", "Cumulated number", "7 day rolling average"))

if select_data == 'Cases' and select_figure == 'Number':
    st.plotly_chart(plot(select_figure='new_cases_per_million'), use_container_width=True)
    
if select_data == 'Cases' and select_figure == 'Cumulated number':
    st.plotly_chart(plot(select_figure='total_cases_per_million'), use_container_width=True)
    
if select_data == 'Cases' and select_figure == '7 day rolling average':
    st.plotly_chart(plot(select_figure='new_cases_smoothed_per_million'), use_container_width=True)
    
if select_data == 'Deaths' and select_figure == 'Number':
    st.plotly_chart(plot(select_figure='new_deaths_per_million'), use_container_width=True)
    
if select_data == 'Deaths' and select_figure == 'Cumulated number':
    st.plotly_chart(plot(select_figure='total_deaths_per_million'), use_container_width=True)
    
if select_data == 'Deaths' and select_figure == '7 day rolling average':
    st.plotly_chart(plot(select_figure='new_deaths_smoothed_per_million'), use_container_width=True)
    
