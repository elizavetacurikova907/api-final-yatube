from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

router = DefaultRouter()
router.register('v1/posts', PostViewSet)
router.register('v1/follow', FollowViewSet)
router.register('v1/groups', GroupViewSet)
router.register(r'v1/posts/(?P<post_id>\d+)/comments', CommentViewSet)

app_name = 'api'

urlpatterns = [
    path('v1/', include('djoser.urls.jwt')),
    path('', include(router.urls))
] 
