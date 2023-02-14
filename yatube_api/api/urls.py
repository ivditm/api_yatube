from rest_framework.routers import DefaultRouter

from django.urls import include, path

from api.views import CommentViewSet, GroupViewSet, PostViewSet

from rest_framework.authtoken import views


router = DefaultRouter()

router.register('comments', CommentViewSet)
router.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet,
                basename='comment')
router.register('groups', GroupViewSet)
router.register('posts', PostViewSet, basename='posts')

urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token),
]
