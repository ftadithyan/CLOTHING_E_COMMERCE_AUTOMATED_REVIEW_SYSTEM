import requests

url = "http://127.0.0.1:5000/predict"
payload = {"name": "Alice", "review": "Great, rather heavyweight, long cardi. i purchased the blue, which is a lovely shade of gray/blue, not quite as bright as the picture depicts. pin is adorable; doubt i'll ever use it to close the sweater, but still a nice touch. for reference i'm 5'5\", 136 lbs, 34ddd and typically fall between size small and medium. took a medium in this one and glad i did. perfect fit. falls exactly like on the model."}

response = requests.post(url, json=payload)
print(response.json())
