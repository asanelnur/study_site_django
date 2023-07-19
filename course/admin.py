from django.contrib import admin

from course import models

# Register your models here.

admin.site.register(models.Category)
admin.site.register(models.Course)
admin.site.register(models.Section)
admin.site.register(models.Lecture)
admin.site.register(models.Task)
admin.site.register(models.Teacher)

