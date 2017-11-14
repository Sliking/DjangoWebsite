from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'), # Setup home page for each individual app ^ is begin and $ is end
]