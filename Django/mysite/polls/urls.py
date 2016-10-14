from django.conf.urls import url

from . import views

urlpatterns = [
    # url(r'^polls/$', views.index, name='index'),
    url(r'^test/', views.test, name='test'),
    url(r'^$', views.mgs_pull, name='mgs_pull'),
]
