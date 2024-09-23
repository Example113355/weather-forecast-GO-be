from django.db import models
from ..exceptions import EmailCodeNotFound

class EmailCode(models.Model):
    email = models.EmailField()
    code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True, null=False, blank=False)

    class Meta:
        unique_together = ['email', 'code']

    def __str__(self):
        return f"{self.email} - {self.code}"
    
    @staticmethod
    def get_email_code(email: str):
        try:
            return EmailCode.objects.get(email=email)
        except EmailCode.DoesNotExist:
            raise EmailCodeNotFound()
        
class EmailLocation(models.Model):
    email = models.EmailField()
    location = models.CharField(max_length=255)

    class Meta:
        unique_together = ['email', 'location']

    def __str__(self):
        return f"{self.email} - {self.location}"
    
    @staticmethod
    def get_locations_by_email(email: str):
        return EmailLocation.objects.filter(email=email)
