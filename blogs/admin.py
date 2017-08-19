from django.contrib import admin
from .models import Category, Blog

class AuthorAdmin(admin.ModelAdmin):
    #date_hierarchy = 'posted'   
    list_display =['title','posted']
    #fields = ('title','posted')

admin.site.register(Category)
admin.site.register(Blog,AuthorAdmin)


#list_display = ['title', 'status']

