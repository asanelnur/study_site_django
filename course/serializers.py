from rest_framework import serializers

import users.models
from course import models


class TeacherSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Teacher
        fields = '__all__'


class _TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Teacher
        fields = ('first_name', 'last_name', 'level', 'work_at')


class CourseSerializer(serializers.ModelSerializer):
    teacher = _TeacherSerializer(read_only=True)

    class Meta:
        model = models.Course
        fields = '__all__'


class _CourseSerializer(serializers.ModelSerializer):
    teacher = _TeacherSerializer(read_only=True)

    class Meta:
        model = models.Course
        fields = ('title', 'desc', 'price', 'teacher')


class CategorySerializer(serializers.ModelSerializer):
    courses = _CourseSerializer(many=True, read_only=True)

    class Meta:
        model = models.Category
        fields = '__all__'




class LectureSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Lecture
        fields = ('title', 'video', 'duration')


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Task
        fields = ('title', 'file')



class SectionSerializer(serializers.ModelSerializer):
    lectures = LectureSerializer(many=True, read_only=True)
    tasks = TaskSerializer(many=True, read_only=True)

    class Meta:
        model = models.Section
        fields = '__all__'


class _SectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Section
        fields = ('id', 'title',)


class DetailCourseSerializer(serializers.ModelSerializer):
    teacher = _TeacherSerializer(read_only=True)
    sections = _SectionSerializer(many=True, read_only=True)

    class Meta:
        model = models.Course
        fields = '__all__'


class CreatePaidCourseSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = models.PaidCourse
        fields = ('course', 'user')


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = users.models.CustomUser
        fields = ('username',)


class PaidCourseSerializer(serializers.ModelSerializer):
    course = CourseSerializer()

    class Meta:
        model = models.PaidCourse
        fields = ('course',)


class DetailPaidCourseSerializer(serializers.ModelSerializer):
    teacher = _TeacherSerializer(read_only=True)
    sections = _SectionSerializer(many=True, read_only=True)

    class Meta:
        model = models.PaidCourse
        fields = '__all__'