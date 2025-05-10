from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_nested.routers import NestedDefaultRouter
from .views import *

router = DefaultRouter()
router.register('categories', CategoryViewSet)
router.register('posts', PostViewSet)

post_router = NestedDefaultRouter(router, 'posts', lookup='post')
post_router.register('comments', CommentViewSet, basename='post-comments')

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/', include(post_router.urls)),
    path('api/register/', RegisterView.as_view()),
    path('api/login/', obtain_auth_token),
]