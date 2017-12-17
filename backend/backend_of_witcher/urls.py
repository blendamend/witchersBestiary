from django.conf.urls import url
from backend_of_witcher import views

urlpatterns = [
    url(r'^$', views.index),
]