from django.urls import path
from .views import url_list_view

app_name = "url"

urlpatterns = [
    path("", url_list_view),  # Home route for URL shortening form
    #path("u/<str:slugs>", views.urlRedirect, name="redirect"),  # Redirect using the slug
]