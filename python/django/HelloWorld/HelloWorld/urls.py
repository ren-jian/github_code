from django.conf.urls import url
from django.contrib import admin
from . import view, testdb, search, search1

urlpatterns = [
    url(r'^hello$', view.hello),
    url(r'^testdb$', testdb.testdb),
    url(r'^search-form$', search.search_form),
    url(r'^search$', search.search),
    url(r'^search-post$', search1.search_post),
    url(r'^admin/', admin.site.urls),
]
