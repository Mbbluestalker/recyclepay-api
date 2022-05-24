from db.models import User
from django.contrib import admin
from django_rest_passwordreset.models import ResetPasswordToken


class ResetPasswordTokenAdmin(admin.ModelAdmin):
    list_display = ('user', 'key', 'created_at', 'ip_address', 'user_agent')

admin.site.register(User)
