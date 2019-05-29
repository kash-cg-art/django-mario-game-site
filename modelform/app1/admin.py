from django.contrib import admin

# Register your models here.
from app1.models import feedback,mail

admin.site.register(feedback)
admin.site.register(mail)
