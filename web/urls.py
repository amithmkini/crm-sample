from django.conf.urls import url
from . import views

app_name = 'web'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^logout/$', views.logout_user, name='logout_user'),
    url(r'^compare/$', views.compare, name='compare'),
    url(r'^accounts/$', views.accounts, name='accounts'),
    url(r'^accounts/create/$', views.account_create, name='account_create'),
    url(r'^accounts/(?P<aid>[0-9]+)/$', views.account, name='account'),
    url(r'^accounts/(?P<aid>[0-9]+)/edit/$', views.account_update, name='account_update'),
    url(r'^contacts/$', views.contacts, name='contacts'),
    url(r'^contacts/(?P<cid>[0-9]+)/$', views.contact, name='contact'),
    url(r'^contacts/create/$', views.contact_create, name='contact_create'),
    url(r'^contacts/(?P<cid>[0-9]+)/edit/$', views.contact_update, name='contact_update'),
    url(r'^leads/(?P<lid>[0-9]+)/$', views.lead, name='lead'),
    url(r'^leads/(?P<lid>[0-9]+)/edit/$', views.lead_update, name='lead_update'),
    url(r'^leads/$', views.leads, name='leads'),
    url(r'^leads/create/$', views.lead_create, name='lead_create'),
    url(r'^opportunities/(?P<oid>[0-9]+)/$', views.opportunity, name='opportunity'),
    url(r'^opportunities/$', views.opportunities, name='opportunities'),
    url(r'^opportunities/create/$', views.opportunity_create, name='opportunity_create'),
    url(r'^opportunities/(?P<oid>[0-9]+)/edit/$', views.opportunity_update, name='opportunity_update'),
    url(r'^chart1/$', views.chart1, name='chart1'),
    url(r'^chart2/$', views.chart2, name='chart2'),
    url(r'^chart3/$', views.chart3, name='chart3')
]
