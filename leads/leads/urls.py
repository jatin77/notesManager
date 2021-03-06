from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from django.conf.urls import url
from .views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('', include('posts.urls')),
    path('', include('accounts.urls')),
    # url(r'^.*', TemplateView.as_view(template_name="index.html"), name="index"),
]
