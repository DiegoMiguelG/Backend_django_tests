
#Django
from django.contrib import admin

#Models
from users.models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass