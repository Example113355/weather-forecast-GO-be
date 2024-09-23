from django.contrib import admin

# Register your models here.
from .models import EmailCode, EmailLocation

admin.site.register(EmailCode)

admin.site.register(EmailLocation)
