from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


# Register your models here.

class CustomAdmin(UserAdmin):
    list_display = ('email', 'date_joined', 'last_login')
    search_fields = ('email', 'username')
    readonly_fields = ('id', 'date_joined', 'last_login')

    filter_horizontal = ()


admin.site.register(CustomUser, CustomAdmin)
