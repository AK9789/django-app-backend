from rest_framework.response import Response
from .models import User
from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed
import jwt, datetime
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.authentication import TokenAuthentication # get user
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate, login
from django.http import HttpResponse 



from .models import User
from .serializers import Userserializer


# USER LOGIN
class login(ObtainAuthToken):
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            # print(f'====================={Token}')
            token, created =  Token.objects.get_or_create(user=serializer.validated_data['user'])
            # return Response({'token': token.key})
            print(token)
            response = Response()  
            response.set_cookie('token',f'Token {token.key}',samesite='Lax')
            return Response({'token': f'Token {token.key}'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# USER LOGIN
class GetUser(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    
    def get(self, request):
        # print(request.user)
        user = User.objects.get(username__iexact=request.user)
        serializer = Userserializer(user, many=False)
        # print(serializer.data)
        return Response({
            'user': serializer.data
        })

class Register(APIView):
    def post(self, request):
        serializer = Userserializer(data=request.data)
        print(request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
# class wish(APIView):
#     def get(self, request):
#         print("hello")
#         return Response(print('hello'))