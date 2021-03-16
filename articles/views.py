from .serializers import ArticleSerializer
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from .models import Article

@csrf_exempt

# Create your views here.
def articles(request):
    if request.method == 'GET':
        articles = Article.objects.all().order_by('date')
        ser_articles = ArticleSerializer(articles,many=True)
        return JsonResponse(ser_articles.data,safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        ser_articles = ArticleSerializer(data = data)
        if ser_articles.is_valid():
            ser_articles.save()
            return JsonResponse(ser_articles.data,status=201)
        return JsonResponse(ser_articles.errors,status=400)

