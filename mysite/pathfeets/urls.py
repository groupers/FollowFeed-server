from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^api/event/(?P<token>[a-zA-Z0-9]+)/$', views.details, name='details'),
    url(r'^api/send_gps/$', views.receive_gps_coord, name='send_gps'),
    url(r'^api/make_planned_pos/$', views.make_planned_pos, name='make_planned_pos'),
    url(r'^api/create/$', views.create_event, name='create event'),
    url(r'^api/send_gps/$', views.receive_gps_coord, name='send_gps'),
]
