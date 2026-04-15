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

plt.xticks(rotation=30, ha='right')
plt.tight_layout()

plt.savefig("static/incident_type_analysis.png")
plt.close()

#2.Hourly Analysis
print ("\nIncidents by Hour:")
print(df['hour'].value_counts().sort_index())

plt.figure(figsize=(10,6))
df['hour'].value_counts().sort_index().plot(kind='bar')
plt.title("Traffic Incidents by Hour")
plt.xlabel("Hour")
plt.ylabel("Count")
plt.savefig("static/hourly_analysis.png")
plt.close()

#day analysis
print("|nIncidents by Day:")
print(df['day'].value_counts())
plt.figure(figsize=(10,6))
df['day'].value_counts().plot(kind='bar')
plt.title("Traffic Incidents by Day")
plt.xlabel("Day")
plt.ylabel("Count")

plt.xticks(rotation=30, ha='right')
plt.tight_layout()

plt.savefig("static/day_analysis.png")
plt.close()

#Severity Analysis
print("\nSeverity Distribution:")
print(df['severity'].value_counts())

plt.figure()

df['severity'].value_counts().plot(
    kind='pie',
    autopct='%1.1f%%',
    startangle=90
)

plt.title("Traffic Severity Distribution")
plt.ylabel("")

plt.savefig("static/severity_pie.png")

#Time of Day Analysis
print("\nTime of Day Distribution:")
print(df['time_of_day'].value_counts())
plt.figure(figsize=(10,6))
df['time_of_day'].value_counts().plot(kind='bar')
plt.title("Traffic Incidents by Time of Day")
plt.xlabel("Time of Day")
plt.ylabel("Count")

plt.xticks(rotation=30, ha='right')
plt.tight_layout()

plt.savefig("static/time_of_day_analysis.png")
plt.close()

# Traffic Zone Analysis (PIE)

print("\nTraffic zone Distribution")
print(df['traffic_zone'].value_counts())

plt.figure(figsize=(8,8))

colors = ['#2E86C1', '#28B463', '#F39C12']  # blue, green, orange

df['traffic_zone'].value_counts().plot(
    kind='pie',
    autopct='%1.1f%%',
    colors=colors
)

plt.title("Traffic Zone Distribution")

plt.savefig("static/traffic_zone_analysis.png")
plt.close()

#Rush Hour Analysis
print("\nRush Hour Distribution:")
print(df['rush_hour_category'].value_counts())
plt.figure(figsize=(10,6))
df['rush_hour_category'].value_counts().plot(kind='bar')
plt.title("Rush Hour Traffic Incidents")
plt.xlabel("Rush Hour Category")
plt.ylabel("count")

plt.xticks(rotation=30, ha='right')
plt.tight_layout()

plt.savefig("static/rush_hour_analysis.png")
plt.close()

# Severity vs Time of Day Analysis

print("\nSeverity vs Time of Day:")
pivot = df.groupby(['time_of_day', 'severity']).size().unstack()

print(pivot)

plt.figure()

pivot.plot(kind='bar', stacked=True)

plt.title("Severity vs Time of Day")
plt.xlabel("Time of Day")
plt.ylabel("Count")

plt.xticks(rotation=30, ha='right')
plt.tight_layout()

plt.savefig("static/severity_time.png")
plt.close()

#Close connection
conn.close()
print("\nData Analysis Completed Successfully!")
