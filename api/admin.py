# api/admin.py
from django.contrib import admin
from .models import User, Project, Comment, Like, ProjectMember, Reference, File, ProjectFile, Tag, ProjectTag

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','email', 'name', 'lastname', 'role', 'created_at', 'active')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'owner', 'description', 'created_at', 'active')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id','project', 'user', 'content', 'created_at', 'active')

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('id','project', 'user', 'created_at')

@admin.register(ProjectMember)
class ProjectMemberAdmin(admin.ModelAdmin):
    list_display = ('id','project', 'user', 'active')

@admin.register(Reference)
class ReferenceAdmin(admin.ModelAdmin):
    list_display = ('id','project', 'description', 'created_at', 'active')

@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ('id','route', 'active')

@admin.register(ProjectFile)
class ProjectFileAdmin(admin.ModelAdmin):
    list_display = ('id','project', 'file', 'title', 'description', 'active')

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'active')

@admin.register(ProjectTag)
class ProjectTagAdmin(admin.ModelAdmin):
    list_display = ('id','project', 'tag', 'active')
