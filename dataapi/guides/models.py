from mongoengine import Document, EmbeddedDocument, connect
from mongoengine.fields import *


connect('mydb')


class Comments(Document):
    """
    评论的Document
    """
    authorId = StringField(required=True)
    # the id of the document that owns the comment
    documentId = StringField(required=True)
    # id of the recipient of the comment
    recipientId = StringField(default=None)
    text = StringField(max_length=500)


class Process(EmbeddedDocument):
    """
    embedded process document
    """
    text = StringField()
    listOfImage = ListField(StringField())


class BaseDocument(Document):
    """
    基本文档 document
    """
    title = StringField(required=True)
    authorId = StringField(required=True)
    listOfProcess = ListField(EmbeddedDocumentField(Process))
    dateTime = DateTimeField(required=True, help_text='date published')
    listOfTag = ListField(StringField(max_length=200))
    listOfCategory = ListField(StringField())

    meta = {'allow_inheritance': True}


class Guide(BaseDocument):
    """
    攻略的Document
    """
    # list of comment id
    listOfComments = ListField(StringField())
    # list of user id who shares the guide
    listOfShare = ListField(StringField())
    # list of user id who add it to their favorite collection
    listOfFavorite = ListField(StringField())
    # list of user id who likes this guide
    listOfLike = ListField(StringField())
    #
    # def __init__(self):
    #     Document.__init__(self)
    #     BaseDocument.__init__(self)
