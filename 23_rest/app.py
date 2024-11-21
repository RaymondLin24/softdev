import json
import urllib.request
from flask import Flask, render_template

app = Flask(__name__)
with open('key_nasa.txt', 'r') as file:
    API_KEY = file.read()
APOD_URL = f'https://api.nasa.gov/planetary/apod?api_key={API_KEY}'

@app.route('/')
def index():

    with urllib.request.urlopen(APOD_URL) as response:
        if response.status == 200:
            data = json.loads(response.read().decode())

            title = data['title']
            date = data['date']
            explanation = data['explanation']
            image_url = data['url']

            return render_template('main.html', title=title, date=date, explanation=explanation, image_url=image_url)
        else:
            return f"Error fetching data: {response.status}"

if __name__ == '__main__':
    app.run(debug=True)
