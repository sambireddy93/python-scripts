#Application-health-check
import requests

# Application URL to check
URL = "http://mysite.com"

try:
    # Send HTTP request with timeout
    response = requests.get(URL, timeout=5)

    # Check status code
    if response.status_code == 200:
        print("Application is UP and running correctly.")
    else:
        print("Application is DOWN or returning an unexpected status code:", response.status_code)

except requests.exceptions.RequestException as e:
    print("Application is DOWN or not reachable.")
    print(f"Error details: {e}")

except Exception as e:
    print(f"Unexpected error: {e}")
