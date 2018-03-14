from rest_framework_mongoengine import serializers
from guide.models import Guide


class GuideSerializer(serializers.DocumentSerializer):
    """
    Guide Serializer
    """
    class Meta:
        model = Guide
        fields = ('title',
                  'authorId',
                  'listOfProcess',
                  'dateTime',
                  'listOfTag',
                  'listOfCategory',
                  'listOfComments',
                  'listOfShare',
                  'listOfFavorite',
                  'listOfLike')
        depth = 2
