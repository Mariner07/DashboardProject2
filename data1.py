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

def simpleGraph(country_options):
  fig=plt.figure(figsize=(14,6))
  plt.title("Death toll")
  plt.xticks(rotation=90)
  plt.xlabel("Date", fontsize=8)
  plt.ylabel("Total deaths per million", fontsize=8)
  sns.lineplot(data=data[data['location'].isin(country_options)]['total_deaths'])
  return fig

def plot_cases():
    fig=px.line(data, x=data['date'], y=data['new_cases'], title = "Cases")
    return fig

def plot_deaths():
    fig=px.line(data, x=data['date'], y=data['new_deaths'], title = "Death toll")
    return fig

page = st.sidebar.selectbox("Dashboard Options", ("Simple: 1 country", "Home Page"))
if page== "Simple: 1 country":
  if st.checkbox('Show simple graph'):
    st.subheader('Simple graph')
    st.pyplot(simpleGraph(country_options), use_container_width = True)
    
#Date slider
show_timerange = st.sidebar.checkbox("Show date range")
if show_timerange == True:
    # Comute timerange
    min_ts = min(df[DATE_COLUMN]).to_pydatetime()
    max_ts = max(df[DATE_COLUMN]).to_pydatetime()
    day_date = pd.to_datetime(st.sidebar.slider("Date choice", min_value=min_ts, max_value=max_ts, value=max_ts))
    st.write(f"Data for {day_date.date()}")
    df = data[(data['date'] == day_date)]

#Selectbox for data
select_event = st.sidebar.selectbox('Data options', ('Cases', 'Deaths'))
if select_event == 'Cases':
    st.plotly_chart(plot_cases(), use_container_width=True)

if select_event == 'Deaths':
    st.plotly_chart(plot_deaths(), use_container_width=True)
