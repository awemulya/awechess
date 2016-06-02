from django.conf.urls import url
from game import views

app_name="game"

urlpatterns = [
    url(r'^$', views.index, name='index'),
]