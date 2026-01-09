import random
import string

from rest_framework import status
from rest_framework.decorators import renderer_classes

from .models import UrlData
from .forms import Url
from django.shortcuts import render,redirect
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from .serializers import UrlSerializer

class UrlList(ListCreateAPIView):
    queryset = UrlData.objects.all()
    serializer_class = UrlSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'index2.html'

    def list(self, request, *args, **kwargs):
        queryset =self.get_queryset()
        serializer = self.get_serializer()
        return Response({'data':queryset,'serializer':serializer})

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            self.perform_create(serializer)
            return redirect('/shortener/')
        queryset = self.get_queryset()
        return Response({'data':queryset,'serializer':serializer},status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        random_slug= ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(10))
        serializer.save(slug=random_slug)

url_list_view = UrlList.as_view()

