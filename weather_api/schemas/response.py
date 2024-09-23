from ninja import Field, Schema
from typing import List

class LocationResponse(Schema):
    name: str = Field(description="Location Name")
    region: str = Field(description="Location Region")
    country: str = Field(description="Location Country")
    lat: float = Field(description="Location Latitude")
    lon: float = Field(description="Location Longitude")

class ConditionResponse(Schema):
    text: str = Field(description="Condition Text")
    icon: str = Field(description="Condition Icon")

class CurrentWeatherResponse(Schema):
    last_updated: str = Field(description="Last Date Updated")
    temp_c: float = Field(description="Temperature in Celsius")
    temp_f: float = Field(description="Temperature in Fahrenheit")
    condition: ConditionResponse = Field(default_factory = ConditionResponse, description="Condition")
    wind_mph: float = Field(description="Wind Speed in MPH")
    wind_kph: float = Field(description="Wind Speed in KPH")
    humidity: int = Field(description="Humidity")
    uv: float = Field(description="UV Index")

class ForecastInformationResponse(Schema):
    maxtemp_c: float = Field(description="Maximum Temperature in Celsius")
    maxtemp_f: float = Field(description="Maximum Temperature in Fahrenheit")
    mintemp_c: float = Field(description="Minimum Temperature in Celsius")
    mintemp_f: float = Field(description="Minimum Temperature in Fahrenheit")
    avgtemp_c: float = Field(description="Average Temperature in Celsius")
    avgtemp_f: float = Field(description="Average Temperature in Fahrenheit")
    maxwind_mph: float = Field(description="Maximum Wind Speed in MPH")
    maxwind_kph: float = Field(description="Maximum Wind Speed in KPH")
    avghumidity: int = Field(description="Average Humidity")
    condition: ConditionResponse = Field(default_factory = ConditionResponse, description="Condition")
    uv: float = Field(description="UV Index")

class ForecastWeatherResponse(Schema):
    date: str = Field(description="Date of Forecast")
    day: ForecastInformationResponse = Field(default_factory = ForecastInformationResponse, description="Day Forecast")

class ForecastResponse(Schema):
    forecastday: List[ForecastWeatherResponse] = Field(default_factory = list, description="Forecast Days")

class WeatherResponse(Schema):
    location: LocationResponse = Field(default_factory = LocationResponse, description="Location")
    current: CurrentWeatherResponse = Field(default_factory = CurrentWeatherResponse, description="Current Weather")
    forecast: ForecastResponse = Field(default_factory = ForecastResponse, description="Forecast Weather")

SearchResponse = List[LocationResponse]
