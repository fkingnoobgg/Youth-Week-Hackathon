from django.conf.urls import url
from django.contrib.auth.views import password_reset, password_reset_done, password_reset_confirm, password_reset_complete 
from . import views

app_name = 'logbook'
urlpatterns = [
    url(r'^$', views.indexView, name='index'),
    url(r'^faq/$', views.FAQView, name='faq' ),
    ]
