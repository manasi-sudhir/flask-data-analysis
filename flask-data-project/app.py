from flask import Flask
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    # Sample data
    data = {
        'Name': ['A', 'B', 'C'],
        'Marks': [80, 90, 85]
    }

    df = pd.DataFrame(data)

    avg = df['Marks'].mean()

    return f"""
    <h1>Student Data Analysis</h1>
    <p>Average Marks: {avg}</p>
    {df.to_html()}
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
