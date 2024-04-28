from django.contrib import admin

from .models import Student

# Register your models here.
# admin.site.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=('id','Name','Email','Contact','Add','Age')
admin.site.register(Student,StudentAdmin)
