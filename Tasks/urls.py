from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, Registration
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register('tasks', TaskViewSet, basename='tasks')

urlpatterns = [
    path('register/', Registration.as_view()),
    path('login/', obtain_auth_token),
    path('', include(router.urls)),
]
