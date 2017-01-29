from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^event/(?P<token>[a-zA-Z0-9]+)/$', views.details, name='details'),
    url(r'^create/$', views.create_event, name='create event')
]
