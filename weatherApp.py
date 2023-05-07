#!/bin/python3

# Import necessary libraries
import requests  # for sending HTTP requests
import json  # for working with JSON data
import os  # for interacting with the operating system

# Prompt user to enter the name of a city
try:
    city = input("Enter the name of city\n")

    # Use the Weather API to retrieve current weather data for the given city
    url = f"https://api.weatherapi.com/v1/current.json?key=94c2758647de479a89a71553230705&q={city}"
    r = requests.get(url)  # send an HTTP GET request to the API

    # Convert the JSON response into a Python dictionary
    wdic = json.loads(r.text)

    # Retrieve the temperature in Celsius from the dictionary
    w = wdic["current"]["temp_c"]

    # Print the current temperature to the console
    print(f"The current weather is in {city} is {w} degrees")

    # Use the espeak command to speak the current temperature aloud
    os.system(f"espeak 'The current weather is in {city} is {w} degrees'")
	
except Exception as e:
	# Print an error message if there was an exception during the execution of the program
	print("Recheck the name of city", e)
