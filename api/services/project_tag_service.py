from api.repositories.project_tag_repository import ProjectTagRepository
from api.repositories.tag_repository import TagRepository
from api.repositories.project_repository import ProjectRepository
class ProjectTagService:
    @staticmethod
    def add_project_tag(project_tag_data):
        project = project_tag_data.pop('project')
        tag = project_tag_data.pop('tag')
        project_tag_data['tag'] = tag
        project_tag_data['project'] = project
        return ProjectTagRepository.create(project_tag_data)

    @staticmethod
    def delete_project_tag(project_tag_id):
        ProjectTagRepository.delete(project_tag_id)

    @staticmethod
    def get_project_tag(project_tag_id):
        return ProjectTagRepository.find_by_id(project_tag_id)

    @staticmethod
    def get_project_tags(project_id):
        return ProjectTagRepository.find_by_project_id(project_id)