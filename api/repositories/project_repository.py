# api/repositories/project_repository.py
from api.models import Project

class ProjectRepository:
    @staticmethod
    def findAll():
        return Project.objects.all()

    @staticmethod
    def create(projectData):
        return Project.objects.create(**projectData)

    @staticmethod
    def update(projectId, projectData):
        project = Project.objects.get(id=projectId)
        for key, value in projectData.items():
            setattr(project, key, value)
        project.save()
        return project

    @staticmethod
    def delete(projectId):
        project = Project.objects.get(id=projectId)
        project.delete()

    @staticmethod
    def deactivate(projectId):
        project = Project.objects.get(id=projectId)
        project.active = False
        project.save()
        return project

    @staticmethod
    def findById(projectId):
        return Project.objects.get(id=projectId)
