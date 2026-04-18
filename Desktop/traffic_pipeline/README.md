Dublin Traffic Incidents Pipeline
Project Development Report
1. Project Overview
This project was developed to design and implement a complete data processing pipeline for analysing real-time traffic incidents in Dublin using the TomTom Traffic API. The system collects live traffic incident data, stores it, processes it, performs analysis, and presents insights through a web dashboard.
The objective of the project was to demonstrate practical skills in data engineering, automation, feature engineering, testing, and cloud deployment.

2. Project Architecture
TomTom API → Data Collection → Data Storage → Data Cleaning → Feature Engineering → Data Analysis → Visualisation → Flask Dashboard → Google Cloud Deployment

3. Technologies Used
•	Python
•	TomTom Traffic API
•	Pandas
•	Matplotlib
•	Flask
•	SQLite
•	Google Cloud Virtual Machine
•	Unittest
•	ChatGPT (OpenAI) as a development support tool.

4. Development Process
Stage 1: Research and API Selection
Initially, I explored multiple traffic-related APIs to identify a suitable real-time data source. After testing different options, I selected the TomTom Traffic API because it provided structured incident data with useful geographic and severity information.
The selected API endpoint was used to collect traffic incidents within the Dublin region.

Stage 2: Data Collection
The pipeline was designed to collect raw traffic incident data containing fields such as:
•	Latitude
•	Longitude
•	Incident Category
•	Severity
•	Timestamp
At first, I attempted to generate derived features during data collection. However, this created inconsistencies in the raw dataset. I then redesigned the pipeline to first store only clean raw data and perform feature engineering in later stages. This improved reliability and maintainability.
Initially, data was collected manually for testing purposes. Later, the process was automated using a scheduled cron job to fetch new data every five minutes and store it in the database. ChatGPT was consulted for cron scheduling syntax and automation guidance (OpenAI, 2026).
Stage 3: Data Preprocessing
The raw dataset was cleaned and prepared for analysis using Python and Pandas. Preprocessing techniques such as handling missing values, removing duplicates, and formatting data types were reviewed using W3Schools Python and Pandas tutorial resources (W3Schools, 2026).
Preprocessing tasks included:
•	Removing duplicate records
•	Handling missing values
•	Standardising timestamps
•	Formatting column names
Stage 4: Feature Engineering
Additional analytical features were created from the cleaned dataset to generate more meaningful insights.
Features developed included:
•	Hour of incident
•	Time of day classification
•	Day-wise traffic analysis
•	Rush hour indicator
•	Incident type grouping
•	Traffic zones (City Centre, Inner Dublin, Outer Dublin)
•	Severity categories (High, Medium, Low)
These features significantly improved the analytical value of the original raw data.

Stage 5: Data Analysis and Visualisation
Using Matplotlib, multiple charts were generated to analyse traffic behaviour in Dublin.
Visualisations included:
•	Hourly Traffic Analysis
•	Day-wise Analysis
•	Time of Day Analysis
•	Rush Hour Trends
•	Severity Distribution
•	Traffic Zone Analysis
Generated charts were stored in the static folder and integrated into the dashboard. Chart formatting and troubleshooting guidance was supported through ChatGPT where required (OpenAI, 2026)..

Stage 6: Dashboard Development
A Flask web application was developed to display all analysis results through a user-friendly dashboard.
The dashboard enabled visual inspection of:
•	Traffic activity by hour
•	High congestion periods
•	Severity trends
•	Zone-based incident patterns
•	Daily traffic behaviour
ChatGPT was occasionally used for Flask troubleshooting and template debugging (OpenAI, 2026).
Stage 7: Cloud Deployment
The completed Flask dashboard was deployed on a Google Cloud Virtual Machine.
Deployment steps included:
1.	Connecting to the VM via SSH
2.	Navigating to the project directory
3.	Running the Flask application
4.	Accessing the dashboard through the VM IP address and port
5. Testing and Validation
To ensure the reliability of the pipeline, tests were created using Python Unittest.
Tests included:
•	Timestamp conversion validation
•	Database table existence check
•	Data availability verification
These tests helped confirm that the pipeline executed correctly.

6. Evidence of Independent Development
The project was developed incrementally over several weeks. File creation and modification timestamps show progressive work across multiple stages including preprocessing, feature engineering, analysis, testing, and deployment.
The project structure contains separate modules such as:
•	preprocessing.py
•	merge_data.py
•	feature_engineering.py
•	test_pipeline.py
•	analysis.py
This modular progression reflects genuine iterative development.

7. Challenges Faced and Solutions
During development, several practical challenges were encountered:
•	Selecting a reliable traffic API
•	Managing inconsistent raw data
•	Deciding when to apply feature engineering at the moment of later
•	Automating scheduled data collection
•	Deploying Flask on a cloud VM
These were resolved through redesigning the pipeline structure, testing alternative approaches, and incremental debugging.
8. Use of AI Assistance Tools
During the development of this project, ChatGPT (OpenAI) was used as a supplementary support tool for selected tasks such as:
•	Debugging Python errors
•	Understanding Flask deployment steps
•	Cron job scheduling guidance
•	Code optimisation suggestions
•	Explanation of libraries and functions
•	Formatting documentation
All project design decisions, integration of components, testing, execution, and final implementation were completed independently.
9. Conclusion
This project successfully demonstrates the complete lifecycle of a modern data engineering pipeline: data acquisition, storage, preprocessing, feature engineering, analysis, dashboard development, testing, and deployment.
It also reflects practical problem-solving, independent implementation, and the ability to convert real-time raw data into meaningful analytical insights.
References
OpenAI (2026) ChatGPT (GPT-5.3) [Large language model]. Available at: https://chat.openai.com/ (Accessed: 18 April 2026).
ChatGPT Development Support Conversations:
https://chatgpt.com/share/69e0b644-5388-8329-9a3d-201e198a4bd1
https://chatgpt.com/share/69e0b65c-ebc4-8328-b749-776a3624a023
https://chatgpt.com/share/69e0b644-5388-8329-9a3d-201e198a4bd1
https://chatgpt.com/share/69e0b6a5-6d88-8325-b297-5a73acbca6a8
https://chatgpt.com/share/69e0b0b6-068c-832e-831c-ad6a4e0315be
TomTom (2026) Traffic Incident API Documentation. Available at: https://developer.tomtom.com/ (Accessed: 18 April 2026).
W3Schools (2026) Python Tutorial. Available at: https://www.w3schools.com/python/
