from api.models import ProjectFile

class FileRepository:
    @staticmethod
    def findById(fileId):
        return ProjectFile.objects.get(id=fileId)

    @staticmethod
    def create(fileData):
        return ProjectFile.objects.create(**fileData)

    @staticmethod
    def delete(fileId):
        file = ProjectFile.objects.get(id=fileId)
        file.delete()

    @staticmethod
    def deactivate(fileId):
        file = ProjectFile.objects.get(id=fileId)
        file.active = False
        file.save()
        return file
