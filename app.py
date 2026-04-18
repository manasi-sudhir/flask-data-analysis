import sqlite3
import pandas as pd
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():

    conn = sqlite3.connect('traffic_data.db')
    df = pd.read_sql("SELECT * FROM Traffic_features", conn)

    total = len(df)

    rush = len(df[df['rush_hour_category'] != 'Non Rush'])

    high = len(df[df['severity'] == 'High'])

    low = len(df[df['severity'] == 'Low'])

    day = df['day'].value_counts()

    return render_template('index.html',
                           total=total,
                           rush=rush,
                           high=high,
                           low=low,
                           day_labels=list(day.index),
                           day_values=list(day.values)
                           )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
