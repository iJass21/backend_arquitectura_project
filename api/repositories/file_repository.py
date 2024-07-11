# api/repositories/file_repository.py
from api.models import ProjectFile, File
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

class FileRepository:
    @staticmethod
    def findById(fileId):
        return ProjectFile.objects.get(id=fileId)

    @staticmethod
    def findByProjectId(projectId):
        return ProjectFile.objects.filter(project_id=projectId)

    @staticmethod
    def create(fileData, fileContent):
        file_path = default_storage.save(fileContent.name, ContentFile(fileContent.read()))
        file_instance = File.objects.create(route=file_path, active=True)
        project_file_data = {
            'project': fileData['project'],
            'file': file_instance,
            'title': fileData['title'],
            'description': fileData.get('description', ''),
            'active': True
        }
        return ProjectFile.objects.create(**project_file_data)
    
    @staticmethod
    def delete(fileId):
        project_file = ProjectFile.objects.get(id=fileId)
        file_instance = project_file.file
        file_instance.delete()
        project_file.delete()

    @staticmethod
    def deactivate(fileId):
        project_file = ProjectFile.objects.get(id=fileId)
        project_file.active = False
        project_file.save()
        return project_file
