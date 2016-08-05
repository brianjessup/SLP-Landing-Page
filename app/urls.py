from django.conf.urls import patterns, url, include
from django.views.generic import RedirectView, TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # We give the root view the name 'auth_login', since this is what other
    # packages such as django.contrib.auth expect the login view to be named.
    # -> If the user is logged in, they are shown the dashboard.
    # -> If not, they are shown the landing page.
    url(r'^$', TemplateView.as_view(template_name='landing/slp-base.html'), name='home'),
    url(r'^referrals/$', TemplateView.as_view(template_name='fellow-incentive-program-results.html'), name='incentive_program'),


)
