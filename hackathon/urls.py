from django.conf.urls import url
from django.contrib.auth.views import password_reset, password_reset_done, password_reset_confirm, password_reset_complete 
from . import views

app_name = 'hackathon'
urlpatterns = [
    url(r'^$', views.indexView, name='index'),
    url(r'^faq/$', views.FAQView, name='faq' ),
    url(r'^add-hotspot/$', views.createHotSpotView, name='hotspot'),
    url(r'^add-service/$', views.createServiceView, name='service'),
    url(r'^submit_voting/$', views.voteView , name='voting'),
    url(r'^accounts/signup/$', views.signupView, name='signup'),
    url(r'^activate/(?P<key>.+)$', views.activationView, name = 'activate'),
    url(r'^new-activation-link/(?P<user_id>[0-9]+)/$', views.new_activation_link, name = 'new_activation_link'),
    url(r'^accounts/login/$', views.loginView, name='login'),
    url(r'^accounts/logout/$', views.logoutView, name='logout'),
    url(r'^accounts/password_reset/$', password_reset, {'post_reset_redirect':'/hackathon/accounts/password_reset/done'}, name='password_reset'),
    url(r'^accounts/password_reset/done/$', password_reset_done, name='password_reset_done'),
    url(r'^accounts/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        password_reset_confirm, {'post_reset_redirect':'/hackathon/accounts/reset/done/'},
        name='password_reset_confirm'),
    url(r'^accounts/reset/done/$', password_reset_complete, name='password_reset_complete'),
    ]
