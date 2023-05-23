# -*- coding: utf-8 -*-
import time
import json
from datetime import datetime
from bmp280 import BMP280

try:
    from smbus2 import SMBus
except ImportError:
    from smbus import SMBus

print("""temperature-and-pressure.py - Displays the temperature and pressure.

Press Ctrl+C to exit!
""")

# Initialise the BMP280
bus = SMBus(1)
bmp280 = BMP280(i2c_dev=bus)
# Create a dictionary to store temperature and pressure data
data = []

while True:
    temperature = bmp280.get_temperature()
    pressure = bmp280.get_pressure()
    temp = '{:05.2f}'.format(temperature)
    press = '{:05.2f}'.format(pressure)
    text = "temperatura: " + temp + "ºC - " + "pressió: " + press + "hPa"
    print(text)

    # Append temperature and pressure data to the dictionary
    data.append({"time": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
                 "temperature": temperature,
                 "pressure": pressure})

    # Save the data to a JSON file
    with open("/var/www/html/Weather-Dashboard/data.json", "w") as outfile:
        json.dump(data, outfile)

    time.sleep(1)
