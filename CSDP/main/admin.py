# Register your models here.
from django.contrib import admin
from main.models import Meeting, ToDo, EventGallery


admin.site.register(Meeting)
admin.site.register(ToDo)
admin.site.register(EventGallery)