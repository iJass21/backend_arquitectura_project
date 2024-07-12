# api/repositories/file_repository.py
from api.models import ProjectFile, File
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import uuid
from datetime import datetime
import os

class FileRepository:
    @staticmethod
    def findById(fileId):
        return ProjectFile.objects.get(id=fileId)

    @staticmethod
    def findByProjectId(projectId):
        return ProjectFile.objects.filter(project_id=projectId)

    @staticmethod
    def create(fileData, fileContent):
        file_instance = FileRepository.saveFile(fileContent)
        project_file_data = {
            'project': fileData['project'],
            'file': file_instance,
            'title': fileData['title'],
            'description': fileData.get('description', ''),
            'active': True
        }
        return ProjectFile.objects.create(**project_file_data)


    @staticmethod
    def saveFile(fileContent, random_filename=False):
        file_name = fileContent.name
        if random_filename:
            current_date = datetime.now().strftime("%Y%m%d")
            file_name = f"{uuid.uuid4().hex}_{current_date}{os.path.splitext(file_name)[1]}"

        relative_path = os.path.join('media/', file_name)

        file_path = default_storage.save(file_name, ContentFile(fileContent.read()))
        return File.objects.create(route=relative_path, active=True)
    
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