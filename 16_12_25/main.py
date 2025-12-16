import requests
import json

url = "https://api.open-meteo.com/v1/forecast?latitude=54.3523&longitude=18.6491&current=temperature_2m,relative_humidity_2m,apparent_temperature,is_day&hourly=temperature_2m,relative_humidity_2m,apparent_temperature,precipitation,cloud_cover,wind_speed_10m&daily=weather_code,uv_index_max&timezone=Europe%2FBerlin"

response = requests.get(url)

print(response.text)

with open("response.json", "wt") as f:
    json.dump(eval(response.text), f, indent=2)