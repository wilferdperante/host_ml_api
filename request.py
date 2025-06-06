import requests
# Define the URL of your Flask API
url = 'http://127.0.0.1:5000/predict'

# Define the input data as a dictionary
data = {
    "Avg. Session Length": [34.49726773, 31.92627203, 33.00091476, 34.30555663],
    "Time on App": [12.65565115, 11.10946073, 11.33027806, 13.71751367],
    "Time on Website": [50.57766802, 80.26895887, 37.11059744, 36.72128268],
    "Length of Membership": [1.082620633, 2.664034182, 4.104543202, 3.120178783]
}

# Send a POST request to the API with the input data
response = requests.post(url, json=data)

# Check the HTTP response status code
if response.status_code == 200:
    # Parse and print the JSON response (assuming it contains the prediction)
    prediction = response.json()
    print(prediction)
else:
    # Handle the case where the API request failed
    print(f'API Request Failed with Status Code: {response.status_code}')
    print(f'Response Content: {response.text}')
