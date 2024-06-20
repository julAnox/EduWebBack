from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import GroupsLessonsView, TeachersList, WeekTeachersLessonsView, PostsList, UsersList

urlpatterns = [
    path('get_groups_data/', GroupsLessonsView.as_view()),

    path('get_teachers/', TeachersList.as_view()),
    path('get_week_data_by_teacher/<str:teacher>', WeekTeachersLessonsView.as_view()),
    path('posts/', PostsList.as_view()),

    path('users/', UsersList.as_view()),
]
