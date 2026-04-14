# Traffic Data Pipeline using TomTom API

This project builds an end-to-end traffic data pipeline using TomTom API.

Project Overview
This project implements an end-to-end traffic data pipeline using the TomTom Traffic API. The system collects real-time traffic incident data, processes it, performs analysis, and displays results through a web dashboard.

The pipeline includes:

Data Fetching (TomTom API)
Data Preprocessing
Feature Engineering
Data Analysis
Dashboard Development (Flask)
Cloud Deployment (Google Cloud VM)
Project Architecture

TomTom API → Data Fetching → Preprocessing → Feature Engineering → Data Analysis → Visualization → Flask Dashboard → Deployment

Project Structure

traffic_pipeline/

traffic_pipeline.py (Data fetching from TomTom API)
preprocessing.py (Data cleaning)
feature_engineering.py (Feature creation)
analysis.py (Data analysis and charts)
app.py (Flask dashboard)

templates/

index.html (Dashboard layout)

static/

day_analysis.png
traffic_zone_analysis.png
rush_hour_analysis.png
time_of_day_analysis.png
severity_analysis.png
hourly_analysis.png

traffic_data.db
README.md

Data Fetching (TomTom API)

Traffic data is collected using the TomTom Traffic Incident API.

API Used:

https://api.tomtom.com/traffic/services/5/incidentDetails

Data collected includes:

Traffic incidents
Latitude and longitude
Incident category
Timestamp
Severity
Data Preprocessing

The preprocessing step cleans the raw traffic data.

Steps performed:

Remove duplicates
Handle missing values
Convert timestamp format
Format columns
Feature Engineering

New features are created from the raw data.

Features created:

Hour
Day
Month
Weekend indicator
Peak hour
Time of day
Severity
Traffic zone
Data Analysis

The following visualizations are generated:

Day Analysis
Traffic Zone Analysis
Rush Hour Analysis
Time of Day Analysis
Severity Analysis
Hourly Analysis

Charts are generated using Matplotlib and stored in the static folder.

Dashboard

A Flask dashboard displays all traffic analysis charts.

The dashboard includes:

Day Analysis
Traffic Zone Analysis
Rush Hour Analysis
Time of Day Analysis
Severity Analysis
Hourly Analysis
Deployment

The dashboard is deployed on a Google Cloud Virtual Machine.

Steps to run:

SSH into VM

cd traffic_pipeline

python app.py

Access dashboard:

http://VM-IP:8080

Technologies Used
Python
TomTom API
Pandas
Matplotlib
Flask
SQLite
Google Cloud VM
Results

The dashboard provides insights into:

Traffic patterns
Peak traffic hours
High traffic zones
Incident severity
Time-based traffic trends
Future Improvements
Real-time streaming
Machine learning prediction
Interactive dashboard
Map visualization
Author

Manasi Sonawane
Traffic Data Analysis Pipeline
