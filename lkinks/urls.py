from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from views import homepage,imagesave
from django.views.generic import TemplateView as TView
from django.views.static import serve

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',homepage,name='home'),
    url(r'^about/$',TView.as_view(template_name='about.html'),name='about'),
    url(r'^products/$',TView.as_view(template_name='services.html'),name='products'),
    url(r'^contactus/$',TView.as_view(template_name='contact.html'),name='contact'),
    url(r'^sitemap/$',TView.as_view(template_name='sitemap.xml'),name='sitemap'),
    url(r'^ajax/actions/$',imagesave,name='imagesave'),
    url(r'^lkmedia/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]
