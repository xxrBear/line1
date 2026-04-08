from debug_toolbar.toolbar import debug_toolbar_urls
from django.conf import settings
from django.contrib import admin
from django.urls import path

from apps.blog import views as blog_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog_views.BlogView.as_view()),
]

if settings.DEBUG is True:
    urlpatterns += debug_toolbar_urls()
