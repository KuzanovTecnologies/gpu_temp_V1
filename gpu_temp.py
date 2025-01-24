import requests # type: ignore
import json

def get_gpu_temperature():
    try:
        # URL for OpenHardwareMonitor's web server
        url = "http://localhost:8085/data.json"
        response = requests.get(url)  # Fetch data from the server
        response.raise_for_status()  # Raise an error for bad responses

        # Parse the JSON data
        data = json.loads(response.text)
        gpu_temperature = None

        # Traverse the JSON structure to find GPU temperature
        for hardware in data['Children']:
            if 'GPU' in hardware['Text']:  # Adjust keyword as needed
                for sensor in hardware['Children']:
                    if 'Temperature' in sensor['Text']:
                        gpu_temperature = sensor['Value']
                        break

        # Display the result or handle no data
        if gpu_temperature is not None:
            print(f"GPU Temperature: {gpu_temperature}°C")
        else:
            print("GPU temperature data not found.")
    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")