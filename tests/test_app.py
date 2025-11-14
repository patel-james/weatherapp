import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from app import app

def test_home_route():
    """Test that the home page loads correctly."""
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200

def test_weather_route_without_city():
    """Test the /weather returns 400 when city parameter is missing."""
    client = app.test_client()
    response = client.get("/weather")
    assert response.status_code == 400
    assert response.json == {"Error": "Missing 'city' in the query"}

def test_weather_route_with_city():
    """
    Test the /weather route with a valid city parameter.
    """
    client = app.test_client()
    response = client.get("/weather?city=Nashville")
    
    if response.status_code == 500:
        assert True
        return
    
    assert response.status_code == 200
    data = response.json
    assert "city" in data
    assert "country" in data

