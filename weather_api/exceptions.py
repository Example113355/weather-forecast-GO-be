from http import HTTPStatus
from exceptions.base import BaseException
    
class LocationMissing(BaseException):
    error_code = HTTPStatus.BAD_REQUEST
    message_code = "LOCATION_MISSING"
    message = "Location missing"

class LocationNotFound(BaseException):
    error_code = HTTPStatus.NOT_FOUND
    message_code = "LOCATION_NOT_FOUND"
    message = "Location not found"

class ExternalAPIError(BaseException):
    error_code = HTTPStatus.INTERNAL_SERVER_ERROR
    message_code = "EXTERNAL_API_ERROR"
    message = "External API error"

class EmailCodeNotFound(BaseException):
    error_code = HTTPStatus.NOT_FOUND
    message_code = "EMAIL_CODE_NOT_FOUND"
    message = "Email code not found"

class EmailServiceError(BaseException):
    error_code = HTTPStatus.INTERNAL_SERVER_ERROR
    message_code = "EMAIL_SERVICE_ERROR"
    message = "Email service error"

class EmailCodeNotMatch(BaseException):
    error_code = HTTPStatus.BAD_REQUEST
    message_code = "EMAIL_CODE_NOT_MATCH"
    message = "Email code not match"
