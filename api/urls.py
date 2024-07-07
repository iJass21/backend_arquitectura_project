from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ProjectViewSet, CommentViewSet, LikeViewSet, ProjectMemberViewSet, ReferenceViewSet, ProjectFileViewSet, TagViewSet, ProjectTagViewSet, UserRegisterView, UserLoginView, ChangePasswordView

router = DefaultRouter()
router.register(r'users', UserViewSet)
# router.register(r'projects', ProjectViewSet)
# router.register(r'comments', CommentViewSet)
router.register(r'likes', LikeViewSet)
router.register(r'project-members', ProjectMemberViewSet)
router.register(r'references', ReferenceViewSet)
# router.register(r'files', FileViewSet)
# router.register(r'project-files', ProjectFileViewSet)
router.register(r'tags', TagViewSet)
router.register(r'project-tags', ProjectTagViewSet)


# router = DefaultRouter()
router.register(r'projects', ProjectViewSet, basename='project')
router.register(r'files', ProjectFileViewSet, basename='file')
router.register(r'comments', CommentViewSet, basename='comment')

# urlpatterns = [
#     path('', include(router.urls)),
# ]

urlpatterns = [
    path('', include(router.urls)),
    path('users/register/', UserRegisterView.as_view({'post': 'register'})),
    path('users/login/', UserLoginView.as_view({'post': 'login'})),
    path('auth/change-password/', ChangePasswordView.as_view({'post': 'change_password'})),
    path('users/', UserViewSet.get_all_users, name='get_all_users'),
    path('users/create/', UserViewSet.create_user, name='create_user'),
    path('users/update/<int:user_id>/', UserViewSet.update_user, name='update_user'),
    path('users/delete/<int:user_id>/', UserViewSet.delete_user, name='delete_user'),
    path('users/login/', UserViewSet.login_user, name='login_user'),
    path('users/change-password/<int:user_id>/', UserViewSet.change_password, name='change_password'),
]