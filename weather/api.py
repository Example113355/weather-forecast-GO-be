from ninja import NinjaAPI
from weather_api.api import router as weather_router
from exceptions.base import BaseException
from django.http import HttpRequest

api = NinjaAPI()

api.add_router("/weather", weather_router)

@api.exception_handler(BaseException)
def weather_exception_handler(request: HttpRequest, exc: BaseException):
    return api.create_response(request, exc.get_response(), status=200)
