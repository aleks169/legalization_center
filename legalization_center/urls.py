"""
Definition of urls for legalization_center.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views
#from django.contrib import admin
import app.forms
import app.views

# Uncomment the next lines to enable the admin:
#from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^$', app.views.home, name='home'),
    #url(r'^upload/$', app.views.upload, name='upload'),
    #url(r'^upload/', app.views.upload, name='upload'),
    #url(r'^admin/', include(admin.site.urls)),

    # Uncomment the admin/doc line below to enable admin documentation:
    

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
]
