from django.contrib import admin
from .models import Kirimlar, Chiqimlar
# Register your models here.


class KirimlarAdmin(admin.ModelAdmin):
    list_display = ('user', "id", "name", "cost", "date")
    search_fields = ("name", )
    list_filter = ("user", "cost", "date")


class ChiqimlarAdmin(admin.ModelAdmin):
    list_display = ('user', "id", "name", "cost", "date")
    search_fields = ("name", )
    list_filter = ("user", "cost", "date")


admin.site.register(Kirimlar, KirimlarAdmin)
admin.site.register(Chiqimlar, ChiqimlarAdmin)
