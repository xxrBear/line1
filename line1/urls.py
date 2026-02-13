from debug_toolbar.toolbar import debug_toolbar_urls
from django.conf import settings
from django.contrib import admin
from django.urls import path

from apps.blog import views as blog_views

urlpatterns = [
    path('', blog_views.BlogView.as_view()),
    path('admin/', admin.site.urls),
]

if settings.DEBUG is True:
    urlpatterns += debug_toolbar_urls()
