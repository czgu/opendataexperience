from django.conf.urls import patterns, url

from webapp import views

urlpatterns = patterns('',
    url(r'^(home/)?$', views.home, name="home"),
    url(r'^tracker/$', views.tracker, name="nutritionTracker"),
    url(r'^about/(?P<item>[A-Za-z]+)?$', views.about, name="about"),
    url(r'^contact/$', views.contact, name="contact")
)
