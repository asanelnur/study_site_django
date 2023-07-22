# study_site_django

Basic info:
---
This site is intended for online programming shcools such us Decode, Extra or other. Shcools can sell courses on a suitable site by uploading their courses to the site with video and assignments. And students will be able to choose the course they need, make payment, watch video lectures, download assignments. 

The app is written in Django Python:

+ Using virtualenv
+ Clean Architecture
+ ModelViewSet, ViewSet
+ Router, API with versions
+ Permission Classes
+ Serializer, ModelSerializer
+ DjangoModel
+ Custom User
+ JWT authentication
+ Swagger
+ Django Cleanupp

</br>
</br>
</br>


# Explanation of the basic logic
---
Admins have permissions for all action. An Unauthorized users have permission for safety actions for categories, cources, teachers. 
<pre>
class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS or
            request.user
            and request.user.is_authenticated
            and request.user.is_staff
        )

Students who made the payment have permission for safety actions for all models. So they can watch lectures and do assignments.

Which student has access to which course is checked using this table and organized by serializers:
When student made payment, admins add her to this table:

class PaidCourse(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE, related_name='my_courses')
    course = models.ForeignKey(to=Course, on_delete=models.CASCADE, related_name='paid_course')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_at',)

class CourseViewSet(mixins.ActionSerializerMixin, viewsets.ModelViewSet):
    ACTION_SERIALIZERS = {
        'retrieve': serializers.DetailCourseSerializer,
    }
    course_services: services.CourseServicesInterface = services.CourseServicesV1()
    queryset = course_services.get_courses()
    serializer_class = serializers.CourseSerializer
    permission_classes = permissions.IsAdminOrReadOnly,
    
</pre>

# Database: SQLite
<b>SQLite</b> provides an excellent development alternative for applications that are predominantly read-only or require a smaller installation footprint. As with all database servers, though, there are some differences that are specific to SQLite that you should be aware of.

</br>
<pre> 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
</pre>

# To clone and run project
https://www.geeksforgeeks.org/clone-and-run-a-django-project-from-github/
