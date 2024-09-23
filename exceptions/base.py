class BaseException(Exception):
    error_code = 500
    message_code = "INTERNAL_SERVER_ERROR"
    message = "Internal server error"

    def get_response(self):
        return {
            "message_code": self.message_code,
            "message": self.message,
            "error_code": self.error_code,
        }
