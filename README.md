# Python Weather Forecaster

## Overview

The **Python Weather Forecaster** is a simple command-line application that allows users to fetch weather forecasts for a given USA zipcode. It uses the OpenWeatherMap API to retrieve weather data, such as temperature, humidity, wind speed, and a brief description of the weather conditions.

## How It Works

1. The program prompts the user to enter a valid USA zipcode.
2. It sends a request to the OpenWeatherMap API using the entered zipcode.
3. The program retrieves the weather forecast for the specified location and displays it to the user.
4. Users can choose to fetch another forecast or quit the application.

## Requirements

- Python 3.x
- `requests` module (can be installed using `pip install requests`)
- OpenWeatherMap API key (already included in the code)

## Installation

1. Clone this repository or download the code files.
2. Install the required `requests` module by running:

```
bash
pip install requests
```
3. Run the `python_weather_forecaster.py` file in your terminal

## How to Use
1. Run the Program: After launching the program, you will be greeted with a welcome message.
2. Enter Zipcode: The program will prompt you to enter a valid USA zipcode.
3. View Forecast: The program fetches the weather forecast for the provided zipcode, displaying the temperature, humidity, wind speed, and weather description.
4. Choose to Continue or Quit: After retrieving a forecast, the program asks if you would like to get another forecast (Y for yes, N for no).

## Error Handling
* If an invalid zipcode is entered or there is an issue with the API connection, an error message will be displayed, and the program will prompt the user to try again.
* If the user enters an invalid option when asked if they want another forecast, the program will notify them and ask again.

## Example Output
```
Welcome to the Python Weather Forecaster
==========================================
Please enter a USA zipcode to receive the weather forecast: 90210
The weather forecast for 90210 in Beverly Hills is: 75°F, with humidity at 60%, wind at 5mph, and you can expect: clear sky.

Retrieve another forecast? Type 'Y' or 'N': Y

```

This project is open-source and available under the MIT License.
