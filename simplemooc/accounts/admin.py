from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'last_login', 'is_superuser', 'is_staff']
    search_fields = ['name', 'email']
    list_filter = ['date_joined']


admin.site.register(User, UserAdmin)
