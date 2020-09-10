from django.contrib import admin

# Register your models here.
from .models import Course, LectureSession

class LectureInline(admin.StackedInline):
    model = LectureSession
    extra = 3

class CourseAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Course Information', {'fields': ['course_name', 'course_description']}),
    ]
    inlines = [LectureInline]

admin.site.register(Course, CourseAdmin)
admin.site.register(LectureSession)