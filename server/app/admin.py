from django.contrib import admin

from app.models import Teacher, Post, User

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ("name",)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title",)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("email",)