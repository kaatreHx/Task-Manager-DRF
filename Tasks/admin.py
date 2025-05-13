from django.contrib import admin
from .models import Task

# Register your models here.
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'status', 'created_at', 'user')
    search_fields = ('title', 'description')
    list_filter = ('status',)
    ordering = ('-created_at',)
    list_per_page = 10