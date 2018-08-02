from django.contrib import admin

# Register your models here.
from .models import Course, Enrollment, Announcement, Comment, Lesson, Material


# customizações do Admin
class CourseAdmin(admin.ModelAdmin):

    list_display = ['name', 'slug', 'start_date', 'create_at']
    search_fields = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

# TabularInline em linha ou em coluna StackedInline


class MaterialAdmin(admin.StackedInline):

    model = Material


class LessonAdmin(admin.ModelAdmin):

    list_display = ['name', 'number', 'course', 'release_date']
    search_fields = ['name', 'description']
    list_filter = ['create_at']

    inlines = [MaterialAdmin]


admin.site.register(Course, CourseAdmin)
admin.site.register([Enrollment, Announcement, Comment])
admin.site.register(Lesson, LessonAdmin)
