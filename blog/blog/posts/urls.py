from django.urls import path
from .views import post_list_api_view,index
urlpatterns = [
    path('', index, name='index'),
    path('posts/', post_list_api_view),
]