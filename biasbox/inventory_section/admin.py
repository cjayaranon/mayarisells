from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import *

class UsersAdminPage(UserAdmin):
    list_display = ('username', 'id', 'email', 'first_name', 'last_name', 'is_staff')

admin.site.unregister(User)
admin.site.register(User, UsersAdminPage)
admin.site.register(Product_Category)
admin.site.register(Location)
admin.site.register(Store)
admin.site.register(Merch)
admin.site.register(Inventory)