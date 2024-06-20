import os
import json
from django.http import JsonResponse
from django.conf import settings
from rest_framework import generics
from rest_framework.views import APIView
from app.models import Teacher, Post, User
from app.serializers import TeacherSerializer, PostSerializer, UserSerializer


class GroupsLessonsView(APIView):
    def get(self, request):
        file_path = os.path.join(settings.BASE_DIR, 'data', 'students_week_lessons.json')
        with open(file_path, 'r') as file:
            data = json.load(file)
        return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})


class TeachersList(generics.ListAPIView):
    serializer_class = TeacherSerializer

    def get_queryset(self):
        return Teacher.objects.all().order_by('name')


class WeekTeachersLessonsView(APIView):
    def get(self, request, teacher):
        file_path = os.path.join(settings.BASE_DIR, 'data', 'teachers_week_lessons.json')
        with open(file_path, 'r') as file:
            data = json.load(file)
        for item in data:
            for key, value in item.items():
                if key.split(" ")[0] == teacher:
                    return JsonResponse(value, safe=False, json_dumps_params={'ensure_ascii': False})

        return JsonResponse([], safe=False, json_dumps_params={'ensure_ascii': False})


class PostsList(generics.ListAPIView):
    serializer_class = PostSerializer


    def get_queryset(self):
        return Post.objects.all().order_by('date_posted')


class UsersList(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    # def get_queryset(self):
    #     return Teacher.objects.all().order_by('name')