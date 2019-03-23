from django.contrib import admin

from .models import Todo


class TodoAdmin(admin.ModelAdmin):
    pass


admin.site.register(Todo, TodoAdmin)
