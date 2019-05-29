
from django.conf.urls import url
from app1 import views

urlpatterns = [
    url('review/', views.index,name='review'),
    url('contact/', views.contact,name='contact'),
]
