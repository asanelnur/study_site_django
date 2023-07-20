import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _

from course import choices


# Create your models here.


class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    title = models.CharField(max_length=255)
    desc = models.TextField()

    class Meta:
        ordering = ('title',)
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __str__(self):
        return self.title


class Teacher(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    level = models.CharField(
        max_length=10,
        choices=choices.LevelChoices.choices)
    work_at = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_at',)
        verbose_name = _('Teacher')
        verbose_name_plural = _('Teachers')

    def __str__(self):
        return self.first_name



class Course(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    title = models.CharField(max_length=255)
    desc = models.TextField()
    price = models.DecimalField(max_digits=12, decimal_places=2)
    is_top = models.BooleanField(default=False, verbose_name=_('Is top?'))
    is_active = models.BooleanField(default=True, verbose_name=_('Is active?'))
    syllabus = models.FileField(upload_to='files/', verbose_name=_('Syllabus'))
    category = models.ForeignKey(to=Category, on_delete=models.PROTECT, related_name='courses')
    teacher = models.ForeignKey(to=Teacher, on_delete=models.PROTECT, related_name='courses')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('is_top', '-created_at')
        verbose_name = _('Course')
        verbose_name_plural = _('Courses')

    def __str__(self):
        return self.title


class Section(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    title = models.CharField(max_length=255)
    course = models.ForeignKey(to=Course, on_delete=models.CASCADE, related_name='sections')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Lecture(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    title = models.CharField(max_length=255)
    video = models.FileField(upload_to='video/')
    duration = models.PositiveIntegerField(verbose_name=_('video duration'))
    section = models.ForeignKey(to=Section, on_delete=models.CASCADE, related_name='lectures')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Task(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='files/')
    section = models.ForeignKey(to=Section, on_delete=models.CASCADE, related_name='tasks')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
