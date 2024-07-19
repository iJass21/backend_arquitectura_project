# api/services/comment_service.py
from api.repositories.comment_repository import CommentsRepository
from api.models import Comment, Project, User

class CommentsService:
    @staticmethod
    def addComment(project_id, data):
        project = Project.objects.get(id=project_id)
        #user = User.objects.get(id=data['user'])
        print("project id", project_id)
        print("project data", project)
        print("comment data", data)
        #print("user test", user)
        comment = Comment.objects.create(
            project=project,
            user=data['user'],
            content=data['content']
        )
        return comment

    @staticmethod
    def updateComment(commentId, commentData):
        return CommentsRepository.update(commentId, commentData)

    @staticmethod
    def deleteComment(commentId):
        CommentsRepository.delete(commentId)

    @staticmethod
    def deactivateComment(commentId):
        return CommentsRepository.deactivate(commentId)
    
    @staticmethod
    def getComments(projectId):
        return CommentsRepository.findByProjectId(projectId)
