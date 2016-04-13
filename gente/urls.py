from django.conf.urls import patterns, include, url
from django.views.generic import ListView, TemplateView, RedirectView
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gente.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^facebook/', include('facebook_login.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ai/', include('genteai.urls')),
    url(r'^logout/','genteai.views.logout_user', name='logout'),
    url(r'^$', TemplateView.as_view(template_name="index.html"), name='index')
)
