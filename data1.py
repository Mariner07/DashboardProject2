import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

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

<<<<<<< HEAD
st.write('You selected:', country_options)

def simpleGraph(country_options):
=======
def simpleGraph():
>>>>>>> ba28344c51d5a954f2970f83e9447b70a43b6b9e
  fig=plt.figure(figsize=(14,6))
  plt.title("Death toll")
  plt.xticks(rotation=90)
  plt.xlabel("Date", fontsize=8)
  plt.ylabel("Total deaths per million", fontsize=8)
<<<<<<< HEAD
  sns.lineplot(data=data[data['location'].isin(country_options)]['total_deaths'])
=======
  sns.lineplot(data=data['total_deaths'])
>>>>>>> ba28344c51d5a954f2970f83e9447b70a43b6b9e
  return fig


page = st.sidebar.selectbox("Dashboard Options", ("Simple: 1 country", "Home Page"))
if page== "Simple: 1 country":
  if st.checkbox('Show simple graph'):
    

    
    st.subheader('Simple graph')
<<<<<<< HEAD
    st.pyplot(simpleGraph(country_options), use_container_width = True)
=======
    st.pyplot(simpleGraph(), use_container_width = True)
 

    
>>>>>>> ba28344c51d5a954f2970f83e9447b70a43b6b9e
  
  


