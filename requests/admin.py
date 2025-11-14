from django.contrib import admin
from . import models

admin.site.register(models.Contact)
admin.site.register(models.Course)
admin.site.register(models.Request)
admin.site.register(models.Feedback)
