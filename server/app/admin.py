from django.contrib import admin

from app.models import Teacher, Post

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ("name",)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title",)