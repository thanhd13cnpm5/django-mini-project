from django.contrib import admin
from .models import Staff,Student,FeedBackStaff,FeedBackStudent,NotificationStaff,NotificationStudent


admin.site.register(Student)
admin.site.register(Staff)
admin.site.register(FeedBackStudent)
admin.site.register(FeedBackStaff)
admin.site.register(NotificationStaff)
admin.site.register(NotificationStudent)