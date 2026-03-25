import requests

# The URL of our local Flask API
url = "http://127.0.0.1:5000/generate"

# The data we are simulating a user typing into our HTML form
form_data = {
    "company_name": "OpenAI",
    "job_url": "https://en.wikipedia.org/wiki/Artificial_intelligence" # Using wiki just as a dummy URL with text
}

print("Sending POST request to /generate (this might take 10 seconds for the AI to type)...")

# Make the request
response = requests.post(url, data=form_data)

# Print the result
print("\n--- Response ---")
print("Status Code:", response.status_code)
try:
    print("JSON Data:", response.json())
except:
    print("Text Data:", response.text)
