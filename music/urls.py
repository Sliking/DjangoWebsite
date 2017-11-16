from django.conf.urls import include, url
from . import views
from dashing.utils import router

urlpatterns = [
    # Setup home page for each individual app ^ is begin and $ is end
    url(r'^$', views.index, name='index'),
    url(r'^dashboard/', include(router.urls)),
    url(r'^(?P<album_id>[0-9]+)/$', views.details, name="details"),
]