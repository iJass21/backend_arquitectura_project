# api/services/file_service.py
from api.repositories.file_repository import FileRepository

class FileService:
    @staticmethod
    def getFile(fileId):
        return FileRepository.findById(fileId)

    @staticmethod
    def getProjectFiles(projectId):
        return FileRepository.findByProjectId(projectId)

    @staticmethod
    def uploadFile(fileData, fileContent):
        return FileRepository.create(fileData, fileContent)

    @staticmethod
    def deleteFile(fileId):
        FileRepository.delete(fileId)

    @staticmethod
    def deactivateFile(fileId):
        return FileRepository.deactivate(fileId)
