from rest_framework.routers import DefaultRouter

from course import views

router = DefaultRouter()
router.register(r'category', views.CategoryViewSet)
router.register(r'teacher', views.TeacherViewSet)
router.register(r'course', views.CourseViewSet)
router.register(r'section', views.SectionViewSet)
router.register(r'lecture', views.LectureViewSet)
router.register(r'task', views.TaskViewSet)
router.register(r'paid-course', views.PaidCourseViewSet, basename='paid_course')

urlpatterns = router.urls
