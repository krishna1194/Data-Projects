#!/usr/bin/env python
# coding: utf-8

# # Overall Problem Statement
# The problem asks to use Open Weather Map's API (Application Programming Interface) to query forecasted temperature data. You will write your results to a CSV file.
# 
# ## Introduction
# 
# 1. Use the OpenWeatherMap API to query future-day forecasts containing expected daily weather conditions for 16 different cities.
# 2. Parse the Python variables returned by the API to extract the the minimum and maximum forecast temperature temperatureMini and temperatureMaxi in Celsius for each of the upcoming four (4) days.
# 3. Compute the average minimum and maximum forecast temperatures Minavg and Maxavg for the upcoming four (4) days.
# 
# ## Cities to Query
# 
# 1. Bengaluru, India
# 2. Glasgow, Scotland
# 3. Gumi, South Korea
# 4. Lagos, Nigeria
# 5. Nanaimo, Canada
# 6. Niskayuna, New York
# 7. Nizhny Novgorod, Russia
# 8. Olongapo, Philippines
# 9. Peshawar, Pakistan
# 10. Peterhead, Scotland
# 11. Quito, Ecuador
# 12. Simmern, Germany
# 13. Tainan, Taiwan
# 14. Tbilisi, Georgia
# 15. Vinh Long, Vietnam
# 16. Xi'an, China
# 
# 
# ## Locating "Tomorrow"
# 
# Your 4-day forecast starts at midnight tomorrow, and includes tomorrow plus the three days following tomorrow. For example, if the date when you run your program is August 23, you would provide a 4-day forecast for August 24 through August 28.
# 
# 
# 
# # Solution
# 
# The solution is completely automated. The user can change the number of days or add a city to get extra details. Except that everything is automated.
# API is used to pull the data from Open Weather Map website.
# 
# There are 3 "for loops":
# 
# 1. Looping the cities
# 2. Looping for the days we are interested in
# 3. Looping to get the min and max for each day
# 
# 
# 
# The notebook is fully commented and it can be used directly - Create an account in Open Weather Map and get the api key and run this program.

# In[1]:


# Import functions
import pprint
import requests
import pandas as pd
import json
import calendar
from datetime import datetime, timezone
from dateutil.relativedelta import relativedelta
from decimal import *

# Intermediate and Final empty dataframes
df_ = pd.DataFrame()
df_main = pd.DataFrame()

# Look ahead period
days = 4

# Getting UTC's today date
today = datetime.now(timezone.utc).date()

# Interested cities
city = ["Bengaluru,India",                                                                                   
        "Glasgow,Scotland",
        "Gumi,South Korea",
        "Lagos,Nigeria",
        "Nanaimo,Canada",
        "Niskayuna,New York",
        "Nizhny Novgorod,Russia",
        "Olongapo,Phillipines",
        "Peshawar,Pakistan",
        "Peterhead,Scotland",
        "Quito,Ecuador",
        "Simmern,Germany",
        "Tainan,Taiwan",
        "Tbilisi,Georgia",
        "Vinh Long,Vietnam",
        "Xi'an,China"]

# Main Program
for city_i in city:                                                                                                 # Loop data for all cities
    api_key = '********************************'                                                                    # Enter your API
    URL_ = 'http://api.openweathermap.org/data/2.5/forecast?'                                                       # URL for program
    URL = URL_ + 'q='+city_i+'&appid=' + api_key + '&units=metric'                                                  # units:in Celcius[official doc]
    response = requests.get( URL )
    df_['City'] = [city_i]                                                                                          # Add city name to intermediate df
    if response.status_code == 200:                                                                                 # Success
        data = response.json()
        printer = pprint.PrettyPrinter(width=80, compact=True)
        for i in range (1,days+1):                                                                                  # Loop data for all days
            next_day = today + relativedelta(days=i)                                                                # Get date for future
            next_day = next_day.strftime("%Y-%m-%d")                                                                # Convert to string; used below
            min_day_list = []                                                                                       # Empty list: 
            max_day_list = []                                                                                         # Store min & max temp
            for k in range(len(data["list"])):                                                                      # Get the min and max for full day
                if data["list"][k]["dt_txt"].split()[0] == next_day:                                                # Loop for interested dates
                    max_day_list.append(data["list"][k]["main"]["temp_max"])                                        # Append min and max for each day: 
                    min_day_list.append(data["list"][k]["main"]["temp_min"])                                          # to empty list
            df_['Min' + ' ' + str(i)] = min(min_day_list)                                                           # For a given day in df:
            df_['Max' + ' ' + str(i)] = max(max_day_list)                                                            # get max,min from lists & store
        df_['Min Avg'] = float('%.2f'%(df_[df_.columns[pd.Series(df_.columns).str.contains('^Min [0-9]+')]].mean(axis=1)))  # For a given day in df: 
        df_['Max Avg'] = float('%.2f'%(df_[df_.columns[pd.Series(df_.columns).str.contains('^Max [0-9]+')]].mean(axis=1)))  # get min,max Average & round
    else:                                                                                                           # Failure
        print( 'Error:', response.status_code )
    df_main = pd.concat([df_main,df_])                                                                              # Concat intermediate with final

# df_main.to_csv('output.csv', index=False)                                                                              # Write the o/p to csv
df_main

