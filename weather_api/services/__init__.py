import requests
from typing import List
from django.http import HttpRequest
from ..exceptions import LocationNotFound, ExternalAPIError, LocationMissing, EmailCodeNotMatch
from django.conf import settings
from ..utils.function import get_random_code
from ..models import EmailCode, EmailLocation
from ..services.mail import MailService
from django.db import transaction

class WeatherService:
    def get_weather_information(self, location: str):
        if not location:
            raise LocationMissing()

        weather_data = requests.get(f"{settings.WEATHER_API_URL}/forecast.json?key={settings.WEATHER_API_KEY}&q={location}&days=10&aqi=no&alerts=no").json()
        
        if "error" in weather_data:
            raise LocationNotFound()
        
        if "current" not in weather_data:
            raise ExternalAPIError()
        
        return weather_data
    
    def search_location(self, location: str):
        if not location:
            raise LocationMissing()

        locations_data = requests.get(f"{settings.WEATHER_API_URL}/search.json?key={settings.WEATHER_API_KEY}&q={location}").json()
        
        return locations_data
    
    @transaction.atomic
    def send_code(self, email: str):
        code = get_random_code()

        if EmailCode.objects.filter(email=email).exists():
            email_code = EmailCode.get_email_code(email)
            email_code.code = code
            email_code.save()
        else:
            EmailCode.objects.create(email=email, code=code)
        
        MailService.send_mail("Weather API - Email Verification", f"Your verification code is {code}", email)
        return True

    def verify_code(self, email: str, code: str, type: str, locations: List[str]):
        email_code = EmailCode.get_email_code(email)
        
        if email_code.code != code:
            raise EmailCodeNotMatch()
        
        if type == "register":
            email_locations = [EmailLocation(email=email, location=location) for location in locations]
            EmailLocation.objects.bulk_create(email_locations)

        else:
            existing_locations = EmailLocation.objects.filter(email=email, location__in=locations)
            existing_location_names = existing_locations.values_list('location', flat=True)
            non_existing_locations = set(locations) - set(existing_location_names)

            if non_existing_locations:
                raise LocationNotFound()
            
            existing_locations.delete()
        
        return True


                                        
