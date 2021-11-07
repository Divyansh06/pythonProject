from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import models, serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

invalid_data = {'Error': 'Invalid Data!'}


@api_view(['GET'])
def api_overview(request):
    api_urls = {
        'Sign up': '/accounts/user-signup',
        'Sign in': '/accounts/user-signin',
        'All Users': '/accounts/get-users',
        'Get user': '/accounts/get-users/<str:pk>',
    }
    return Response(api_urls)


# User Views
@api_view(['POST'])
def user_create(request):
    serializer = serializers.UserSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(status=500, data=invalid_data)


@api_view(['POST'])
def user_login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'Error': 'Invalid Credentials'}, status=400)
    token, created = Token.objects.get_or_create(user=user)
    return Response({'token': token.key, 'success': 'true'}, status=200)


@api_view(['GET'])
def user_logout(request):
    request.user.auth_token.delete()
    return Response(status=200, data={'success': True})


@api_view(['GET'])
def user_list(request):
    users = models.User.objects.all()
    serializer = serializers.UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def user_list_django(request):
    users = User.objects.all()
    serializer = serializers.UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def user_details(request, pk):
    users = models.User.objects.get(id=pk)
    serializer = serializers.UserSerializer(users, many=False)
    return Response(serializer.data)
