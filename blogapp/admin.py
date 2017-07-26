from django.contrib import admin
from blogapp.models import Blogpost


# Register your models here.
class BlogpostAdmin(admin.ModelAdmin):
    exclude = ['posted', ]
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Blogpost, BlogpostAdmin)
