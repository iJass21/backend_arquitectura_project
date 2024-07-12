# urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FileViewSet, ProjectViewSet, UserLoginView, UserRegisterView, CommentViewSet, LikeViewSet, ProjectMemberViewSet, ReferenceViewSet, ProjectFileViewSet, TagViewSet, ProjectTagViewSet, ChangePasswordView, UserViewSet
from rest_framework_simplejwt.views import TokenRefreshView

router = DefaultRouter()
# router.register(r'users', UserViewSet, basename='user')
router.register(r'projects', ProjectViewSet, basename='project')
router.register(r'comments', CommentViewSet, basename='comment')
router.register(r'likes', LikeViewSet, basename='like')
router.register(r'project-members', ProjectMemberViewSet, basename='projectmember')
router.register(r'references', ReferenceViewSet, basename='reference')
router.register(r'files', ProjectFileViewSet, basename='file')
router.register(r'files-upload', FileViewSet, basename='file-upload')
router.register(r'tags', TagViewSet, basename='tag')
router.register(r'project-tags', ProjectTagViewSet, basename='projecttag')
router.register(r'users', UserViewSet, basename='user')


urlpatterns = [
    path('', include(router.urls)),
    path('users/register/', UserRegisterView.as_view({'post': 'register'})),
    path('users/login/', UserLoginView.as_view({'post': 'login'})),
    path('auth/change-password/', ChangePasswordView.as_view({'post': 'change_password'})),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('projects/<int:project>/members/', ProjectMemberViewSet.as_view({
        'get': 'list',
        'post': 'create'
    }), name='project-members-list'),
    path('project-members/<int:id>/', ProjectMemberViewSet.as_view({
        'delete': 'destroy',
    }), name='project-member-detail'),


    # path('users/', UserViewSet.get_all_users, name='get_all_users'),
    # path('users/create/', UserViewSet.create_user, name='create_user'),
    # path('users/update/<int:user_id>/', UserViewSet.update_user, name='update_user'),
    # path('users/delete/<int:user_id>/', UserViewSet.delete_user, name='delete_user'),
    # path('users/login/', UserViewSet.login_user, name='login_user'),
    # path('users/change-password/<int:user_id>/', UserViewSet.change_password, name='change_password'),
]
