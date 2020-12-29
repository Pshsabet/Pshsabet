from django.contrib import admin
from . import models
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'publish', 'updated', 'status')
    list_filter = ('publish', 'status')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['-publish', 'status']
    

admin.site.register(models.post, PostAdmin)