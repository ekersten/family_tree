from django.contrib import admin
from . import models


# Register your models here.
class PersonAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'middle_name', 'last_name', 'nickname', 'birth_date', 'birth_city', 'birth_country', 'death_date')
    list_filter = ('birth_country',)
    date_hierarchy = 'birth_date'


class CoupleAdmin(admin.ModelAdmin):
    list_display = ('father', 'mother', 'start_date', 'end_date')

admin.site.register(models.Person, PersonAdmin)
admin.site.register(models.Couple, CoupleAdmin)