# api/services/project_service.py
from api.repositories.project_repository import ProjectRepository
from api.services.comment_service import CommentsService
from api.services.file_service import FileService
from api.models import Project, User

class ProjectService:
    @staticmethod
    def getAllProjects():
        return ProjectRepository.findAll()

    @staticmethod
    def createProject(projectData):
        owner_id = projectData.pop('owner')
        owner = User.objects.get(id=owner_id)
        projectData['owner'] = owner
        return ProjectRepository.create(projectData)

    @staticmethod
    def updateProject(projectId, projectData):
        if 'owner' in projectData:
            owner_id = projectData.pop('owner')
            owner = User.objects.get(id=owner_id)
            projectData['owner'] = owner
        return ProjectRepository.update(projectId, projectData)

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
    def addFile(projectId, fileData):
        return FileService.addFile(projectId, fileData)

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
