import uuid
from typing import Protocol

from django.db.models import QuerySet

from course import models
from users.models import CustomUser


class CourseReposInterface(Protocol):

    @staticmethod
    def get_categories() -> QuerySet[models.Category]: ...

    @staticmethod
    def get_teachers() -> QuerySet[models.Teacher]: ...

    @staticmethod
    def get_courses() -> QuerySet[models.Course]: ...

    @staticmethod
    def get_course(course_id: uuid.uuid4) -> models.Course: ...

    @staticmethod
    def get_sections() -> QuerySet[models.Section]: ...

    @staticmethod
    def get_lectures() -> QuerySet[models.Lecture]: ...

    @staticmethod
    def get_tasks() -> QuerySet[models.Task]: ...

    @staticmethod
    def get_paid_courses(user: CustomUser) -> QuerySet[models.PaidCourse]: ...



class CourseReposV1:

    @staticmethod
    def get_categories() -> QuerySet[models.Category]:
        return models.Category.objects.all().prefetch_related('courses', 'courses__teacher')

    @staticmethod
    def get_teachers() -> QuerySet[models.Teacher]:
        return models.Teacher.objects.all()

    @staticmethod
    def get_courses() -> QuerySet[models.Course]:
        return models.Course.objects.all().select_related('teacher')

    @staticmethod
    def get_course(course_id: uuid.uuid4) -> models.Course:
        return models.Course.objects.get(id=course_id)
    
    @staticmethod
    def get_sections() -> QuerySet[models.Section]:
        return models.Section.objects.all().prefetch_related('lectures', 'tasks')

    @staticmethod
    def get_lectures() -> QuerySet[models.Lecture]:
        return models.Lecture.objects.all()

    @staticmethod
    def get_tasks() -> QuerySet[models.Task]:
        return models.Task.objects.all()

    @staticmethod
    def get_paid_courses(user: CustomUser) -> QuerySet[models.PaidCourse]:
        return models.PaidCourse.objects.filter(user=user)
