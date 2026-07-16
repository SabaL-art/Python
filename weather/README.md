# Weather App

A terminal-based Weather App built in Python.

Get the current weather conditions for any city using the OpenWeather API. The program displays the city, country, weather condition, humidity, and temperature in Celsius.

## Features

- Search weather by city name
- Current weather conditions
- Temperature in Celsius
- Humidity information
- Country detection
- Error handling for invalid city names
- API key stored separately for security

## Requirements

- Python 3.10+
- requests

## Installation

Install the required dependency:

```bash
pip install requests
```

## Setup

Create a file named:

```text
config.py
```

Add your OpenWeather API key:

```python
API_KEY = "your_api_key_here"
```

You can obtain a free API key from:

https://openweathermap.org/api

## Run

```bash
python3 weather.py
```

## Example

```text
Enter city name: Kathmandu

City: Kathmandu
Country: NP
Weather: Clouds
Humidity: 78 %
Temperature: 24.6 °C
```

## Output

The program displays:

- City
- Country
- Current weather
- Humidity
- Temperature (°C)

## Concepts Practiced

- API requests
- JSON parsing
- HTTP requests
- Functions
- User input
- Exception handling
- Working with external services
- Python modules

## Project Structure

```text
weather.py
config.py      # Stores OpenWeather API key
```

## Future Improvements

- 5-day weather forecast
- Weather icons
- Wind speed and pressure
- Sunrise and sunset times
- Automatic location detection
- GUI version using Tkinter
- Better error handling for network failures
- Support for Fahrenheit and Kelvin

## Author

Sabal