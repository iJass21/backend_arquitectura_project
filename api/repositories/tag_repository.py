# api/repositories/tag_repository.py
from api.models import Tag

class TagRepository:
    @staticmethod
    def create(tag_data):
        return Tag.objects.create(**tag_data)

    @staticmethod
    def delete(tag_id):
        tag = Tag.objects.get(id=tag_id)
        tag.delete()

    @staticmethod
    def find_by_id(tag_id):
        return Tag.objects.get(id=tag_id)

    @staticmethod
    def find_all():
        return Tag.objects.all()
