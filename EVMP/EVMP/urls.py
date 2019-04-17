from django.conf.urls import url
from . import view

urlpatterns = [
    url(r'^$', view.hello),
    # url(r'^hello$', view.hello),
]