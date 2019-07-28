from django.urls import path
from hello import views

urlpatterns = [
    path("", views.home, name="home"),
    path("json-data", views.json_data),
    path("post-request", views.post_request),
]