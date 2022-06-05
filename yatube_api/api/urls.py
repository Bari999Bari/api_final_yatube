from django.urls import path, include
from rest_framework import routers

from api.views import CommentViewSet, FollowViewSet
from api.views import UserViewSet, GroupViewSet, PostViewSet
app_name = 'api'

router_v1 = routers.DefaultRouter()
router_v1.register('users', UserViewSet,
                   basename='user')
router_v1.register('groups', GroupViewSet,
                   basename='group')
router_v1.register('posts', PostViewSet,
                   basename='post')
router_v1.register(r'posts/(?P<post_id>[0-9]+)/comments',
                   CommentViewSet, basename='comment')
router_v1.register('follow', FollowViewSet,
                   basename='follow')

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/', include('djoser.urls.jwt')),
]
