from mongoengine import ValidationError
from rest_framework import status, viewsets
from rest_framework.response import Response

from guide.serializers import GuideSerializer
from guide.models import Guide

import bson


class GuideViewSet(viewsets.ViewSet):
    """
    Guide model ViewSet
    """
    serializer_class = GuideSerializer

    def list(self, request):
        """
        show list of operations guide model's operation
        """
        guideHelpMessage = [
            'Allowed operations list, create, retrieve, update, delete',
            'Automatically maps to URLs using Routers.',
        ]
        return Response({'helper': guideHelpMessage})

    def create(self, request):
        """
        create a new guide
        :param request: request
        :return: status, docId
        """
        guideSerializer = GuideSerializer(data=request.data)

        if not guideSerializer.is_valid():
            return Response({'Error': guideSerializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        else:
            docId = guideSerializer.save()[id]

        return Response({'message': 'Created guide successfully!', 'doc_id': docId}, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk):
        """
        retrieve a guide via object id
        :param request
        :param pk: primary key(unique object id in mongodb)
        :return: response
        """
        # handle invalid id format
        try:
            doc = Guide.objects(id=bson.objectid.ObjectId(pk))
        except ValidationError:
            return Response({'Error': 'Invalid id format'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            return Response({'Error': 'Unknown error'}, status=status.HTTP_400_BAD_REQUEST)

        if len(doc) >= 1:
            tmpSerializer = GuideSerializer(doc[0])
            return Response({'message': 'Retrieved guide successfully!',
                             'document': tmpSerializer.data},
                            status=status.HTTP_302_FOUND)
        # no document is found
        else:
            return Response({'Error': 'Not document found'}, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk):
        """
        delete the whole document
        :param request: whole document
        :param pk: primary key(unique object id in mongodb)
        :return: response
        """
        # handle invalid id format
        try:
            doc = Guide.objects(id=bson.objectid.ObjectId(pk))
        except ValidationError:
            return Response({'Error': 'Invalid id format'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            return Response({'Error': 'Unknown error'}, status=status.HTTP_400_BAD_REQUEST)

        if len(doc) >= 1:
            doc.delete()
            return Response({'message': 'Delete the guide successfully!'},
                            status=status.HTTP_202_ACCEPTED)
        # no document is found
        else:
            return Response({'Error': 'Not document found'}, status=status.HTTP_404_NOT_FOUND)



