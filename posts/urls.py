from django.urls import path
from django.urls.conf import include
from rest_framework.routers import DefaultRouter
from .views import CommentViewSet, PostViewSet
from rest_framework.authtoken import views

router_v1 = DefaultRouter()

router_v1.register('posts', PostViewSet, basename='posts')
router_v1.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)

urlpatterns = [
    path('v1/api-token-auth/', views.obtain_auth_token),
    path('v1/', include(router_v1.urls)),
]
