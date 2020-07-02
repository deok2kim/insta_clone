from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

# from .models import Article
# from .serializers import ArticleListSerializer, ArticleSerializer
from .models import User
from .serializers import UserSerializer

# Create your views here.
@api_view(['GET'])
def profile(request, username):
    print('안되나?')
    user = get_object_or_404(User, username=username)
    serializer = UserSerializer(user)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def follow(request, username):
    me = request.user.username
    you = get_object_or_404(User, username=username)
    print(me, you)
    pass

