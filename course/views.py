from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from utils import mixins

from course import models, serializers, permissions, services


# Create your views here.



class CategoryViewSet(viewsets.ModelViewSet):
    course_services: services.CourseServicesInterface = services.CourseServicesV1()
    queryset = course_services.get_categories()
    serializer_class = serializers.CategorySerializer
    permission_classes = permissions.IsAdminOrReadOnly,


class TeacherViewSet(viewsets.ModelViewSet):
    course_services: services.CourseServicesInterface = services.CourseServicesV1()
    queryset = course_services.get_teachers()
    serializer_class = serializers.TeacherSerializer
    permission_classes = permissions.IsAdminOrReadOnly,


class CourseViewSet(mixins.ActionSerializerMixin, viewsets.ModelViewSet):
    ACTION_SERIALIZERS = {
        'retrieve': serializers.DetailCourseSerializer,
    }
    course_services: services.CourseServicesInterface = services.CourseServicesV1()
    queryset = course_services.get_courses()
    serializer_class = serializers.CourseSerializer
    permission_classes = permissions.IsAdminOrReadOnly,


class SectionViewSet(viewsets.ModelViewSet):
    course_services: services.CourseServicesInterface = services.CourseServicesV1()
    queryset = course_services.get_sections()
    serializer_class = serializers.SectionSerializer
    permission_classes = permissions.IsAdminOrReadOnly,


class LectureViewSet(viewsets.ModelViewSet):
    course_services: services.CourseServicesInterface = services.CourseServicesV1()
    queryset = course_services.get_lectures()
    serializer_class = serializers.LectureSerializer
    permission_classes = permissions.IsAdminOrReadOnly,


class PaidCourseViewSet(mixins.ActionSerializerMixin, viewsets.ModelViewSet):
    ACTION_SERIALIZERS = {
        'create': serializers.CreatePaidCourseSerializer,
        'retrieve': serializers.DetailPaidCourseSerializer,
    }
    permission_classes = IsAuthenticated,
    serializer_class = serializers.PaidCourseSerializer
    course_services: services.CourseServicesInterface = services.CourseServicesV1()
    queryset = models.PaidCourse.objects.all()

    def list(self, request, *args, **kwargs):
        courses = self.course_services.get_paid_courses(user=request.user)
        data = serializers.PaidCourseSerializer(courses, many=True).data
        return Response(data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        course = self.course_services.get_course(course_id=instance.id)
        serializer = serializers.DetailCourseSerializer(course)
        return Response(serializer.data)


class TaskViewSet(viewsets.ModelViewSet):
    course_services: services.CourseServicesInterface = services.CourseServicesV1()
    queryset = course_services.get_tasks()
    serializer_class = serializers.TaskSerializer
    permission_classes = permissions.IsAdminOrReadOnly,
