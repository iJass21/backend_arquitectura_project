#
from api.repositories.tag_repository import TagRepository

class TagService:
    @staticmethod
    def add_tag(tag_data):
        return TagRepository.create(tag_data)

    @staticmethod
    def delete_tag(tag_id):
        TagRepository.delete(tag_id)

    @staticmethod
    def get_tag(tag_id):
        return TagRepository.find_by_id(tag_id)

    @staticmethod
    def get_all_tags():
        return TagRepository.find_all()
