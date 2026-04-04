import requests
import pandas as pd
from datetime import datetime
import sqlite3
from geopy.geocoders import Nominatim
import time
geolocator = Nominatim(user_agent="traffic_pipeline")

def get_location(lat, lon):
    try:
        location = geolocator.reverse((lat, lon), timeout=10)
        address = location.raw.get('address', {})
        
        city = address.get('city', address.get('town', address.get('village', None)))
        county = address.get('county', None)

        return pd.Series([city, county])
    
    except:
        return pd.Series([None, None])
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
df['hour'] = df['timestamp'].dt.hour
df['day'] = df['timestamp'].dt.day_name()
# derived features
df['hour'] = df['timestamp'].dt.hour
df['day'] = df['timestamp'].dt.day_name()
df['month'] = df['timestamp'].dt.month
df['is_weekend'] = df['timestamp'].dt.dayofweek >= 5
df['minute'] = df['timestamp'].dt.minute
df['week_number'] = df['timestamp'].dt.isocalendar().week
df['is_peak_hour'] = df['hour'].apply(lambda x: 1 if 7 <= x <= 9 or 16 <= x <= 19 else 0)
#traffic pattern
df['is_peak_morning'] = df['hour'].between(7,9)
df['is_peak_evening'] = df['hour'].between(16,19)
df['is_night'] = df['hour'].apply(lambda x: 1 if x >= 22 or x <= 5 else 0)
#location Based
df['is_peak_morning'] = df['hour'].between(7,9)
df['is_peak_evening'] = df['hour'].between(16,19)
df['is_night'] = df['hour'].apply(lambda x: 1 if x >= 22 or x <= 5 else 0)
#severity Based
severity_map = {
    1: "High",
    6: "Medium",
    7: "Medium",
    8: "High",
    9: "Low"
}
df['severity'] = df['iconCategory'].map(severity_map)
#time bucket feature
df['time_of_day'] = pd.cut(
    df['hour'],
    bins=[0,6,12,18,24],
    labels=['Night','Morning','Afternoon','Evening'],
    right=False
)
#df[['city', 'county']] = df.apply(
 #   lambda x: get_location(x['latitude'], x['longitude']), axis=1
#)
print(df.head())
conn = sqlite3.connect('traffic_data.db')
df.to_sql('traffic_incidents', conn, if_exists='append', index=False)
conn.close()

print("Data fetched at:", datetime.now())
import os

if os.path.exists("traffic_data.csv"):
    df.to_csv("traffic_data.csv", mode='a', header=False, index=False)
else:
    df.to_csv("traffic_data.csv", index=False)

