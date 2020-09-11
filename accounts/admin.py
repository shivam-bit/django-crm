from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Customer)
admin.site.register(Products)
admin.site.register(order)
admin.site.register(tag)
admin.site.register(expected)
admin.site.register(testcase)