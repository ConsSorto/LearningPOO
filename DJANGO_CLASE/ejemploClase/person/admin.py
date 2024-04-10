from django.contrib import admin
from person.models import Person
# Register your models here.
# admin.site.register(Person)
@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('firstName', 'lastName', 'created_at', 'updated_at')
    search_fields = ('firstName',)
    list_filter = ('created_at', 'updated_at')