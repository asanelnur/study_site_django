import uuid
from typing import Protocol

from django.db.models import QuerySet

from course import models, repos
from users.models import CustomUser


class CourseServicesInterface(Protocol):

    def get_categories(self) -> QuerySet[models.Category]: ...

    def get_teachers(self) -> QuerySet[models.Teacher]: ...

    def get_courses(self) -> QuerySet[models.Course]: ...

    def get_course(self, course_id: uuid.uuid4) -> models.Course: ...

    def get_sections(self) -> QuerySet[models.Section]: ...

    def get_lectures(self) -> QuerySet[models.Lecture]: ...

    def get_tasks(self) -> QuerySet[models.Task]: ...

    def get_paid_courses(self, user: CustomUser) -> QuerySet[models.PaidCourse]: ...


class CourseServicesV1:
    course_repos: repos.CourseReposInterface = repos.CourseReposV1()

    def get_categories(self) -> QuerySet[models.Category]:
        return self.course_repos.get_categories()

    def get_teachers(self) -> QuerySet[models.Teacher]:
        return self.course_repos.get_teachers()

    def get_courses(self) -> QuerySet[models.Course]:
        return self.course_repos.get_courses()

    def get_course(self, course_id: uuid.uuid4) -> models.Course:
        return self.course_repos.get_course(course_id=course_id)

    def get_sections(self) -> QuerySet[models.Section]:
        return self.course_repos.get_sections()

    def get_lectures(self) -> QuerySet[models.Lecture]:
        return self.course_repos.get_lectures()

    def get_tasks(self) -> QuerySet[models.Task]:
        return self.course_repos.get_tasks()

    def get_paid_courses(self, user: CustomUser) -> QuerySet[models.PaidCourse]:
        return self.course_repos.get_paid_courses(user=user)
