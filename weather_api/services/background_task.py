from background_task import background
from ..models import EmailLocation
import requests
from ..services.mail import MailService
from django.conf import settings

@background
def daily_weather_email(email: str):
    locations = EmailLocation.get_locations_by_email(email)

    if not locations:
        return

    message = ""
    for location in locations:
        weather_data = requests.get(f"{settings.WEATHER_API_URL}/forecast.json?key={settings.WEATHER_API_KEY}&q={location}&days=10&aqi=no&alerts=no").json()
        message += f"Location: {location}\n"
        message += f"Current Temperature: {weather_data['current']['temp_c']}C\n"
        message += f"Condition: {weather_data['current']['condition']['text']}\n"
    
    MailService.send_mail("Weather API - Daily Weather Report", message, email)
