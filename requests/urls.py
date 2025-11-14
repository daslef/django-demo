from django.urls import path
from . import views

urlpatterns = [
    path('', views.requests_list),
    path('new', views.create_request)
]
