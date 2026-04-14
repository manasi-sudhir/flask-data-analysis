import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

#connect to database
conn=sqlite3.connect('traffic_data.db')

#load feature engineered data
df=pd.read_sql("SELECT * FROM Traffic_features",conn)

print("Dataset shape:", df.shape)

#1. incident type analysis

print("\n Incident Type Distribution:")
print(df['incident_type'].value_counts())
plt.figure(figsize=(10,6))
df['incident_type'].value_counts().plot(kind='bar')
plt.title("Traffic Incidents by Type")
plt.xlabel("Incident Type")
plt.ylabel("count")
plt.savefig("incident_type_analysis.png")
plt.close()

#2.Hourly Analysis
print ("\nIncidents by Hour:")
print(df['hour'].value_counts().sort_index())

plt.figure(figsize=(10,6))
df['hour'].value_counts().sort_index().plot(kind='bar')
plt.title("Traffic Incidents by Hour")
plt.xlabel("Hour")
plt.ylabel("Count")
plt.savefig("hourly_analysis.png")
plt.close()

#day analysis
print("|nIncidents by Day:")
print(df['day'].value_counts())
plt.figure(figsize=(10,6))
df['day'].value_counts().plot(kind='bar')
plt.title("Traffic Incidents by Day")
plt.xlabel("Day")
plt.ylabel("Count")
plt.savefig("day_anaysis.png")
plt.close()

#Severity Analysis

print("|nSeverity Distribution:")
print(df['severity'].value_counts())
plt.figure(figsize=(10,6))
df['severity'].value_counts().plot(kind='bar')
plt.title("Traffic Severity Distribution")
plt.xlabel("Severity")
plt.ylabel("Count")
plt.savefig("severity_analysis.png")
plt.close()

#Time of Day Analysis
print("\nTime of Day Distribution:")
print(df['time_of_day'].value_counts())
plt.figure(figsize=(10,6))
df['time_of_day'].value_counts().plot(kind='bar')
plt.title("Traffic Incidents by Time of Day")
plt.xlabel("Time of Day")
plt.ylabel("Count")
plt.savefig("Time_of_day_analysis.png")
plt.close()

#Traffic Zone Analysis
print("\nTraffic zone Distribution")
print(df['traffic_zone'].value_counts())
plt.figure(figsize=(10,6))
df['traffic_zone'].value_counts().plot(kind='bar')
plt.title("Traffic Incidents by Zone")
plt.xlabel("Zone")
plt.ylabel("Zone")
plt.savefig("Traffic_Zone_Anlysis.png")
plt.close()

#Rush Hour Analysis
print("\nRush Hour Distribution:")
print(df['rush_hour_category'].value_counts())
plt.figure(figsize=(10,6))
df['rush_hour_category'].value_counts().plot(kind='bar')
plt.title("Rush Hour Traffic Incidents")
plt.xlabel("Rush Hour Category")
plt.ylabel("count")
plt.savefig("rush_hour_analysis.png")
plt.close()

#Close connection
conn.close()
print("\nData Analysis Completed Successfully!")
