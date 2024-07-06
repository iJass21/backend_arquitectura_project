from api.repositories.file_repository import FileRepository

class FileService:
    @staticmethod
    def getFile(fileId):
        return FileRepository.findById(fileId)

    @staticmethod
    def uploadFile(fileData):
        return FileRepository.create(fileData)

    @staticmethod
    def deleteFile(fileId):
        FileRepository.delete(fileId)

    @staticmethod
    def deactivateFile(fileId):
        return FileRepository.deactivate(fileId)
