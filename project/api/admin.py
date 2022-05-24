from django.contrib import admin
from db.models import User


class ResetPasswordTokenAdmin(admin.ModelAdmin):
    list_display = ('user', 'key', 'created_at', 'ip_address', 'user_agent')
    
admin.site.register(User)
