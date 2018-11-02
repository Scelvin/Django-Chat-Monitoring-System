from django.conf.urls import include, url
from django.contrib import admin
from . import views

admin.autodiscover()
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('alpha.urls')),
    url(r'^$', views.Login, name='login'),
]

def __unicode__(self):
    return self.message

