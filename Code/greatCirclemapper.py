# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 11:52:56 2020

@author: 45950
"""

import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import csv
import re
import pandas as pd

url = 'https://www.greatcirclemapper.net/en/airlines.html'
result = requests.get(url)
soup = BeautifulSoup(result.text, "html.parser")
craft_links=[]
for data in soup.find_all(class_="container"):
    for link in data.find_all('a'):
        craft_links.append('https://www.greatcirclemapper.net/'+link.get('href'))

craft_links_1=[]
for url in craft_links:
    result = requests.get(url)
    soup_link = BeautifulSoup(result.text, "html.parser")
    for data in soup_link.find_all(class_="table-responsive"):
        for link in data.find_all('a'):
            craft_links_1.append('https://www.greatcirclemapper.net/'+link.get('href'))
 
dfObj6 = pd.DataFrame()
df_output6 = pd.DataFrame()
for items in range(0,len(craft_links_1)):
    try:
        url_link = craft_links_1[items]
        result_1 = requests.get(url_link)
        #print(result_1)
        soup_1 = BeautifulSoup(result_1.content, "html.parser")
        text_= soup_1.find(class_='col-md-6')
        #print(text_)
        temp = text_.get_text()
        break
    except:
        print("Oops Error occured!")
temp_1 = temp.splitlines()
regex = re.compile('\t\n')
temp_1 = regex.split(temp)
for element in range(0,len(temp_1)):
    temp_1[element] = temp_1[element].strip()
dfObj6 = pd.DataFrame(temp_1)

dfObj6.columns = ['Team_Name']
dfObj6['Team_Name'].str.split(expand=False)
dfObj6['Team_Name'] = dfObj6['Team_Name'].str.replace("\t","")
dfObj6['Team_Name'] = dfObj6['Team_Name'].str.replace("\n",",")
new =  dfObj6["Team_Name"].str.split(",,", n = 1, expand = True) 
dfObj6["Attributes"]= new[0]
dfObj6["Values"]= new[1] 
dfObj6.drop(columns =["Team_Name"], inplace = True)
#print(dfObj)
#dfObj = dfObj.append(temp_1)
df_output6= df_output6.append(dfObj6["Values"])
#df_output.reset_index(drop=True)
#new_header = df_output.iloc[0] #grab the first row for the header
#df_output = df_output[1:] #take the data less the header row
#df_output.columns = new_header #set the header row as the df header
#df_output.reset_index(drop=True)
    
    
    
     
    
    
    
    
    
    
    
    
            
    




