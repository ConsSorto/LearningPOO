from django.contrib import admin
from person.models import Person

# Register your models here.
# @admin.register(Person)
# class PersonAdmin(admin.ModelAdmin):
#     pass

admin.site.register(Person)
