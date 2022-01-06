from django.contrib import admin
from .models import Post
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_at', 'updated_at')
    list_filter = ['status','created_at',]
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}
    
# Register your models here.
admin.site.register(Post,PostAdmin)