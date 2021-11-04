#!/usr/bin/env python
# coding: utf-8

# In[1]:


## IMPORT LIBRARY ##
import pandas as pd
import requests
import json


# In[2]:


## REQUESTS LIBRARY ## can alter requests to fit unique analysis needs ##
# Constructing API:
# https://api.census.gov/data/2019/acs/acs1/profile?get=NAME,DP05_0023E&for=county:005,047,061,081,085&in=state:36
HOST = 'https://api.census.gov/data'
year = '2019'
dataset = 'acs/acs1'
tabletype = 'profile'
base_url = "/".join([HOST, year, dataset, tabletype])
predicates = {}
get_vars = ["NAME","DP05_0001E", "DP05_0037E", "DP05_0038E", "DP05_0024E"] 
predicates["get"] = ",".join(get_vars)
predicates["for"] = "public use microdata area:*"
# alternate geography filter==> predicates["for"] = "county:005,047,061,081,085"
predicates["in"] = "state:36"
response = requests.get(base_url, params=predicates)

# Checking status of API response to the request ## 200 means request has been processed successfully
response.status_code


# In[3]:


# Converting API response to a json
data = response.json()


# In[7]:


# Translating the json file into a data frame with pandas
import pandas as pd
df = pd.DataFrame(data[1:], columns=data[0])
df.columns = ["Neighborhood", "Total Pop", "White alone", "Black Alone", "65 years and older", "State code", "County code"]

# PUMA filter to only display NYC neighborhoods
df[df['Neighborhood'].str.contains("NYC")]


# In[8]:


# Converting into integers
df['Total Pop'] = df['Total Pop'].astype(int)
df['White alone'] = df['White alone'].astype(int)
df['Black Alone'] = df['Black Alone'].astype(int)
df['65 years and older'] = df['65 years and older'].astype(int)

# Formulating the ratio of 65 year and older
df['% 65 years and older'] = (df['65 years and older']/df['Total Pop'])*100


# In[9]:


# Display PUMA filtered NYC neighborhoods with new variable
df[df['Neighborhood'].str.contains("NYC")]


# In[10]:


# Filter for a specific borough
df[df['Neighborhood'].str.contains("Manhattan")]


# In[11]:


# Filter for a specific neighborhood
df[df['Neighborhood'].str.contains("West Harlem")]


# In[ ]:




