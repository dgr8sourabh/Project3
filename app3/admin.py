from django.contrib import admin
from app3.models import EmployeeModel


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['idno','name','salary','city']


admin.site.register(EmployeeModel, EmployeeAdmin)

