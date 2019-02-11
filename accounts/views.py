from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework import generics
from rest_framework import permissions
from rest_framework.permissions import AllowAny
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from accounts.serializers import UserSerializer
# from .models import create_auth_token
from rest_framework.authtoken.models import Token


class UserCreate(generics.CreateAPIView):
    # print('I am in class of registration')
    """
    Create the users
    """

    model = User
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UserSerializer
    print(serializer_class.errors)
    print(serializer_class)


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=status.HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=status.HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},
                    status=status.HTTP_200_OK)



