import pandas as pd
import requests
import json

HOST = 'https://api.census.gov/data'
year = '2019'
dataset = 'acs/acs1'
base_url = "/".join([HOST, year, dataset])
predicates = {}
get_vars = ["NAME","B01001_001E", "B01001_002E", "B01001_026E"] #"B01001A_001E", "B01001A_002E", "B01001A_026E", "B01001B_001E", "B01001B_002E", "B01001B_026E", "B01001G_001E", "B01001G_002E", "B01001G_026E"
predicates["get"] = ",".join(get_vars)
predicates["for"] = "public use microdata area:*"
#predicates["for"] = "county:005,047,061,081,085"
predicates["in"] = "state:36"
response = requests.get(base_url, params=predicates)
response.status_code

