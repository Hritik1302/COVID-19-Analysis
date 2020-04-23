#!/usr/bin/env python
# coding: utf-8

# # COVID-19 Scientific Analysis

# ### What is Covid-19 ?

# Coronavirus disease 2019 (COVID-19) is an infectious disease caused by severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2).
# The disease was first identified in December 2019 in Wuhan, the capital of China's Hubei province, and has since spread globally, resulting in the ongoing 2019–20 coronavirus pandemic.
# The first confirmed case of what was then an unknown coronavirus was traced back to November 2019 in Hubei province.Common symptoms include fever, cough, and shortness of breath.
# Other symptoms may include fatigue, muscle pain, diarrhoea, sore throat, loss of smell, and abdominal pain.The time from exposure to onset of symptoms is typically around five days but may range from two to fourteen days.
# While the majority of cases result in mild symptoms, some progress to viral pneumonia and multi-organ failure.
# As of 23 April 2020, more than 2.62 million cases have been reported across 185 countries and territories,resulting in more than 183,000 deaths.More than 784,000 people have recovered.
# 
# <p><a href="https://commons.wikimedia.org/wiki/File:Symptoms_of_coronavirus_disease_2019_3.0.svg#/media/File:Symptoms_of_coronavirus_disease_2019_3.0.svg"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b4/Symptoms_of_coronavirus_disease_2019_3.0.svg/1200px-Symptoms_of_coronavirus_disease_2019_3.0.svg.png" alt="Symptoms of coronavirus disease 2019 3.0.svg"></a>

# ### Covid-19 Symptoms

# COVID-19 affects different people in different ways. Most infected people will develop mild to moderate symptoms.
# 
# Common symptoms:
# 
# * **Fever**
# * **Tiredness**
# * **Dry Cough**
# * **Aches and Pains**
# * **Nasal Congestion**
# * **Runny Nose**
# * **Sore Throat**
# * **Diarrhoea**
# 
# On average it takes 5–6 days from when someone is infected with the virus for symptoms to show, however it can take up to 14 days.
# People with mild symptoms who are otherwise healthy should self-isolate. Seek medical attention if you have a fever, a cough, and difficulty breathing.

# ### Covid-19 Preventions

# <center><img class="lqwrY" src="data:image/gif;base64,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" alt="" data-atf="1"></center>
# 
# <h1><center>STAY HOME.SAVE LIVES.</center></h1>
# <h4><center>STAY home</center></h4>
# <h4><center>KEEP a safe distance</center></h4>
# <h4><center>WASH hands often</center></h4>
# <h4><center>COVER your cough</center></h4>
# <h4><center>SICK? Call the helpline</center></h4>

# In[1]:


#Importing Libraries and Modules
from __future__ import print_function
from ipywidgets import interact, interactive, fixed, interact_manual
from IPython.core.display import display, HTML

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import folium
import plotly.graph_objects as go
import seaborn as sns
import ipywidgets as widgets


# # Importing Raw Data

# In[2]:


#Collecting Data
death_df = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv')
confirmed_df = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')
recovered_df = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv')
country_df = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/web-data/data/cases_country.csv')


# # Death Cases

# In[3]:


death_df.head()


# # Confirmed Cases

# In[4]:


confirmed_df.head()


# # Recovered Cases

# In[5]:


recovered_df.head()


# # Cases According To The Countries

# In[6]:


country_df.head()


# In[7]:


#Manipulating Data
country_df.columns = map(str.lower, country_df.columns)
confirmed_df.columns = map(str.lower, confirmed_df.columns)
death_df.columns = map(str.lower, death_df.columns)
recovered_df.columns = map(str.lower, recovered_df.columns)


# In[8]:


confirmed_df = confirmed_df.rename(columns={'province/state': 'state', 'country/region': 'country'})
recovered_df = recovered_df.rename(columns={'province/state': 'state', 'country/region': 'country'})
death_df = death_df.rename(columns={'province/state': 'state', 'country/region': 'country'})
country_df = country_df.rename(columns={'country_region': 'country'})


# In[9]:


sorted_country_df = country_df.sort_values("confirmed",ascending=False).head(20)


# # Countries with Highest Rates

# In[16]:


def highlight_col(x):
    a = 'background-color:#abbaab'
    b = 'background-color:#e52d27'
    c = 'background-color:#667db6'
    d = 'background-color:#52c234'
    e = 'background-color:#11998e'
    temp_df = pd.DataFrame('',index=x.index,columns=x.columns)
    temp_df.iloc[:,0]=a
    temp_df.iloc[:,4]=c
    temp_df.iloc[:,5]=b
    temp_df.iloc[:,6]=d
    temp_df.iloc[:,7]=e
    return temp_df

sorted_country_df.style.apply(highlight_col ,axis=None)


# In[17]:


fig = px.scatter(sorted_country_df.head(25),x="country" ,y="confirmed" ,size="confirmed" ,color="country" ,hover_name="country" ,size_max=70)


# # Graphical Format

# In[18]:


fig.show()


# In[19]:


def plot_cases_for_country(country):
    labels = ['confirmed', 'deaths']
    colors = ['#667db6', '#e52d27']
    mode_size = [6,8]
    line_size = [4,5]

    df_list = [confirmed_df, death_df]

    fig = go.Figure()

    for i, df in enumerate(df_list):
        if country == 'World' or country == 'world':
            x_data = np.array(list(df.iloc[:, 5:].columns))
            y_data = np.sum(np.asarray(df.iloc[:, 5:]), axis=0)
        else:
            x_data = np.array(list(df.iloc[:, 5:].columns))
            y_data = np.sum(np.asarray(df[df['country']==country].iloc[:, 5:]),axis=0)
        
        fig.add_trace(go.Scatter(x=x_data, y=y_data, mode="lines+markers",name=labels[i],
                             line=dict(color=colors[i],width=line_size[i]),
                             connectgaps = True ,text='Total'+str(labels[i]) + ": "+ str(y_data[-1])
                                        ))
    
        fig.show()


# # Enter Country to View the Stats

# In[20]:


interact(plot_cases_for_country, country="World");


# # World Map

# In[21]:


world_map = folium.Map(location=[11,0], tiles="cartodbpositron", zoom_start=2, max_zoom=5, min_zoom=2)

for i in range(len(confirmed_df)):
    folium.Circle(
    location=[confirmed_df.iloc[i]['lat'], confirmed_df.iloc[i]['long']],
    fill = True,
    radius = (int((np.log(confirmed_df.iloc[i,-1]+1.001))) + 0.7)*50000,
    fill_color= 'blue',
    color = 'red',
    tooltip = "<div style='margin: 0; background-color: #2193b0; color: #200122;'>"+
                    "<h4 style='text-align:center;font-weight: bold'>"+confirmed_df.iloc[i]['country'] + "</h4>"
                    "<hr style='margin:10px;color: white;'>"+
                    "<ul style='color: white;;list-style-type:circle;align-item:left;padding-left:20px;padding-right:20px'>"+
                        "<li>Confirmed: "+str(confirmed_df.iloc[i,-1])+"</li>"+
                        "<li>Deaths:   "+str(death_df.iloc[i,-1])+"</li>"+
                        "<li>Death Rate: "+ str(np.round(death_df.iloc[i,-1]/(confirmed_df.iloc[i,-1]+1.00001)*100,2))+ "</li>"+
                    "</ul></div>",
    ).add_to(world_map)
    
    
world_map


# # Top 10 Countries with Affected Cases

# In[31]:


px.bar(
    sorted_country_df.head(10),
    x = "country",
    y = "deaths",
    title= "Affected Cases",
    color_discrete_sequence=["#fc466b"], 
    height=750,
    width=1000
)


# ## Top 10 Countries with Recovered Cases

# In[30]:


px.bar(
    sorted_country_df.head(10),
    x = "country",
    y = "recovered",
    title= "Recovered Cases",
    color_discrete_sequence=["#56ab2f"], 
    height=750,
    width=1000
)


# ## Top 10 Countries with Confirmed Cases

# In[27]:


px.bar(
    sorted_country_df.head(10),
    x = "country",
    y = "confirmed",
    title= "Confirmed Cases",
    color_discrete_sequence=["#8e2de2"], 
    height=750,
    width=1000
)


# ## Resources
# - https://en.wikipedia.org/wiki/2019%E2%80%9320_coronavirus_pandemic
# 
# - https://www.who.int/emergencies/diseases/novel-coronavirus-2019
# 
# - https://www.worldometers.info/coronavirus/
# 
# - https://github.com/CSSEGISandData/COVID-19

# In[ ]:




