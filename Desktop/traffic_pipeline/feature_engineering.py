import sqlite3
import pandas as pd
import numpy as np

#connect to database
conn= sqlite3.connect('traffic_data.db')

#load cleaned data 
df=pd.read_sql("SELECT*FROM traffic_incidents_clean",conn)

print("loaded clean data:", df.shape)

#convert timestamp
df['timestamp']=pd.to_datetime(df['timestamp'])

#time_based derived features
df['hour']=df['timestamp'].dt.hour
df['day']=df['timestamp'].dt.day_name()
df['month']=df['timestamp'].dt.month
df['minute']=df['timestamp'].dt.minute
df['week_number']=df['timestamp'].dt.isocalendar().week
df['is_weekend']=df['timestamp'].dt.dayofweek >=5

#Traffic pattern features
df['is_peak_hour']=df['hour'].apply(lambda x:1 if 7<=x<=9 or 16<=x<=19 else 0)
df['is_peak_morning']=df['hour'].between(7,9)
df['is_peak_evening']=df['hour'].between(16,19)
df['is_night']=df['hour'].apply(lambda x:1 if x>=22 or x<=5 else 0)

#severity mapping
severity_map={
    1:"High",
    6:"Medium",
    7:"Medium",
    8:"High",
    9:"Low"
}
df['severity']=df['iconCategory'].map(severity_map)

#time Bucket feature
df['time_of_day']=pd.cut(
    df['hour'],
    bins=[0,6,12,18,24],
    labels=['Night','Morning','Afternoon','Evening'],
    right=False
)

#Incident Type feature
incident_map={
    1:"Accident",
    6:"Road Closure",
    7:"Construction",
    8:"congestion",
    9:"Hazard"
}
df['incident_type']=df['iconCategory'].map(incident_map)

#day type feature
df['day_type']=df['is_weekend'].map({
    True:"Weekend",
    False:"Weekday"
})

#Distance From Dublin City Centre
DUBLIN_LAT=53.3498
DUBLIN_LON=-6.2603

def haversine(lat,lon):
    R=6371
    lat1=np.radians(lat)
    lon1=np.radians(lon)
    lat2=np.radians(DUBLIN_LAT)
    lon2=np.radians(DUBLIN_LON)

    dlat=lat2-lat1
    dlon=lon2-lon1

    a=np.sin(dlat/2)**2 + np.cos(lat1)*np.cos(lat2)* np.sin(dlon/2)**2
    c=2*np.arcsin(np.sqrt(a))

    return R*c
df['distance_from_centre_km']=df.apply(
    lambda x:haversine(x['latitude'],x['longitude']),axis=1
)

#traffic zone feature 
def traffic_zone(distance):
    if distance<2:
        return "City Center"
    elif distance <5:
        return"Inner Dublin"
    else:
        return"Outer Dublin"
df['traffic_zone']=df['distance_from_centre_km'].apply(traffic_zone)

#rush hour category
def rush_hour(row):
    if row['is_peak_morning']:
        return "Morning Rush"
    elif row['is_peak_evening']:
        return "Evening Rush"
    else:
        return "Non Rush"
df['rush_hour_category']=df.apply(rush_hour, axis=1)
        
#save to database
df.to_sql("Traffic_features",conn, if_exists='replace', index=False)
conn.close()
print("Feature engineering complete!")
print("Final datset shape:",df.shape)