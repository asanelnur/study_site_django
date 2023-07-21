from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

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
        'retrieve': serializers.DetailCourseSerializer,
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


class PaidCourseViewSet(mixins.ActionSerializerMixin, viewsets.ModelViewSet):
    ACTION_SERIALIZERS = {
        'create': serializers.CreatePaidCourseSerializer,
        'retrieve': serializers.DetailPaidCourseSerializer,
    }
    permission_classes = IsAuthenticated,
    serializer_class = serializers.PaidCourseSerializer
    queryset = models.PaidCourse.objects.all()

    def list(self, request, *args, **kwargs):
        courses = models.PaidCourse.objects.filter(user=request.user)
        data = serializers.PaidCourseSerializer(courses, many=True).data
        return Response(data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        course = models.Course.objects.get(id=instance.course.id)
        serializer = serializers.DetailCourseSerializer(course)
        return Response(serializer.data)


class TaskViewSet(viewsets.ModelViewSet):
    queryset = models.Task.objects.all()
    serializer_class = serializers.TaskSerializer
    permission_classes = permissions.IsAdminOrReadOnly,
