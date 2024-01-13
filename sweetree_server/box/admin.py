from django.contrib import admin
from .models import Box


@admin.register(Box)
class BoxAdmin(admin.ModelAdmin):
    pass
