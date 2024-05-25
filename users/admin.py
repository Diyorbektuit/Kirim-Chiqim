from django.contrib import admin
from .models import TgUsers
# Register your models here.


class TgUsersAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'tg_id')
    search_fields = ('tg_id', 'username', 'first_name', 'last_name')


admin.site.register(TgUsers, TgUsersAdmin)