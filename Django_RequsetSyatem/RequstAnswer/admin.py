from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.RequestInfo)
admin.site.register(models.RequestTargetInfo)
