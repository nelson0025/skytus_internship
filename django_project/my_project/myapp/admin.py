from django.contrib import admin
from .models import student
from .models import cource
from .models import book

# Register your models here.
@admin.register(student)
class student_admin(admin.ModelAdmin):
        list_display=( 'id','name','age')
        search_fields = ('name', 'email')
        
@admin.register(cource)
class cource_admin(admin.ModelAdmin):
        list_display=('id','name')
        search_fields = ('name','id')

@admin.register(book)
class book_admin(admin.ModelAdmin):
        list_display=('id','name','title','price')
        search_fields=('id','name','title','price')
        list_filter=('id','name','title')

