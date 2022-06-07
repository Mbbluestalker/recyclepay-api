from db.models import Category, Order, User
from django.contrib import admin


class PickupAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'location', 'weight_in_kg', 'status', 'requested_by')


admin.site.register(Order, PickupAdmin)
admin.site.register(Category)


class ResetPasswordTokenAdmin(admin.ModelAdmin):
    list_display = ('user', 'key', 'created_at', 'ip_address', 'user_agent')


admin.site.register(User)
