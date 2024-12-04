from django.contrib import admin
from .models import PersonalInfo

@admin.register(PersonalInfo)
class PersonalInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'profession', 'bio')
