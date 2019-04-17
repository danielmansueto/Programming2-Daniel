# SCRAPING LAB 
# (20pts)
# Below is a link to a 10-day weather forecast at weather.com
# Use requests and BeautifulSoup to scrape data from the weather table.
# Print a synopsis of the weather for the next 10 days by grabbing each of the following:
# Day, date, description, high and low temp, chance of rain, and wind. (2pts each)
# Print the weather for each of the next 10 days to the user in readable sentences.
# You can customize the text as you like, but it should be readable as a sentence without errors. (10pts)
# You will need to target specific classes or other attributes to pull some parts of the data.
# Sample sentence:  
# Wednesday, April 4 will be Partly Cloudy/Windy with a High of 37 degrees and a low of 25, humidity at 52%.  There is 0% chance of rain with winds out of the WNW at 22 mph.

# Note: Although it is possible to pull a description of the weather which includes much of this data, that is not the intent.
# However, if you can do it and add the additional info, that works for me.

from bs4 import BeautifulSoup
import requests
url = "https://weather.com/weather/tenday/l/USIL0225:1:US"

page = requests.get(url)  # get request from to that url
print(page)
soup = BeautifulSoup(page.text, "html.parser")

day = soup.findAll(class_="date-time")
date = soup.findAll(class_="day-detail clearfix")
description = soup.findAll(class_="description")
temp = soup.findAll(class_="temp")
rain = soup.findAll(class_="precip")
wind = soup.findAll(class_="wind")

for i in range(10):
    print()
    print(day[i].text, str(date[i].text) + ',', "the weather will be", description[i + 1].text, "with a high of", temp[i + 1].text[:3], "and a low of", str(temp[i].text[-3:]) + ',', "there looks to be a", rain[i + 1].text, "chance of rain with wind looking like", wind[i + 1].text)