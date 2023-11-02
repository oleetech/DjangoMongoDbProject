from django.contrib import admin

from .models import MyModel
@admin.register(MyModel)
class MyModelAdminmodel(admin.ModelAdmin):
    pass






