import requests

url = "https://api.nasa.gov/planetary/apod"
f = open("key_nasa.txt", "r")
api_key = f.read()

params = {
    "api_key": api_key
}

response = requests.get(url, params=params)

data = response.json()
print("Title:", data['title'])
print("Explanation:", data['explanation'])
print("Image URL:", data['url'])