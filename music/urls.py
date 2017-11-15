from django.conf.urls import url
from . import views

urlpatterns = [
    # Setup home page for each individual app ^ is begin and $ is end
    url(r'^$', views.index, name='index'),

    url(r'^(?P<album_id>[0-9]+)$', views.details, name="details"),
]