from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ProjectViewSet, CommentViewSet, LikeViewSet, ProjectMemberViewSet, ReferenceViewSet, FileViewSet, ProjectFileViewSet, TagViewSet, ProjectTagViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'likes', LikeViewSet)
router.register(r'project-members', ProjectMemberViewSet)
router.register(r'references', ReferenceViewSet)
router.register(r'files', FileViewSet)
router.register(r'project-files', ProjectFileViewSet)
router.register(r'tags', TagViewSet)
router.register(r'project-tags', ProjectTagViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
