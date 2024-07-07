# urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ProjectViewSet, UserRegisterView ,UserLoginView, CommentViewSet, LikeViewSet, ProjectMemberViewSet, ReferenceViewSet, ProjectFileViewSet, TagViewSet, ProjectTagViewSet, ChangePasswordView
from rest_framework_simplejwt.views import TokenRefreshView

router = DefaultRouter()
# router.register(r'users', UserViewSet, basename='user')
router.register(r'projects', ProjectViewSet, basename='project')
router.register(r'comments', CommentViewSet, basename='comment')
router.register(r'likes', LikeViewSet, basename='like')
router.register(r'project-members', ProjectMemberViewSet, basename='projectmember')
router.register(r'references', ReferenceViewSet, basename='reference')
router.register(r'files', ProjectFileViewSet, basename='file')
router.register(r'tags', TagViewSet, basename='tag')
router.register(r'project-tags', ProjectTagViewSet, basename='projecttag')

urlpatterns = [
    path('', include(router.urls)),
    path('users/register/', UserRegisterView.as_view({'post': 'register'})),
    path('users/login/', UserLoginView.as_view({'post': 'login'})),
    path('auth/change-password/', ChangePasswordView.as_view({'post': 'change_password'})),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
