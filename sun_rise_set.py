import requests
from datetime import datetime as dt

VAN_LAT = 49.269909
VAN_LNG = -123.153237

# dictionary
parameters = {
    "lat": VAN_LAT,
    "lng": VAN_LNG,
    "formatted": 0
}
# Endpoint ? Param Name = Value &
# https://api.sunrise-sunset.org/json?lat=49.269909&lng=-123.153237

url = "https://api.sunrise-sunset.org/json"
responce = requests.get(url, params=parameters)
responce.raise_for_status()
data = responce.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

print(f"Sunrise: {sunrise} \nSunset: {sunset}\n")

time_now = dt.now()
print(f"Time Now: {time_now.hour}")
