import pandas as pd
import sqlite3

# Load old database
conn = sqlite3.connect("traffic_data_old.db")
df = pd.read_sql("SELECT * FROM traffic_incidents", conn)
conn.close()

# Convert timestamp
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Time Features
df['hour'] = df['timestamp'].dt.hour
df['day'] = df['timestamp'].dt.day_name()
df['month'] = df['timestamp'].dt.month
df['minute'] = df['timestamp'].dt.minute
df['week_number'] = df['timestamp'].dt.isocalendar().week

# Weekend
df['is_weekend'] = df['timestamp'].dt.dayofweek >= 5

# Peak hour
df['is_peak_hour'] = df['hour'].apply(lambda x: 1 if 7 <= x <= 9 or 16 <= x <= 19 else 0)

# Traffic Pattern
df['is_peak_morning'] = df['hour'].between(7,9)
df['is_peak_evening'] = df['hour'].between(16,19)
df['is_night'] = df['hour'].apply(lambda x: 1 if x >= 22 or x <= 5 else 0)

# Severity
severity_map = {
    1: "High",
    6: "Medium",
    7: "Medium",
    8: "High",
    9: "Low"
}

df['severity'] = df['iconCategory'].map(severity_map)

# Time bucket
df['time_of_day'] = pd.cut(
    df['hour'],
    bins=[0,6,12,18,24],
    labels=['Night','Morning','Afternoon','Evening'],
    right=False
)

# Save
df.to_csv("traffic_data_old_with_features.csv", index=False)

print("Old data converted with same features!")