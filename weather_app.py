import requests
import json
from datetime import datetime 
import pyttsx3
district=input("Enter the name of district: ")
url=f"https://api.weatherapi.com/v1/current.json?key=2afcb5b0a93d446ab90134048232803&q={district}"
r=requests.get(url)
#print(r.text) #shows every thing in the url in the form of string
weather_dictionary=json.loads(r.text) #change string into dictionary
# print(weather_dictionary)
temp=weather_dictionary['current']['temp_c']
cond=weather_dictionary['current']['condition']['text']
currrent_time =datetime.now()
print("Current time:",currrent_time)
engine=pyttsx3.init()
text=f"the current condition of {district} is {cond} and the temperature is {temp} "
engine.setProperty('rate', 100)
engine.say(text)
engine.runAndWait()

# print(f"the current condition of {district} is {cond} and the temperature is {temp} ")
