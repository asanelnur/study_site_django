from django.shortcuts import render
from rest_framework import viewsets
from utils import mixins

from course import models, serializers, permissions


# Create your views here.



class CategoryViewSet(viewsets.ModelViewSet):
    queryset = models.Category.objects.all().prefetch_related('courses', 'courses__teacher')
    serializer_class = serializers.CategorySerializer
    permission_classes = permissions.IsAdminOrReadOnly,


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = models.Teacher.objects.all()
    serializer_class = serializers.TeacherSerializer
    permission_classes = permissions.IsAdminOrReadOnly,


class CourseViewSet(mixins.ActionSerializerMixin, viewsets.ModelViewSet):
    ACTION_SERIALIZERS = {
        'retrieve': serializers.RetrieveCourseSerializer,
    }
    queryset = models.Course.objects.all().select_related('teacher')
    serializer_class = serializers.CourseSerializer
    permission_classes = permissions.IsAdminOrReadOnly,


class SectionViewSet(viewsets.ModelViewSet):
    queryset = models.Section.objects.all().prefetch_related('lectures', 'tasks')
    serializer_class = serializers.SectionSerializer
    permission_classes = permissions.IsAdminOrReadOnly,


class LectureViewSet(viewsets.ModelViewSet):
    queryset = models.Lecture.objects.all()
    serializer_class = serializers.LectureSerializer
    permission_classes = permissions.IsAdminOrReadOnly,



class TaskViewSet(viewsets.ModelViewSet):
    queryset = models.Task.objects.all()
    serializer_class = serializers.TaskSerializer
    permission_classes = permissions.IsAdminOrReadOnly,
