from api.models import ProjectTag

class ProjectTagRepository:
    @staticmethod
    def create(project_tag_data):
        return ProjectTag.objects.create(**project_tag_data)

    @staticmethod
    def delete(project_tag_id):
        project_tag = ProjectTag.objects.get(id=project_tag_id)
        project_tag.delete()

    @staticmethod
    def find_by_id(project_tag_id):
        return ProjectTag.objects.get(id=project_tag_id)

    @staticmethod
    def find_by_project_id(project_id):
        return ProjectTag.objects.filter(project_id=project_id)