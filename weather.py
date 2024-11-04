import requests

def get_city_and_condition():
    """Fetch city names and condition from the API."""
    response = requests.get("https://quest.squadcast.tech/api/AP21110011299/weather")
    data = response.json()
    return data['city1'], data['city2'], data['condition']

def get_weather_details(city):
    """Fetch weather details for a given city."""
    response = requests.get(f"https://quest.squadcast.tech/api/AP21110011299/weather/get?q={city}")
    return response.json()

def determine_better_location(city1, city2, condition):
    """Determine which city is better based on the given condition."""
    weather1 = get_weather_details(city1)
    weather2 = get_weather_details(city2)

    if condition == "hot":
        return city1 if weather1['temperature'] > weather2['temperature'] else city2
    elif condition == "cold":
        return city1 if weather1['temperature'] < weather2['temperature'] else city2
    elif condition == "windy":
        return city1 if weather1['wind'] > weather2['wind'] else city2
    elif condition == "rainy":
        return city1 if weather1['rain'] > weather2['rain'] else city2
    elif condition == "sunny":
        return city1 if weather1['cloud'] < weather2['cloud'] else city2
    elif condition == "cloudy":
        return city1 if weather1['cloud'] > weather2['cloud'] else city2

def main():
    city1, city2, condition = get_city_and_condition()
    answer = determine_better_location(city1, city2, condition)
    print("Better Location:", answer)

    # Construct the submission URL
    submission_url = f"https://quest.squadcast.tech/api/AP21110011299/submit/weather?answer={answer}&extension=py"
    print("Submission URL:", submission_url)

    # Submit the code (using an HTTP POST request)
    code = '''
import requests

def get_city_and_condition():
    response = requests.get("https://quest.squadcast.tech/api/AP21110011299/weather")
    data = response.json()
    return data['city1'], data['city2'], data['condition']

def get_weather_details(city):
    response = requests.get(f"https://quest.squadcast.tech/api/AP21110011299/weather/get?q={{city}}")
    return response.json()

def determine_better_location(city1, city2, condition):
    weather1 = get_weather_details(city1)
    weather2 = get_weather_details(city2)

    if condition == "hot":
        return city1 if weather1['temperature'] > weather2['temperature'] else city2
    elif condition == "cold":
        return city1 if weather1['temperature'] < weather2['temperature'] else city2
    elif condition == "windy":
        return city1 if weather1['wind'] > weather2['wind'] else city2
    elif condition == "rainy":
        return city1 if weather1['rain'] > weather2['rain'] else city2
    elif condition == "sunny":
        return city1 if weather1['cloud'] < weather2['cloud'] else city2
    elif condition == "cloudy":
        return city1 if weather1['cloud'] > weather2['cloud'] else city2

def main():
    city1, city2, condition = get_city_and_condition()
    answer = determine_better_location(city1, city2, condition)
    print("Better Location:", answer)

if __name__ == "__main__":
    main()
'''
    response = requests.post(submission_url, data=code)
    print(response.text)

if __name__ == "__main__":
    main()
