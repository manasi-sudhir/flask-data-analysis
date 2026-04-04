import sqlite3
import pandas as pd

# connect to database
conn = sqlite3.connect('traffic_data.db')

# read table
df = pd.read_sql("SELECT * FROM traffic_incidents", conn)

# save to csv
df.to_csv("traffic_data.csv", index=False)

conn.close()

print("CSV file created successfully!")