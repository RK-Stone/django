from django.contrib import admin

from students.models import student

# Register your models here.

class studentAdmin(admin.ModelAdmin):
	list_display = ("stdName", "stdID", "stdSex","stdBirth")
	#過濾器
	list_filter = ("stdName","stdSex")
	#查詢功能
	search_field = ("stdName","stdID")
	#排列順序
	ordering = ("id",)

admin.site.register(student, studentAdmin)