from django.contrib import admin
from .models import sentiment, attrition_upload

# Register your models here.
admin.site.register(sentiment)
admin.site.register(attrition_upload)