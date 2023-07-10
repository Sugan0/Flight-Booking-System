from multiprocessing.connection import Client
from django.contrib import admin
from .models import Flight,Reserve, User, Voyage
# Register your models here.
admin.site.register(User)
admin.site.register(Voyage)
admin.site.register(Flight)
admin.site.register(Reserve)

