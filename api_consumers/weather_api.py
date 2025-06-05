import requests

BASE_URL = "https://api.open-meteo.com/v1/forecast"

def get_weather(lat: float, lon: float) -> dict:
    """Consulta a probabilidade de precipitação nas próximas 24h"""
    params = {
        "latitude": lat,
        "longitude": lon,
        "hourly": "precipitation_probability",
        "forecast_days": 1
    }

    response = requests.get(BASE_URL, params=params, timeout=10)
    response.raise_for_status()  # Lança erro se a API falhar
    return response.json()
