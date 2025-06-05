from api_consumers.weather_api import get_weather

def risk_of_blackout(lat: float, lon: float) -> dict:
    """
    Regra: se a maior chance de chuva nas próximas 24h for > 50%, risco é ALTO.
    """
    data = get_weather(lat, lon)
    hourly = data["hourly"]["precipitation_probability"]
    max_prob = max(hourly)

    risk = "ALTO" if max_prob > 50 else "BAIXO"

    return {
        "max_precipitation_probability": max_prob,
        "blackout_risk": risk
    }
