from django.urls import path

from users import views

urlpatterns = [
    path('users/', views.UserViewSet.as_view({'post': 'create_user', 'get': 'get_user'})),
]
