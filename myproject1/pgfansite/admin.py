from django.contrib import admin

# Register your models here.

from .models import Thread,Response

admin.site.register(Thread)
admin.site.register(Response)