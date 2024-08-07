# api/services/project_service.py
from api.repositories.project_repository import ProjectRepository
from api.services.comment_service import CommentsService
from api.services.file_service import FileService
from api.models import Project, User, File, ProjectFile, ProjectTag, Tag
import uuid
from datetime import datetime
import os


class ProjectService:
    @staticmethod
    def getAllProjects():
        return ProjectRepository.findAll()

    @staticmethod
    def createProject(projectData):
        tags = projectData.pop('project_tags', [])
        project = ProjectRepository.create(projectData)
        ProjectService._update_project_tags(project, tags)
        return project

    @staticmethod
    def updateProject(projectId, projectData):
        tags = projectData.pop('project_tags', [])
        project = ProjectRepository.update(projectId, projectData)
        ProjectService._update_project_tags(project, tags)
        return project

    @staticmethod
    def deleteProject(projectId):
        ProjectRepository.delete(projectId)

    @staticmethod
    def deactivateProject(projectId):
        return ProjectRepository.deactivate(projectId)

    @staticmethod
    def addComment(projectId, commentData):
        return CommentsService.addComment(projectId, commentData)

    @staticmethod
    def addFile(project_id, validated_data, uploaded_file):
        project = Project.objects.get(pk=project_id)
        
        # Generar un nombre aleatorio para el archivo con la fecha de subida
        current_date = datetime.now().strftime("%Y%m%d")
        random_filename = f"{uuid.uuid4().hex}_{current_date}{os.path.splitext(uploaded_file.name)[1]}"
        
        # Definir la ruta relativa y absoluta para guardar el archivo
        relative_path = os.path.join('projects/files/', random_filename)
        absolute_path = os.path.join('media/', relative_path)
        
        # Guardar el archivo en el modelo File con la ruta relativa
        file_instance = File.objects.create(route=relative_path, active=True)
        
        # Guardar el archivo físicamente en el sistema de archivos
        os.makedirs(os.path.dirname(absolute_path), exist_ok=True)  # Crear directorios si no existen
        with open(absolute_path, 'wb+') as destination:
            for chunk in uploaded_file.chunks():
                destination.write(chunk)
        
        # Crear la asociación en ProjectFile
        project_file = ProjectFile.objects.create(
            project=project,
            file=file_instance,
            title=validated_data['title'],
            description=validated_data['description'],
            active=True
        )
        return project_file
    @staticmethod
    def getProjectFiles(projectId):
        return FileService.getProjectFiles(projectId)

    @staticmethod
    def getProjectTags(projectId):
        project = ProjectRepository.findById(projectId)
        return project.project_tags.all()

    @staticmethod
    def getProjectsAndTags():
        projects = ProjectRepository.findAll()
        return [(project, project.project_tags.all()) for project in projects]
        
    @staticmethod
    def getProjectById(projectId):
        return ProjectRepository.findById(projectId)

    @staticmethod
    def _update_project_tags(project, tags):
        ProjectTag.objects.filter(project=project).delete()
        for tag_id in tags:
            tag = Tag.objects.get(id=tag_id)
            ProjectTag.objects.create(project=project, tag=tag)
