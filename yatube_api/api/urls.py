from django.urls import path, include
from rest_framework import routers

from api.views import CommentViewSet, FollowViewSet
from api.views import UserViewSet, GroupViewSet, PostViewSet
app_name = 'api'

router = routers.DefaultRouter('v1')
router.register('users', UserViewSet,
                basename='user')
router.register('groups', GroupViewSet,
                basename='group')
router.register('posts', PostViewSet,
                basename='post')
router.register(r'posts/(?P<post_id>[0-9]+)/comments',
                CommentViewSet, basename='comment')
router.register('follow', FollowViewSet,
                basename='follow')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls.jwt')),
]
