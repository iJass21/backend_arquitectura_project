from api.models import Comment

class CommentsRepository:
    @staticmethod
    def create(commentData):
        return Comment.objects.create(**commentData)

    @staticmethod
    def update(commentId, commentData):
        comment = Comment.objects.get(id=commentId)
        for key, value in commentData.items():
            setattr(comment, key, value)
        comment.save()
        return comment

    @staticmethod
    def delete(commentId):
        comment = Comment.objects.get(id=commentId)
        comment.delete()

    @staticmethod
    def deactivate(commentId):
        comment = Comment.objects.get(id=commentId)
        comment.active = False
        comment.save()
        return comment

    @staticmethod
    def findById(commentId):
        return Comment.objects.get(id=commentId)
