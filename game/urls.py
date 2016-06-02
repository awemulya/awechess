from django.conf.urls import url
from game import views

app_name="game"

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^search/$', views.search_by_moves, name='search_by_moves'),
]