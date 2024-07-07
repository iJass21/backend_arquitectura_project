from rest_framework import viewsets, status
from django.http import JsonResponse
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import User, Project, Comment, Like, ProjectMember, Reference, File, ProjectFile, Tag, ProjectTag
from .serializers import UserSerializer, ProjectSerializer, CommentSerializer, LikeSerializer, ProjectMemberSerializer, ReferenceSerializer, FileSerializer, ProjectFileSerializer, TagSerializer, ProjectTagSerializer
from api.services.file_service import FileService
from api.services.project_service import ProjectService
from api.services.comment_service import CommentsService
from api.services.tag_service import TagService
from api.services.project_tag_service import ProjectTagService
from rest_framework.exceptions import ValidationError



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
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

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
        
    @action(detail=True, methods=['get', 'post'])
    def comments(self, request, pk=None):
        if request.method == 'POST':
            try:
                comment = CommentsService.addComment(pk, request.data)
                serializer = CommentSerializer(comment)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'GET':
            try:
                comments = CommentsService.getComments(pk)
                serializer = CommentSerializer(comments, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


    @action(detail=True, methods=['post'])
    def deactivate(self, request, pk=None):
        project = ProjectService.deactivateProject(pk)
        serializer = ProjectSerializer(project)
        return Response(serializer.data)

    @action(detail=True, methods=['post', 'get'])
    def files(self, request, pk=None):
        if request.method == 'POST':
            file_serializer = ProjectFileSerializer(data=request.data)
            if file_serializer.is_valid():
                file = ProjectService.addFile(pk, file_serializer.validated_data, request.FILES['file'])
                file_serializer = ProjectFileSerializer(file)
                return Response(file_serializer.data, status=status.HTTP_201_CREATED)
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'GET':
            files = ProjectService.getProjectFiles(pk)
            serializer = ProjectFileSerializer(files, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)


    @action(detail=True, methods=['get', 'post'])
    def tags(self, request, pk=None):
        if request.method == 'POST':
            tag = ProjectTagService.add_project_tag(request.data)
            return Response(TagSerializer(tag).data, status=status.HTTP_201_CREATED)
        elif request.method == 'GET':   
            tags = ProjectService.getProjectTags(pk)
            return Response(ProjectTagSerializer(tags, many=True).data, status=status.HTTP_200_OK)


    @action(detail=False, methods=['get'])
    def projects_tags(self, request):
        projects_and_tags = ProjectService.getProjectsAndTags()
        return Response(projects_and_tags)

# Vista para cambiar contraseña
class ChangePasswordView(viewsets.ViewSet):
    @action(detail=False, methods=['post'])
    def change_password(self, request):
        # Implementa lógica de cambio de contraseña aquí
        pass

class TagViewSet(viewsets.ViewSet):
    def list(self, request):
        tags = TagService.get_all_tags()
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = TagSerializer(data=request.data)
        if serializer.is_valid():
            try:
                tag = TagService.add_tag(serializer.validated_data)
                return Response(TagSerializer(tag).data, status=status.HTTP_201_CREATED)
            except ValidationError as e:
                return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            TagService.delete_tag(pk)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Tag.DoesNotExist:
            return Response({"error": "Tag not found"}, status=status.HTTP_404_NOT_FOUND)