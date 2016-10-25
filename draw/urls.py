from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'submit$', views.submit),
    url(r'danger_init$', views.init)
]
