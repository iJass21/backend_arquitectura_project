from django.contrib import admin
from .models import User, Project, Comment, Like, ProjectMember, Reference, File, ProjectFile, Tag, ProjectTag

admin.site.register(User)
admin.site.register(Project)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(ProjectMember)
admin.site.register(Reference)
admin.site.register(File)
admin.site.register(ProjectFile)
admin.site.register(Tag)
admin.site.register(ProjectTag)
