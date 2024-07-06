from rest_framework import viewsets, status
from django.http import JsonResponse
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import User, Project, Comment, Like, ProjectMember, Reference, File, ProjectFile, Tag, ProjectTag
from .serializers import UserSerializer, ProjectSerializer, CommentSerializer, LikeSerializer, ProjectMemberSerializer, ReferenceSerializer, FileSerializer, ProjectFileSerializer, TagSerializer, ProjectTagSerializer
from api.services.file_service import FileService
from api.services.project_service import ProjectService
from api.services.comment_service import CommentsService


def health_check(request):
    return JsonResponse({"status": "ok"})

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

class ProjectMemberViewSet(viewsets.ModelViewSet):
    queryset = ProjectMember.objects.all()
    serializer_class = ProjectMemberSerializer

class ReferenceViewSet(viewsets.ModelViewSet):
    queryset = Reference.objects.all()
    serializer_class = ReferenceSerializer



class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class ProjectTagViewSet(viewsets.ModelViewSet):
    queryset = ProjectTag.objects.all()
    serializer_class = ProjectTagSerializer

# Vista para registrar usuario
class UserRegisterView(viewsets.ViewSet):
    @action(detail=False, methods=['post'])
    def register(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Vista para login de usuario (puede necesitar implementación específica dependiendo del sistema de autenticación)
class UserLoginView(viewsets.ViewSet):
    @action(detail=False, methods=['post'])
    def login(self, request):
        # Implementa lógica de login aquí
        pass
class CommentViewSet(viewsets.ViewSet):
    def create(self, request):
        comment = CommentsService.addComment(request.data['project'], request.data)
        serializer = CommentSerializer(comment)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        comment = CommentsService.updateComment(pk, request.data)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        CommentsService.deleteComment(pk)
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=True, methods=['post'])
    def deactivate(self, request, pk=None):
        comment = CommentsService.deactivateComment(pk)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

class ProjectFileViewSet(viewsets.ViewSet):
    def retrieve(self, request, pk=None):
        file = FileService.getFile(pk)
        serializer = ProjectFileSerializer(file)
        return Response(serializer.data)

    def create(self, request):
        file = FileService.uploadFile(request.data)
        serializer = ProjectFileSerializer(file)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def destroy(self, request, pk=None):
        FileService.deleteFile(pk)
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=True, methods=['post'])
    def deactivate(self, request, pk=None):
        file = FileService.deactivateFile(pk)
        serializer = ProjectFileSerializer(file)
        return Response(serializer.data)

class ProjectViewSet(viewsets.ViewSet):
    def list(self, request):
        projects = ProjectService.getAllProjects()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

    def create(self, request):
        project = ProjectService.createProject(request.data)
        serializer = ProjectSerializer(project)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        project = ProjectService.updateProject(pk, request.data)
        serializer = ProjectSerializer(project)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        ProjectService.deleteProject(pk)
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def retrieve(self, request, pk=None):
        try:
            project = ProjectService.getProjectById(pk)
            serializer = ProjectSerializer(project)
            return Response(serializer.data)
        except Project.DoesNotExist:
            return Response({"error": "Project not found"}, status=status.HTTP_404_NOT_FOUND)


    @action(detail=True, methods=['post'])
    def deactivate(self, request, pk=None):
        project = ProjectService.deactivateProject(pk)
        serializer = ProjectSerializer(project)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def add_comment(self, request, pk=None):
        comment = ProjectService.addComment(pk, request.data)
        return Response(comment, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['post'])
    def add_file(self, request, pk=None):
        file = ProjectService.addFile(pk, request.data)
        return Response(file, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['get'])
    def tags(self, request, pk=None):
        tags = ProjectService.getProjectTags(pk)
        return Response(tags)

    @action(detail=False, methods=['get'])
    def projects_and_tags(self, request):
        projects_and_tags = ProjectService.getProjectsAndTags()
        return Response(projects_and_tags)

# Vista para cambiar contraseña
class ChangePasswordView(viewsets.ViewSet):
    @action(detail=False, methods=['post'])
    def change_password(self, request):
        # Implementa lógica de cambio de contraseña aquí
        pass

# Vista para Tags
class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer