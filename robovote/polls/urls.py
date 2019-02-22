from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'view/',views.index,name='index'),
    url(r'vote/',views.vote,name='vote'),
    url(r'confirm/',views.confirm,name="confirm"),
]
