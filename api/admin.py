from django.contrib import admin

# Register your models here.
from .models import *


class UserAdmin(admin.ModelAdmin):
    exclude = ('groups', 'user_permissions')


admin.site.register(NPO, admin.ModelAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Opportunity, admin.ModelAdmin)
