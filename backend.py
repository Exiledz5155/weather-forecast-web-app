import requests


API_KEY = "1bb933fc6f326228bf8a15e21b615b80"

def get_data(place, forecast_days=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"] # Access relevant data
    nr_values = 8 * forecast_days # Calculate amount of data needed
    filtered_data = filtered_data[:nr_values] # Filter relevant amount of data

    return filtered_data

if __name__ == "__main__":
    print(get_data(place="Tokyo"))