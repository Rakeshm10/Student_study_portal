from django.contrib import admin
from . models import *
from django import forms


# Register your models here.

admin.site.register(Notes)
admin.site.register(Assignment)

admin.site.register(Todo)   


admin.site.register(Room)
admin.site.register(Message)


