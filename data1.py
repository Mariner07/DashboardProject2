import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv')

st.title('COVID dashboard Hélène & Maxime & Nurlan')

def simpleGraph():
  
  fig = plt.figure(figsize=(14,6))
  plt.title("Death toll")
  plt.xticks(rotation=90)
  plt.xlabel("Date", fontsize=8)
  plt.ylabel("Total deaths per million", fontsize=8)
  sns.lineplot(data=data['total_deaths'])
  plt.show()
  return fig

page = st.sidebar.selectbox("Dashboard Options", ("Simple: 1 country", "Complicated"))
if page== "Simple: 1 country":
  simpleGraph()
  
  
                           



st.balloons()

