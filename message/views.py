from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.authentication import TokenAuthentication # get user
from rest_framework.permissions import IsAuthenticated

from .models import Message, Requests
from .serializer import Requestserilazer

class Messagefunc(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        new_message = Message(
            name=request.data.get('name'),
            sendedBy= request.user,
            message=request.data.get('message')
        )
        new_message.save()
        return Response({
            "success": True
        })


class Requestfunc(APIView):
    def post(self, request):
        serializer = Requestserilazer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            request_saved = serializer.save()
        return Response({
            "success": True
        })

