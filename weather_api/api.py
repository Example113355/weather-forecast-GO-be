from ninja import Router
from django.http import HttpRequest
from weather_api.schemas.response import WeatherResponse, SearchResponse
from weather_api.schemas.weather import EmailSchema, EmailCodeSchema
from weather_api.services import WeatherService

router = Router()

class WeatherController:
    service = WeatherService()

    @staticmethod
    @router.get("/{location}", response=WeatherResponse)
    def get_weather(request: HttpRequest, location: str):
        return WeatherController.service.get_weather_information(location)
    
    @staticmethod
    @router.get("/search/{location}", response=SearchResponse)
    def search_location(request: HttpRequest, location: str):
        return WeatherController.service.search_location(location)
    
    @staticmethod
    @router.post("/register/send-code", response=bool)
    def send_mail(request: HttpRequest, payload: EmailSchema):
        return WeatherController.service.send_code(payload.email)
    
    @staticmethod
    @router.post("/register/verify-code", response=bool)
    def verify_code(request: HttpRequest, payload: EmailCodeSchema):
        return WeatherController.service.verify_code(payload.email, payload.code, type="register")
    
    @staticmethod
    @router.post("/unsubscribe/verify-code", response=bool)
    def unsubscribe(request: HttpRequest, payload: EmailCodeSchema):
        return WeatherController.service.verify_code(payload.email, payload.code, type="unsubscribe")
