from django.shortcuts import render
from .models import Post
from rest_framework.generics import ListCreateAPIView

from .serializers import PostSerializer


# Create your views here.

def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html',{'posts':posts})

class PostListAPIView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

post_list_api_view = PostListAPIView.as_view()
