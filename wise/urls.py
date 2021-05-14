from django.urls import path
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from .views import index


urlpatterns = [
    path('', index, name='index'),
]
