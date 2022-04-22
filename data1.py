import streamlit as st
import pandas as pd
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

data_load_state= st.text("Data is in the oven")
data = load_data()
data_load_state.text("Data is cooked")

#Page configuration
st.title('COVID dashboard HMN & co. ☠️')

#Multiselection tool
not_country_list=['Africa', 'Asia', 'Europe', 'European Union', 'International', 'North America', 'Oceania', 'South America', 'Upper middle income']
data_with_valid_countries= data[~data['location'].isin(not_country_list)]

country_options = st.multiselect(
     'Which countries do you want do display ?',
     data_with_valid_countries['location'].unique(),
     ['France'])

def filtered_countries(selected_countries_list):
    data_filtered= data[data['location'].isin(selected_countries_list)]
    return data_filtered

data_filtered=filtered_countries(country_options)

#Date slider
min_ts = min(data[DATE_COLUMN]).to_pydatetime()
max_ts = max(data[DATE_COLUMN]).to_pydatetime()
select_date = st.sidebar.slider("Date range", value=[min_ts, max_ts])
data_selected = data_filtered[(data_filtered['date'] > select_date[0]) & (data_filtered['date'] <= select_date[1])]

#Plotting
def plot(select_figure):
    fig=px.line(data_selected, x=data_selected['date'], y=data_selected[select_figure], color='location')
    fig.update_layout(margin={"r": 0, "t": 50, "l": 0, "b": 0})
    return fig

#Selectbox for data
select_data = st.sidebar.selectbox('Data options', ('Cases 😷', 'Deaths ⚰️', 'Vaccines'))

#Selectbox for figure format
select_figure = st.sidebar.selectbox('Figure format', ("Raw number", "Cumulated number", "7 day rolling average"))

if select_data == 'Cases 😷' and select_figure == 'Raw number':
    st.plotly_chart(plot(select_figure='new_cases_per_million').update_layout(title='Raw Number of Covid 19 Cases', xaxis_title='Date', yaxis_title='Raw Number of Cases (per million)'), use_container_width=True)
    
if select_data == 'Cases 😷' and select_figure == 'Cumulated number':
    st.plotly_chart(plot(select_figure='total_cases_per_million').update_layout(title='Cumulated Number of Covid 19 Cases', xaxis_title='Date', yaxis_title='Cumulated Number of Cases (per million)'), use_container_width=True)
    
if select_data == 'Cases 😷' and select_figure == '7 day rolling average':
    st.plotly_chart(plot(select_figure='new_cases_smoothed_per_million').update_layout(title='7 Days Rolling Average of Covid 19 Cases', xaxis_title='Date', yaxis_title='7 Days Rolling Average (per million)'), use_container_width=True)
    
if select_data == 'Deaths ⚰️' and select_figure == 'Raw number':
    st.plotly_chart(plot(select_figure='new_deaths_per_million').update_layout(title='Raw Number of Covid 19 Deaths', xaxis_title='Date', yaxis_title='Raw Number of Deaths (per million)'), use_container_width=True)
    
if select_data == 'Deaths ⚰️' and select_figure == 'Cumulated number':
    st.plotly_chart(plot(select_figure='total_deaths_per_million').update_layout(title='Cumulated Number of Covid 19 Deaths', xaxis_title='Date', yaxis_title='Cumulated Number of Deaths (per million)'), use_container_width=True)
    
if select_data == 'Deaths ⚰️' and select_figure == '7 day rolling average':
    st.plotly_chart(plot(select_figure='new_deaths_smoothed_per_million').update_layout(title='7 Days Rolling Average of Covid 19 Deaths', xaxis_title='Date', yaxis_title='7 Days Rolling Average of Deaths (per million)'), use_container_width=True)

if select_data == 'Vaccines' and select_figure == 'Raw number':
    st.plotly_chart(plot(select_figure='new_vaccinations_smoothed').update_layout(title='Raw Number of Vaccinated', xaxis_title='Date', yaxis_title='Raw Number of Vaccinated'), use_container_width=True)
    
if select_data == 'Vaccines' and select_figure == 'Cumulated number':
    st.plotly_chart(plot(select_figure='total_vaccinations_per_hundred').update_layout(title='Cumulated Number of Vaccinated', xaxis_title='Date', yaxis_title='Cumulated Number of Vaccinated (per hundred)'), use_container_width=True)
    
if select_data == 'Vaccines' and select_figure == '7 day rolling average':
    st.plotly_chart(plot(select_figure='new_vaccinations_smoothed_per_million').update_layout(title='7 Days Rolling Average of Vaccinated', xaxis_title='Date', yaxis_title='7 Days Rolling Average of Vaccinated (per million)'), use_container_width=True)

