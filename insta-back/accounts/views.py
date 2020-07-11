from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

# from .models import Article
# from .serializers import ArticleListSerializer, ArticleSerializer
from .models import User
from .serializers import UserSerializer

from articles.models import Article
from articles.serializers import ArticleListSerializer

# Create your views here.
@api_view(['GET'])
def profile(request, username):
    profile_user = get_object_or_404(User, username=username)
    serializer = UserSerializer(profile_user)

    me = request.user

    # 팔로우 관련 데이터: 팔로우했는지 안했는지
    status = 'me'
    if me == profile_user:
        pass
    elif profile_user.followers.filter(pk=me.pk).exists():
        status = True
    else:
        status = False
    
    data = {
        'isFollow': status
    }  
    data.update(serializer.data)

    # 팔로워 수
    followers3 = user.followers.filter(pk=profile_user.pk)
    print(followers3)
    return Response(data)

@api_view(['GET'])
def user_article_list(request, username):
    user = get_object_or_404(User, username=username)
    articles = Article.objects.filter(user=user)
    serializer = ArticleListSerializer(articles, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def follow(request, username):
    me = request.user
    you = get_object_or_404(User, username=username)
    status = ''
    if me == you:
        pass
    elif you.followers.filter(pk=me.pk).exists():
        you.followers.remove(me)
        status = False
    else:
        you.followers.add(me)
        status = True  
    
    return Response(status)
