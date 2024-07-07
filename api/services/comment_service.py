# api/services/comment_service.py
from api.repositories.comment_repository import CommentsRepository

class CommentsService:
    @staticmethod
    def addComment(projectId, commentData):
        commentData['project_id'] = projectId
        return CommentsRepository.create(commentData)

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
