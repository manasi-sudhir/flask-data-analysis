import requests
import pandas as pd
from datetime import datetime
import sqlite3
import os
api_key = "s79GgVOx4NfNJ18iuPXItZddGBBqyRgw"

    
url = f"https://api.tomtom.com/traffic/services/5/incidentDetails?bbox=-6.4,53.2,-6.1,53.4&key={api_key}"

response = requests.get(url)
data = response.json()

incidents = data['incidents']

records = []

for incident in incidents:
    
    icon = incident['properties']['iconCategory']
    geometry = incident['geometry']
    
    coords = geometry['coordinates']
    
    if geometry['type'] == 'Point':
        lon, lat = coords
    else:
        lon, lat = coords[0]
    
    records.append({
        "iconCategory": icon,
        "latitude": lat,
        "longitude": lon,
        "timestamp": datetime.now()
        
    })
df = pd.DataFrame(records)

print(df.head())
#store in SQL
conn = sqlite3.connect('traffic_data.db')
df.to_sql('traffic_incidents', conn, if_exists='append', index=False)
conn.close()

print("Data fetched at:", datetime.now())
import os
#save CSV backup
if os.path.exists("traffic_data.csv"):
    df.to_csv("traffic_data.csv", mode='a', header=False, index=False)
else:
    df.to_csv("traffic_data.csv", index=False)

