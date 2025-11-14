from flask import Flask, jsonify, request, render_template
import os
import requests

app = Flask(__name__)

# reads the environment variable for the weather API key from the terminal
WEATHER_API_KEY = os.environ.get('WEATHER_API_KEY')

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/weather", methods=["GET"])
def get_weather():
    """
    Example: /weather?city=Nashville
    Returns the current weather for Nashville.
    """

    city = request.args.get("city")

    if not city:
        return jsonify({"Error": "Missing 'city' in the query"}), 400
    
    if not WEATHER_API_KEY:
        return jsonify({"Error": "Weather API key is either incorrect or not set up properly."}), 500

    #Build the URL for the weather API request
    api_url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": WEATHER_API_KEY,
        "units": "metric" 
    }

    try:
        response= requests.get(api_url, params=params, timeout=5)

    except requests.exceptions.RequestException as e:
        return jsonify({"Error": f"Failed to connect to the weather service: {str(e)}"}), 502

    if response.status_code != 200:
        return jsonify({
            "Error": "Failed to retrieve weather data",
            "status_code": response.status_code,
            "details": response.text
        }), 502
    
    data = response.json()

    result = {
        "city": data.get("name"),
        "country": data.get("sys", {}).get("country"),
        "temperature": data.get("main", {}).get("temp"),
        "feels_like": data.get("main", {}).get("feels_like"),
        "humidity": data.get("main", {}).get("humidity"),
        "description": data.get("weather", [{}])[0].get("description"),
    }

    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)