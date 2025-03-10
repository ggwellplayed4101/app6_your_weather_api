# Weather Station API

This API provides weather information from different weather stations at various timestamps.

## Features
- Get weather data from multiple stations of Europe
- Get historical weather data spanning multiple centuries

## How to use
- Make a URL request using the following format:

http://127.0.0.1:5000/api/v1/{station}/{date}
Replace {station} with the station number and {date} with desired date formated YYYY-MM-DD.

- Example request:
http://127.0.0.1:5000/api/v1/10/1988-10-25

- The API returns data in JSON format with temperature, humidity, and pressure readings. 
