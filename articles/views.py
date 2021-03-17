from .serializers import ArticleSerializer,UserSerializer
from .models import Article
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.contrib.auth.models import User
from rest_framework import viewsets

class ArticlesViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = (TokenAuthentication,)
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
