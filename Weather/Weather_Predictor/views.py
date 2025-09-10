from django.shortcuts import render
import json
from urllib.error import HTTPError
import urllib.request

def index(request):
  if request.method == 'POST':
    city = request.POST['city']
    try:
      res = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=05d83429f1537b3e6735a1f8b25538d5').read()
      json_data= json.loads(res)
      temp = float(json_data['main']['temp']) 
      temp_in_celsius = round(temp - 273.15, 2)
      data = {
       "country_code" : str(json_data['sys']['country']),
       "coordinate" : str(json_data['coord']['lon']) + ' ' + str(json_data['coord']['lat']),
        "temp" : temp_in_celsius ,
        "pressure" : str(json_data['main']['pressure']),
        "humidity" : str(json_data['main']['humidity']),
        "icon" :  (json_data['weather'][0]['icon']),
      }
    except HTTPError as e:
        data = {'error': f"City '{city}' not found. Please check the spelling."}
    except Exception as e:
        data = {'error': 'An unexpected error occurred.'}
    
  else:
    city =''
    data = {}
    
  return render(request, 'index.html',{"city" : city , "data" : data})
