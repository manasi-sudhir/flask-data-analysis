import sqlite3
import pandas as pd

#connect to db
conn=sqlite3.connect('traffic_data.db')

#load raw data
df=pd.read_sql("SELECT* FROM traffic_incidents", conn)
print("raw data shape:",df.shape)

#remove duplicates
df = df.drop_duplicates()

#handle missing values
df = df.dropna()

#convert timestamp
df['timestamp']=pd.to_datetime(df['timestamp'])

print("Cleaned data shape:", df.shape)

#save cleaned data 
df.to_sql("traffic_incidents_clean",conn, if_exists='replace',index=False)

conn.close()
print("preprocessing complete!")

print(df.columns)