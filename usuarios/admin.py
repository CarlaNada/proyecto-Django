from django.contrib import admin
from .models import UsuarioPersonalizado

# Register your models here.

admin.site.register(UsuarioPersonalizado)
class UsuarioAdmin (admin.ModelAdmin):
    list_display = ("id", "password", "last login", "is superuser", "username", "first name", "last name", "email", "is staff", "is active", "date joined", "telefono",)
    search_fields = ("username",)