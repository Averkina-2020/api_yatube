from django.urls import path
from django.urls.conf import include
from rest_framework.routers import DefaultRouter
from .views import CommentViewSet, PostViewSet
from rest_framework.authtoken import views

router = DefaultRouter()

router.register('posts', PostViewSet, basename='posts')
router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)

# !!! выполнить миграции !!!   python manage.py migrate

urlpatterns = [
    path('v1/api-token-auth/', views.obtain_auth_token),
    path('v1/', include(router.urls)),
]
