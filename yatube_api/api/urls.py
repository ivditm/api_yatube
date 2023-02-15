from rest_framework.routers import DefaultRouter

from django.urls import include, path

from api.views import CommentViewSet, GroupViewSet, PostViewSet

from rest_framework.authtoken import views


router_v1 = DefaultRouter()

router_v1.register('comments', CommentViewSet, basename='comments')
router_v1.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet,
                   basename='comment')
router_v1.register('groups', GroupViewSet)
router_v1.register('posts', PostViewSet, basename='posts')

urlpatterns = [
    path('', include(router_v1.urls)),
    path('api-token-auth/', views.obtain_auth_token),
]
