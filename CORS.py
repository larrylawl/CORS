#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 10:47:36 2018

@author: larrylaw
"""

import pandas as pd

data_links = pd.read_excel("/Users/larrylaw/Documents/CS/CORS ML/Data Links.xlsx")
for links in data_links.iloc[:,0]:
    print(links)

x = pd.read_html("http://www.cors.nus.edu.sg/Archive/201718_Sem2/successbid_1A_20172018s2.html")
z = pd.read_html()
y = x[1].fillna(method='ffill')
