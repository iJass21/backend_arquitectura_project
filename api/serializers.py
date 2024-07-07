from rest_framework import serializers
from .models import User, Project, Comment, Like, ProjectMember, Reference, File, ProjectFile, Tag, ProjectTag

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'name', 'lastname', 'role', 'created_at', 'active']
        read_only_fields = ['id', 'created_at', 'active']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'project', 'user', 'content', 'created_at', 'active']
        read_only_fields = ['id', 'created_at', 'active']

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id', 'project', 'user', 'created_at']
        read_only_fields = ['id', 'created_at']

class ProjectMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectMember
        fields = ['id', 'project', 'user', 'active']
        read_only_fields = ['id']

class ReferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reference
        fields = ['id', 'project', 'description', 'created_at', 'active']
        read_only_fields = ['id', 'created_at', 'active']

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ['id', 'route', 'active']
        read_only_fields = ['id', 'active']

class ProjectFileSerializer(serializers.ModelSerializer):
    file = FileSerializer(read_only=True)

    class Meta:
        model = ProjectFile
        fields = ['id', 'project', 'file', 'title', 'description', 'active']

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name', 'active']
        read_only_fields = ['id']

    def validate_name(self, value):
        if Tag.objects.filter(name=value).exists():
            raise serializers.ValidationError("A tag with this name already exists.")
        return value

class ProjectTagSerializer(serializers.ModelSerializer):
    tag = TagSerializer(read_only=True)
    class Meta:
        model = ProjectTag
        fields = ['id', 'project', 'tag', 'active']
        read_only_fields = ['id', 'active']
        
class ProjectSerializer(serializers.ModelSerializer):
    project_files = ProjectFileSerializer(many=True, read_only=True)
    project_members = ProjectMemberSerializer(many=True, read_only=True)
    project_tags = ProjectTagSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = [
            'id', 'name', 'owner', 'description', 'created_at', 'active',
            'project_files', 'project_members', 'project_tags', 'comments'
        ]
        read_only_fields = ['id', 'created_at', 'active']
